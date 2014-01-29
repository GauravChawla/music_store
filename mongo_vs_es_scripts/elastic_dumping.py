#!/usr/bin/python

from elasticsearch import Elasticsearch
from generateCDRs import get_fake_cdr
import json
import random
import uuid
DUMPING_COUNT = 10 ** 6  # 1 million
INDEX_NAME = "dump_test_" + str(uuid.uuid4())


def getElasticSearch():
    try:
        es = Elasticsearch()
        return es
    except Exception as e:
        print "[connection error]:", e


es = getElasticSearch()
for i in xrange(DUMPING_COUNT):
    cdr = json.loads(get_fake_cdr())
    uid = str(uuid.uuid4())
    try:
#        print uid, type(uid) , cdr, INDEX_NAME
        res = es.index(index=INDEX_NAME, doc_type='cdr', id=uid, body=cdr)
        print res
    except Exception as e:
        print "[DUMPING ERROR]:", e
