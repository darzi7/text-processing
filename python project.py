# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *

with open("in.txt", "r", encoding="utf-8") as f:
    file_list = f.readlines()
    o = open("out.txt", "w", encoding="utf-8")

    for line in file_list:
        words = []
        input_string = line
        normalizer = Normalizer()
        s = normalizer.normalize(input_string)
        sentence = sent_tokenize(s)
        for sentence in sentence:
            w = word_tokenize(sentence)
            words += w
            o.write(str(len(words)))
            o.write('\n')
o.close()

