import re 
import os
import sys
import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import bs4
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

def _get_wordcounts(x):
	lenght = len(str(x).split())
	return lenght
def _get_charcounts(x):
	s = x.split()
	x = ''.join(s)
	return len(x)
def _get_avg_wordlenght(x):
	count = _get_charcounts(x)/_get_wordcount(x)
	return count
def _get_stopwords(x):
	l = len([t for t in x.split() if t in STOP_WORDS])
	return l
def _get_hashtag_counts(x):
	l = len([t for t in x.split() if t.startswith('#')])
	return l
def _get_mention_counts(x):
	l = len([t for t in x.split() if t.startswith('@')])
	return l
 

def _get_digit_counts(x):
	l = len([t for t in x.split() if t.isdigit()])
	return l
def _get_upercase_counts(x):

	l = len([t for t in x.split() if t.isupper()])
	return l
def _get_lower_counts(x):
	l = len([t for t in x.split() if t.islower()])
	return l
def _get_emails(x):
	emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)',x)
	counts = len(emails)
	return counts, emails
def _get_remove_emails(x):
	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)','',x)
def _get_urls(x):
	urls = len(re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',x))
	counts = len(urls)
	return counts, urls
def _remove_urls(x):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?','',x)
def _remove_tr(x):
	return  re.sub(r'\brt\b','',x).strip()
def _remove_special_chars(x):
	x = re.sub(r'[^\w ]+','',x)
	x = ' '.join(x.split())
def _remove_htmltags(x):
	return BeautifulSoup(x,'lxml').get_text().strip()
def _remove_accented_chars(x):
	x = unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
	return x
def _remove_stopwords(x):
	return ' '.join([t for t in x.split() if t in STOP_WORDS])
def _make_base(x):
	x = str(x)
	x_list = []
	doc = nlp(x)
	
	for token in doc:
		lemma = token.lemma_
		if lemma == 'PORN' or lemma =='b':
			lemma = token.text
		
		x_list.append(lemma)
	return ' '.join(x_list)

def _remove_commonwords(x,n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm[:n]

	x = ' '.join(t for t in x.split() if t not in fn)
	return x
def _remove_rarewords(x, n=20):
	text = x.split()
	freq_comm = pd.Series(text).value_counts()
	fn = freq_comm.tail(n)
	x = ' '.join(t for t in x.split() if t not in fn)
	return x
def _spelling_correction(x):
	x = TextBlob(x).correct()
	return x











