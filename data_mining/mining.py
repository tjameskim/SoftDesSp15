"""
This file will take data from google
Regarding famous soccer players, those listed 
as the top 23 players last season, and run through
google results and news articles to recieve a count
of how many times each players name shows up when 
something generic is searched like, "Soccer", 
"European Football", "Ballon'dor" that relates to 
all the players. This will be used to determine the
correlation between popularity of a player, defined by 
the number of hits, and the ranking.
"""

import string
import codecs
import nltk
import bs4

Soupy = bs4.BeautifulSoup
#set search engine
from pattern.web import *
g = Google(license = 'AIzaSyCuEyc5AbPiV86BjzBIWZwlxOMD5r7rU4Y')

def process_file(filename):
	"""
	This code is from TP that takes in a text file and 
	creates a histogram with all the words
	and uses the function process_line
	"""
	hist = dict()
	fp = open(filename)
	for line in fp:
		process_line(line,hist)
	return hist

def process_line(line,hist):
	line = line.replace('-','')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()

		hist[word] = hist.get(word,0)+1

def search(google_search):
	""" Writes a text file on computer with content 
	from google search, named "search_text"
	"""
	all_Results = []
	for result in g.search(google_search):
		url = result.url
		txt = URL(url).download()
		soup = Soupy(txt)
		search_text = str(soup.get_text().encode('utf8'))
		all_Results.append(search_text)
	return all_Results	

def mult_searches(m_search):
	"""Creates a single text file with a lot of text 
	from multiple google searches"""
	all_Search_Results = []
	for topic in m_search:
		all_Search_Results.extend(search(topic))
	fp = codecs.open('search_text','r+')
	fp.write(''.join(all_Search_Results))

def name_freq(m_search,players):
	"""
	Makes a dictionary of player:freq, 
	and outputs how many times a player was mentioned
	in the searches
	"""
	#creating the empty dictionary for output
	player_freq = {}

	#mining and filtering the data textfile
	mult_searches(m_search)
	hist = process_file('search_text')

	#creating final dictionary
	for player in players:
		if player in hist:
			player_freq[player] = hist[player]
		else:
			player_freq[player] = 0

	return player_freq

#creates new empty textfile to store our information
open('search_text','w')

#shortlist for 23 candidates for Ballon'dor Award
#names should be all lower case, un separated string, (last name), to simplify counting process
players_list = ['bale','benzema', 'costa', 
'courtois','maria','gotze', 
'hazard','ibrahimovic','iniesta',
'kroos','lahm','mascherano',
'messi','muller','neuer',
'neymar','pogba','ramos','robben',
'rodriguez','ronaldo','schweinsteiger',
'toure']

#what to search in google
m_search = ['soccer','european football','ballon dor',
'champions league','world cup']

print name_freq(m_search,players_list)