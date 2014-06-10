// This script removes the all the dbs mentioned in dbs...

var dbs = ['db1', 'db2', 'db3', 'db4', 'db5']
for(var i in dbs){
   db = db.getMongo().getDB( dbs[i] );
   print( "dropping db " + db.getName());
   db.dropDatabase();
}

