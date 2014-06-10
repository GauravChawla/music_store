from django.http import HttpResponse
import re
from datetime import datetime
import os
import json
from socket import socket, AF_INET, SOCK_STREAM


def mongo_restore(request):
    try:
        date_from = request.REQUEST.get('date_from', None)
        date_to = request.REQUEST.get('date_to', None)
        email_id = request.REQUEST.get('email_id', None)
#        return HttpResponse(json.dumps(date_from, date_to, email_id))
    except Exception as e:
        return HttpResponse('Error: Please enter date_from, date_to and email_id'+str(e))
    if date_from is u'' or date_to is u'' or email_id is u'':
        return HttpResponse('Error: Please enter date_from, date_to and email_id')
    if date_from is None or date_to is None or email_id is None:
        return HttpResponse('Error: Please enter date_from, date_to and email_id')
    if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]*gmail.com$", email_id) == None:    #valid company id
        return HttpResponse('Error: Please enter valid gmail email id : '+email_id)
    if date_from:
        df = valid_date(date_from)
        if not df:
            return HttpResponse("Error: invalid date_from (%s)"%date_from)
    if date_to:
        dt = valid_date(date_to)
        if not dt:
            return HttpResponse("Error: invalid date_to (%s)"%date_to)
    if df > datetime.now():
        return HttpResponse("Error: invalid date_from (%s)"%df)
    if dt > datetime.now():
        return HttpResponse("Error: invalid date_to (%s)"%dt)
    if date_from and date_to:
        if df >= dt:
            return HttpResponse("Error: date_from (%s) is later than date_to (%s)"%(date_from, date_to))
    d = {'start_date':date_from, 'end_date':date_to, 'email_id':email_id}
    try:
        q = "python /volumes/data/mongo_dump/scripts/mongo_restore/main.py "+date_from+' '+date_to+' '+email_id+' >> /volumes/data/mongo_dump/scripts/mongo_restore/mongo_restore.log &'
        os.system(q)
    except Exception as e:
        return HttpResponse(json.dumps("There is problem in server, please contact the concerned person \n"+str(e)))
    return HttpResponse(json.dumps("After restoring the data, conformation mail will be send to : " + email_id +" Please check your spam also"))


def valid_date(d):
    d = str(d)
    d = d.strip()
    try:
        x = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        return x
    except ValueError:
        pass
    try:
        x = datetime.strptime(d, '%Y-%m-%d %H:%M')
        return x
    except ValueError:
        pass
    try:
        x = datetime.strptime(d, '%Y-%m-%d %H')
        return x
    except ValueError:
        pass
    try:
        x = datetime.strptime(d, '%Y-%m-%d')
        return x
    except ValueError:
        pass
    return None
