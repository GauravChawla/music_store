import os
import sys
import datetime
import logging
import settings
mongo_host_with_port = settings.mongo_host_with_port
start_date = sys.argv[2]#'2014-02-24'
out_to = settings.out_to + start_date
out_from = settings.out_from + start_date
new_db = sys.argv[1]#'know' #add the new DB where you want to restore
logging.basicConfig(filename='/volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log', format='%(asctime)s %(message)s', datefmt='%d-%m-%Y %I:%M:%S', level = logging.DEBUG)
logger = logging.getLogger('mongo_logger')


def restore_it():
    """ Restores the data from mongo"""
    try:
        logger.info("in restore" + start_date)
        q = 'cp '+ out_to +'.tar.bz2 /volumes/data/mongo_dump/tmp/'
        print q
        os.system(q)
        q1 = 'tar xjf '+out_from+'.tar.bz2 -C /volumes/data/mongo_dump/tmp/'
        os.system(q1)
        q_Rstr = 'mongorestore -h '+ mongo_host_with_port  +' -c cdr_cdr -d '+ new_db +' ' + out_from+'/knowlus/cdr_cdr.bson'
        os.system(q_Rstr)
        q2 = 'rm -rf /volumes/data/mongo_dump/tmp/'+start_date+'* &'
        os.system(q2)
        logger.info("out restore for " + start_date)
    except:
        logger.exception("ERROR")
  
restore_it()
