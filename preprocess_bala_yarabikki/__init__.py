from preprocess_bala_yarabikki import utils

__version__='0.0.2'

def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlenght(x):
	return utils._get_avg_wordlenght(x)

def get_stopwords(x):
	return utils._get_stopwords(x)

def get_hashtag_counts(x):
	return utils._get_hashtag_counts(x)

def get_mention_counts(x):
	return utils._get_mention_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_upercase_counts(x):
	return utils._get_upercase_counts(x)

def get_lower_counts(x):
	return utils._get_lower_counts(x)

def get_emails(x):
	return utils._get_emails(x)

def get_remove_emails(x):
	return utils._get_remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_tr(x):
	return utils._remove_tr(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_htmltags(x):
	return utils._remove_htmltags(x)

def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)

def remove_commonwords(x,n=20):
	return utils._remove_commonwords(x,n)

def remove_rarewords(x, n=20):
	return utils._remove_rarewords(x,n)

def spelling_correction(x):
	return utils._spelling_correction(x)










