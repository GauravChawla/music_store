from datetime import datetime, timedelta
import sys
import smtplib
import os
import logging
from pymongo import MongoClient
import threading
import settings
import time
mongo_host = settings.mongo_host_with_port
s_d = sys.argv[1]
e_d = sys.argv[2]
email_id = sys.argv[3]
start_date = datetime.strptime(s_d, '%Y-%m-%d')
end_date = datetime.strptime(e_d, '%Y-%m-%d')
logging.basicConfig(filename='/volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log', format='%(asctime)s %(message)s', datefmt='%d-%m-%Y %I:%M:%S', level = logging.DEBUG)
logger = logging.getLogger('mongo_logger')
#start_date = date(2014,02,18
#end_date = date(2014,02,19) # range yield one day less the the end date
#print start_date, "to ", end_date
dbs = ['db1', 'db2', 'db3', 'db4', 'db5']

class M_thread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print "going for run() with thread" ,self.name
        dump_it(self.name)

def getDB():
    to_use_db = None
    client = MongoClient(host=mongo_host)
    for i in dbs:
        db = client[i]
        data = db.metadata.find_one()
        if data['is_active'] == 0:
            to_use_db = i
            data['is_active'] = 1
            data['c_date'] = str(datetime.now())
            db.metadata.save(data)
            break
        else:
            date = data['c_date']
            try:
                meta_date = datetime.strptime(date, '%Y-%m-%d')
            except:
                meta_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
            x = str(datetime.now() - meta_date).split(" ")
            if len(x) == 1:
                continue
            if int(x[0]) > 10:
                to_use_db = i
                data['c_date'] = str(datetime.now())
                db.metadata.save(data)
                db.cdr_cdr.remove()
                break
            else:
                continue
    return to_use_db



def send_mail(text_e=None):
    """Send mail with given parameters through gmail"""
    try:
        sender = 'mongo.@gmail.com'
        recpt = [email_id] #add .com'
        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(sender, 'pwd')
        if text_e:
            text = "The data you requested is exceeding the limit of 5 DBs.. please contact the ADMIN"
        else:
            text ="Your requested data is there in db %s for dates between %s and %s at ip_port %s. please dont reply on this email-id"% (db_name, start_date, end_date, mongo_host)
        subject = "Mongo Restoration"
        headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" %(sender, recpt, subject)
        message = headers + text
        mail_server.sendmail(sender, recpt, message)
        mail_server.close()
        logger.info("Successfully sent email to "+email_id)
    except:
        logger.exception("Error: unable to send email")

def dump_it(day):
    logger.info("restoring the data for date: "+day)
    q = 'python /volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.py '+db_name+' '+day+' >> /volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log'
    os.system(q)
    logger.info("restoring done for date: "+day)



def main(db_name):
    count = 0
    if db_name is not None:
        days = (start_date + timedelta(days=d) for d in xrange((end_date - start_date).days ))
        for day in days:
            day = str(day).split(" ")[0]
            m = M_thread(str(day))
            count += 1
            if count % 4 is not 0:
                 m.start()
            else:
                 try:
                     time.sleep(10*60)
                     m.start()
                 except:
                     logging.excetion("ERROR:")


db_name = getDB()
logger.info("DB selected is "+str(db_name)+" (IF none means all dbs are created recently in interval of 10 days)")
if db_name is None:
    send_mail(text_e='error')
else:
    main(db_name)
    while True:
        print "active thread count is ", threading.active_count()
        if int(threading.active_count()) == 1:
            break
        else:
            print "sleeping for 4 mins..."
            time.sleep(4*60)
    print "sending the mail...."
    send_mail()
