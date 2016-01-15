#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('janome')
from janome.tokenizer import Tokenizer
import re
import codecs
import sqlite3
import geo

conn = sqlite3.connect('dataset/station.db')
cur = conn.cursor()

print "ツイートして\n＞",
input_line=sys.stdin.readline()
print "検索中・・・"

t = Tokenizer()
tokens = t.tokenize(input_line.decode('utf-8'))
lis=[]
i=0
dict={}

for token in tokens:
	lis.append(str(token))
	
for i in range(len(lis)):
	dict[i]=re.split(',|	',lis[i])
	if dict[i][3]=="地域":
		cur.execute("SELECT * FROM station WHERE station.name=\""+dict[i][7]+"\";")
		for name in cur.fetchall():
			geo.search(dict[i][7].decode('utf-8'));
			break;

