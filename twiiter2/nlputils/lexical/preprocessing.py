import nltk
import unidecode
import string
from nltk.corpus import stopwords


class Preprocessing(object):
	
	def __init__(self):
		self.stemmer = nltk.stem.RSLPStemmer()
		self.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
		self.stop_words = set(stopwords.words('portuguese'))

	def remove_acentos(self,text):
		return unidecode.unidecode(text)
	
	def remove_link(self, text):
		frase = []
		text = text.split()
		for palavra in text:
			if 'http' not in palavra:
				frase.append(palavra + ' ')
				
		return ''.join(frase)
	
	def text_to_lower(self, text):
		frase = []
		text = text.split()
		for palavra in text:
			frase.append(palavra.lower() + ' ')
				
		return ''.join(frase)
		

	def remove_pontuacao(self, text):
		return text.translate(str.maketrans('','',string.punctuation))

	def tokenize_sentences(self, text):
		sentences = self.sent_tokenizer.tokenize(text)
		return sentences

	def tokenize_words(self, text):
		tokens = nltk.tokenize.word_tokenize(text)
		return tokens
	
	def remove_stopwords(self, text):
		text = [palavra for palavra in text if palavra not in self.stop_words]
		return text

	def lemmatize(self, text):
		return text

	def stemmize(self, tokens):
		return [self.stemmer.stem(words) for words in tokens]	

	def normalization_pipelines(self,text, remove_accents=False, remove_pontuacao=False, tokenize_sentences=False,
						   tokenize_words=False, lemmatize=False, stemmize=False):

		text = remove_accents(text) if remove_accents else text
		text = remove_pontuacao(text) if remove_pontuacao else text
		text = tokenize_sentences(text) if tokenize_sentences else text
		text = tokenize_words(text) if tokenize_words else text
		text = lemmatize(text) if lemmatize else text
		text = stemmize(text) if stemmize else text
	
		return text