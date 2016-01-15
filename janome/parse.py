#!/usr/bin/python
# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer

t = Tokenizer()
for token in t.tokenize(u"すもももももももものうち"):
    print(token.surface + " " + token.part_of_speech)