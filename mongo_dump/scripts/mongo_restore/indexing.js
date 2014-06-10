var db_name = 'knowlus';
db = db.getMongo().getDB(db_name);
db.cdr_cdr.ensureIndex({'unique_id':1});
db.cdr_cdr.ensureIndex({'did_number':1});
db.cdr_cdr.ensureIndex({'end_time':1});
db.cdr_cdr.ensureIndex({'fs':1});
db.cdr_cdr.ensureIndex({'hangup_time':1});
db.cdr_cdr.ensureIndex({'fs_chan_info':1});
db.cdr_cdr.ensureIndex({'ivr_refnum':1});
db.cdr_cdr.ensureIndex({'order_time':1});
db.cdr_cdr.ensureIndex({'posting_time':1});
db.cdr_cdr.ensureIndex({'start_time':1});
db.cdr_cdr.ensureIndex({'id':1});
db.cdr_cdr.ensureIndex({'caller':1});
db.cdr_cdr.ensureIndex({'ref_uuid':1});
db.cdr_cdr.ensureIndex({'called':1});
db.cdr_cdr.ensureIndex({'pickup_time':1});
db.cdr_cdr.ensureIndex({'hangup_cause':1});
