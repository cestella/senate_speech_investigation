# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers.english import stem_word
from sumy.utils import get_stop_words
import sys

def load_labels(topic_labels_filename):
    with open(topic_labels_filename) as f:
        contents = f.readlines()
    return [content.strip() for content in contents]

def summarize(filename, num_sentences):
    with open (filename, "r") as myfile:
        data=myfile.read()
    parser = PlaintextParser.from_string(data, Tokenizer('english')) 
    summarizer = LsaSummarizer(stem_word)
    summarizer.stop_words = get_stop_words("english")
    summary = ""
    for sentence in summarizer(parser.document, num_sentences):
        summary += sentence.__unicode__().encode('ascii', 'ignore').replace('\"', '').replace('\'', '').strip() + " " 
    return summary

if __name__ == "__main__":
    speeches = load_labels(sys.argv[1])
    num_sentences = int(sys.argv[2])
    for summary in [ summarize('senate_speeches/' + doc, num_sentences) for doc in speeches ]:
        print(summary)
