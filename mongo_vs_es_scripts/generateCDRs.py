#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import random
import uuid
import json
cdr_field_list = ['posting_time', 'order_time', 'call_flow', 'fs_chan_info',
                  'ref_uuid', 'hangup_time', 'pickup_time', 'ivr_refnum',
                  'did_number', 'call_type', 'attempt_number', 'fs', 'data',
                  'events', 'hangup_cause', 'priority', 'end_time', 'start_time',
                  'called', 'caller', 'unique_id', 'id']
def get_fake_cdr():
    cdr = dict()
    cdr['posting_time'] = str(datetime.datetime.now())
    cdr['order_time'] = str(datetime.datetime.now())
    cdr['call_flow'] = "[(324, '2013-09-09 00:00:07.421090'), (324, '2013-09-09 00:00:07.431099', 0),(314, '2013-09-09 00:00:07.432024'), (314, '2013-09-09 00:00:07.472149', 0),(300, '2013-09-09 00:00:07.472315'), (302, '2013-09-09 00:00:16.160595'),(302, '2013-09-09 00:00:16.249476', 0), (300, '2013-09-09 00:00:16.249529', 0),(325, '2013-09-09 00:00:16.250241'), (325, '2013-09-09 00:00:16.260295', 0)]"
    cdr['events'] ='{"input2":"None","input3":"None","input0":"+911149426200","input1":"+911143790236","input6":"None","cdr_si":true,"input4":"None","input5":"None","input8":"None","input9":"None","voicemailurl":null,"POSTPROCESS":false,"recordingFile":[],"input7":"None","hangup_time":"2013-09-09 00:00:16.000000","conf_called_to":"+911143790236","answered":true,"status_from_bridge_api":{"Legb_Start_Time":"2013-09-09 00:00:07","Hangup_Cause":"NORMAL_CLEARING","HangupBy":"LegB","HangupTime":"2013-09-09 00:00:16","other_leg_cdr":[]"Channel_Num":"FreeTDM/6:3/01143790236","LegB_UUID":"c5e4a6c9-d48d-4868-b1b5-475932673c80","Bridge_Number":"+911143790236","JoinTime":"2013-09-09 00:00:08"},"session_uuid":"05eb3730-9b86-48cd-b495-15216a536fd2","confFile":"05eb3730-9b86-48cd-b495-15216a536fd2","hangup_cause":900,"member_info":{"Hangup_Cause":"NORMAL_CLEARING","HangupBy":"LegB","HangupTime":"2013-09-09 00:00:16","LegB_UUID":"c5e4a6c9-d48d-4868-b1b5-475932673c80","Bridge_Number":"+911143790236","JoinTime":"2013-09-09 00:00:08"},"action_id":"1116","direction":"_incoming","incall_answered":true,"start_time":"2013-09-09 00:00:07.391113","pickup_time":"2013-09-09 00:00:07.000000","LegB_join_time":"2013-09-09 00:00:08","session_knumber":"43790229","ivr_disp_number":"+911143790229","display_number":"+911143790229","reference_number":800056382,"INCOMING":true,"recordingFileUUID":[],"caller":"+911149426200","LegB_hangup_time":"2013-09-09 00:00:16","debug":false,"record_custom":[],"called":"+911143790229","unique_id":"05eb3730-9b86-48cd-b495-15216a536fd2"}'
    cdr['fs_chan_info'] = "FreeTDM/3:2/43790229"
    cdr['ref_uuid'] = str(uuid.uuid4())
    cdr['hangup_time'] = str(datetime.datetime.now())
    cdr['pickup_time'] = str(datetime.datetime.now())
    cdr['ivr_refnum'] = random.randint(81200345, 812000000)
    cdr['did_number'] = "+9111"+str(random.randint(43790229, 45000000))
    cdr['call_type'] = random.sample(['incoming','outgoing'],1)[0]
    cdr['attempt_number'] = random.sample(['1', '2', '3'],1)[0]
    cdr['fs'] = "fs7prod"
    cdr['data'] = 'null'
    cdr['hangup_cause'] = str(random.randint(400, 404))
    cdr['priority'] = str(random.randint(1, 6))
    cdr['end_time'] = str(datetime.datetime.now()+datetime.timedelta(minutes = 4))
    cdr['start_time'] = str(datetime.datetime.now())
    cdr['called'] = "+91"+str(random.randint(9654000000, 9654999999))
    cdr['caller'] = "+91"+str(random.randint(9654000000, 9654999999))
    cdr['unique_id'] = cdr['ref_uuid']
    cdr = json.dumps(cdr)
    return cdr
