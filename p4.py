# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *

with open("in.txt", "r", encoding="utf-8") as f:
    file_list = f.readlines()
    o = open("out4.txt", "w", encoding="utf-8")
    max_len = 0
    for line in file_list:
        words = []
        input_string = line
        normalizer = Normalizer()
        s = normalizer.normalize(input_string)
        sentence = sent_tokenize(s)

        for sentence in sentence:
            w = word_tokenize(sentence)
            words += w
            length = len(words)

        sen_len = length
        if sen_len > max_len:
            max_len = sen_len
            sen_len=line
            a=sentence
    o.write('{0} : {1}'.format(a, max_len))

    o.write('\n')

o.close()
