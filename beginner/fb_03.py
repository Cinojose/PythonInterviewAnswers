
"""
Word count
==============
Script to count the number of occurance of each word in the file

""""




import os
from collections import Counter

def get_key(item):
	return item[1]



def count_word_bag(word_bag):
	main_list = []
	for l in Counter(word_bag).items():
		main_list.append(l)
	main_list = sorted(main_list,key=get_key,reverse=True)
	print main_list[:5]

if __name__== "__main__":
	word_bag = []
	word_str=""
	with open(os.getcwd()+"/../files/fb_03.txt") as f:
		for line in f:
			word_str = word_str + line
	count_word_bag(word_str.split())
