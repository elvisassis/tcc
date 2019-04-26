import json
import time
from requests_oauthlib import OAuth1Session
from saveFile import SaveFile
 
MAX_TWEETS = 100
BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"
DATA = '2019-04-25'
PARAMETROS_ADICIONAIS="&lang=pt&until=" + DATA + "&tweet_mode=extended"

salvarAquivo = SaveFile()

 
class MyTwitterSearchClient(object):
	API_KEY ='oEBYr4PCt5JUwVU8GrmGFu5IN'
	API_SECRET ='UaKnly8PASu0uBDD5uptWhrJpS9x3F7ocD1Ug96Co6LwpUAvtu'
	ACCESS_TOKEN ='203499657-G0tWOHVql9ST5D8utmbgjBCW8IPsOABu18C8ff99'
	ACCESS_TOKEN_SECRET ='5q4UtXfu70OjSdYNH17FIRz1hCLH1rF8w2nWokMrMmnt3'
	 
	 
	 #inicializa o auth com as credenciais necessárias para acessar a api to twitter
	def __init__(self):
		self.session = OAuth1Session(self.API_KEY,
									 self.API_SECRET,
									 self.ACCESS_TOKEN,
									 self.ACCESS_TOKEN_SECRET)
	
	def get_twittes(self, keyword, n=15, max_id=None):
		if n > 0:
			print(n)
			url = BASE_URL + ("?q=%s&count=%d" % (keyword, n)) + PARAMETROS_ADICIONAIS

			
			if max_id is not None:
				url = url + "&max_id=%d" % (max_id)

			response = self.session.get(url)
			print(response.status_code)

			if (response.status_code == 200):

				twittes = json.loads(response.content.decode('utf-8'))
				salvarAquivo.salvarArquivoTxt("data/claro/", "claro", twittes, DATA)
				salvarAquivo.salvarArquivoCsv("data/claro/", "claro", twittes, DATA)
				max_id = twittes['search_metadata']['max_id']

				return twittes['statuses'] + \
					self.get_twittes(keyword, n-MAX_TWEETS, max_id)
		return []
