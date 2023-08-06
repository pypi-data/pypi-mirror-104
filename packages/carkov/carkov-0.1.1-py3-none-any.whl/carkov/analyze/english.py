#
# carkov markov chain library
# © Copyright 2021 by Aldercone Studio <aldercone@gmail.com>
# This is free software, see the included LICENSE for terms and conditions.
#

import nltk

from .abstract import AbstractAnalyzer


class English(AbstractAnalyzer):
    def __init__(self, order, filters=None):
        if filters is None:
            filters = []
        super().__init__(order, filters)

    def segmentize_corpus(self, corpus):
        chunks = corpus.split('\n\n')
        ret = []
        for chunk in chunks:
            ret = ret + nltk.sent_tokenize(chunk)
        return ret

    def tokenize_segment(self, segment):
        return list(nltk.word_tokenize(segment))
