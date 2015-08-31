# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hazm import *



with open("in.txt", "r", encoding="utf-8") as f:
    file_list = f.readlines()
    o = open("out5.txt", "w", encoding="utf-8")

    for line in file_list:
        words = []
        input_string = line
        normalizer = Normalizer()
        s = normalizer.normalize(input_string)
        sentence = sent_tokenize(s)
        for sentence in sentence:
            new_words = word_tokenize(sentence)

            stemmed_new_words = []
            for word in new_words:
                stemmer= Stemmer()
                a=stemmer.stem(word)
                stemmed_new_words.append(a)

            words += stemmed_new_words

            o.write(str(stemmed_new_words))
            o.write('\n')
o.close()



# stop_word
# stem
# lemmatize
# subject