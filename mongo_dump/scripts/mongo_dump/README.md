cron.py : script that is added to crontab ,which takes the dump on daily basis
dumping.log : logfile for all scripts here , even for cron
mongo_dump.py : this is script thats takes the input as start_date and end_date and is can be easily run by outer.py by giving asked date in outer.py
outer.py: this scripts takes input as start date and end_date and run the mongo_dumo.py script between the dates.
