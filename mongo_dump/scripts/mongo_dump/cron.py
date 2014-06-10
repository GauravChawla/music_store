# run in cron as "python cron.py >> /mongo_dump/scripts/mongo_dump/dumping.log"

import os
import sys
import datetime
import logging
mongo_host_with_post = '182.71.101.206:27017'
x = datetime.datetime.now()
y = x+datetime.timedelta(-1)
start_date = str(y.date())#'2014-02-18'# sys.argv[1]
end_date = str(x.date())#'2014-02-19'  #sys.argv[2]
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
        print q_str
        print q
        print q1
    except Exception as e:
        logger.exception('failed dumping')
    else:
        logger.info('done the dumping of the date %s'%start_date)


dump_it()
