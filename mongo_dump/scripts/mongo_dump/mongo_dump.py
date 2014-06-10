import os
import sys
import datetime
import logging
mongo_host_with_post = '182.71.101.206:27017' #'127.0.0.1:27017' 42's public ip
start_date = sys.argv[1]  #str(x.date())#'2014-02-18'
end_date = sys.argv[2] #str(y.date())#'2014-02-19'
out_to = '/volumes/data/mongo_dump/dump/'+start_date
logging.basicConfig(filename='dumping.log', level=logging.DEBUG)
logger = logging.getLogger('mongo_dumping')

def dump_it():
    try:
        q_str = '''mongodump -h '''+ mongo_host_with_post + ''' -d knowlus -c cdr_cdr -q "{\"start_time\":{\"\$gt\":'`date -d ''' + start_date + ''' +%F`',\"\$lte\":'`date -d ''' + end_date + ''' +%F`'}}" -o '''+ out_to
        os.system(q_str)
        q = 'tar cjf ' + out_to +'.tar.bz2 -C /volumes/data/mongo_dump/dump/ '+start_date +'/'
        os.system(q)
        q1 = 'rm -rf ' + out_to+' &'
        os.system(q1)
    except Exception as e:
        logger.exception('failed dumping')
    else:
        logger.info('done the dumping of the date %s'%start_date)
        with open('done.txt', 'a') as fp:
            fp.write(start_date + '\n')


dump_it()

