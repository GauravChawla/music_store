#!/usr/bin/python
import time
import os
loop = 10
#x_str = "{time -o a.txt ./a.py; }"
for i in range(loop):
    str1 = 'echo "IN LOOP --> $i">>b.txt'
    ex_str = "{ time -p ./elastic_dumping.py; } 2>> b.txt"
    os.system(str1)
    os.system(ex_str)
