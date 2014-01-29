#!/usr/bin/python

from pymongo import *
from generateCDRs import get_fake_cdr
import json
import random
import uuid
DUMPING_COUNT = 10 ** 6  # 1 million
mongo_host = "10.60.20.43"
mongo_db = "dump_test_" + str(uuid.uuid4())


def connectToMongo():
    try:
        client = MongoClient(host=mongo_host)
        db = client[mongo_db]
        MCDR = db.cdr_cdr
        return MCDR
    except Exception as e:
        print "[db error]:", e


MCDR = connectToMongo()
for i in xrange(DUMPING_COUNT):
    cdr = json.loads(get_fake_cdr())
    try:
        res = MCDR.insert(cdr)
        print res
#        print uid, type(uid) , cdr, INDEX_NAME
    except Exception as e:
        print "[DUMPING ERROR]:", e
