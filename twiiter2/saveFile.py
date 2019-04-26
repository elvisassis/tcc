import time
from datetime import date
from nlputils.lexical import Preprocessing

class SaveFile(object):

	def __init__(self):
		self.pre = Preprocessing()

	#Salva os dados no formato txt sem limpar os dadoss
	def salvarArquivoTxt(self, pathArquivo, fileName, twittes, data):

		with open(pathArquivo + fileName + '-' + data + '.txt', 'a') as twitterFile:
			for twitte in twittes['statuses']:
				frase = twitte['full_text']
				self.salvarArquivoTxtPadronizado(pathArquivo, fileName + '-texto-tratado', frase, data)
				twitterFile.write(twitte['full_text'] + '\n')
	

	#salva um arquivo csv com os a data de criação do twitter
	def salvarArquivoCsv(self, pathArquivo, fileName, twittes, data):

		with open(pathArquivo + fileName + '-' + data + '.csv', 'a') as twitterFile:
			for twitte in twittes['statuses']:
				data = twitte['created_at']
				obj_date = time.strptime(data, "%a %b %d %H:%M:%S +0000 %Y")
				data_convertida = time.strftime('%d/%m/%Y', obj_date)

				twitterFile.write(twitte['full_text'] + ";" + data_convertida + '\n')

	#padroniza pra minuscula e remove os links e salva o arquivo em txt
	def salvarArquivoTxtPadronizado(self, pathArquivo, fileName, frase, data):

		with open(pathArquivo + fileName + '-' + data +'.txt', 'a') as textoTratado:

			frase = self.pre.remove_acentos(frase)
			frase = self.pre.remove_link(frase)
			frase = self.pre.text_to_lower(frase)
			textoTratado.write(frase + '\n')