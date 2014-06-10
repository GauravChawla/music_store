from datetime import datetime, timedelta
import sys
import smtplib
import os
import logging
import settings
from pymongo import MongoClient
mongo_host = settings.mongo_host_with_port
s_d = sys.argv[1]
e_d = sys.argv[2]
email_id = sys.argv[3]
start_date = datetime.strptime(s_d, '%Y-%m-%d')
end_date = datetime.strptime(e_d, '%Y-%m-%d')
logging.basicConfig(filename='/volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log', format='%(asctime)s %(message)s', datefmt='%m-%d-%Y %I:%M:%S %p', level = logging.DEBUG)
logger = logging.getLogger('mongo_logger')
#start_date = date(2014,02,18)
#end_date = date(2014,02,19) # range yield one day less the the end date
#print start_date, "to ", end_date
dbs = ['db1', 'db2', 'db3', 'db4', 'db5']


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
            print date
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
        sender = 'mongo@gmail.com'
        recpt = [email_id] #add
	logger.info("vai recpt: "+str(recpt))
        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(sender, 'pwd')
        if text_e is None:
            text ="Your requested data is there in db %s for dates between %s and %s . please dont reply on this email-id"% (db_name, start_date, end_date)
        else:
            text = "The data you requested is exceeding the limit of 5 DBs.. please contact the ADMIN"
        subject = "Mongo Restoration"
        headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" %(sender, recpt, subject)
        message = headers + text
        mail_server.sendmail(sender, recpt, message)
        mail_server.close()
        logger.info("Successfully sent email to "+email_id)
    except Exception as e:
        logger.exception("Error: unable to send email" + str(e))



db_name = getDB()
logger.info("DB selected is "+ str(db_name) +"(IF none means all dbs are created recently in interval of 10 days)")
if db_name is not None:
    days = (start_date + timedelta(days=d) for d in xrange((end_date - start_date).days ))
    for day in days:
        day = str(day).split(" ")[0]
        q = 'python /volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.py '+db_name+' '+day+' >> /volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log'
        os.system(q)
if db_name is None:
    send_mail('error')
else:
    send_mail()

