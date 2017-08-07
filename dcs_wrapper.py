'''
Read DCS json in an iterated way

@author: avinashvarna
'''

from __future__ import print_function
import os
#import ijson.backends.yajl2_cffi as ijson
import ujson
import codecs
import datetime
from indic_transliteration import sanscript

def iter_sentences():
    start = datetime.datetime.now()
    print("Loading file started at", start)
    with codecs.open('dcs_sentences.json', "rb", "utf8") as f:
        doc_list = ujson.load(f)["docs"]
    
    end = datetime.datetime.now()
    print("Loading file finished at", start, "took", end-start)
    for doc in doc_list:
        if doc["_id"].startswith("sentence_"):
            yield doc
#         objects = ijson.items(f, 'docs.item')
#         sentences = (o for o in objects if o['_id'].startswith("sentence_"))
#         for s in sentences:
#             yield s

start = datetime.datetime.now()
print("Starting processign at", start)
with codecs.open('sent_roots.txt', "wb", "utf8") as out:
    for i,doc in enumerate(iter_sentences()):
        if "dcsAnalysisDecomposition" in doc:
            out.write(str(doc["dcsId"]) + ", ")
            out.write(doc["text"] + ", ")
            s = ""
            for decomp in doc["dcsAnalysisDecomposition"]:
                for group in decomp:
                    if "root" in group:
                        s += " " + group["root"]
        s_trans = sanscript.transliterate(s, sanscript.IAST, sanscript.SLP1)
        out.write(s_trans + "\n")
#         if i == 150: break
end = datetime.datetime.now()
print("Processing finished at", start, "took", end-start)