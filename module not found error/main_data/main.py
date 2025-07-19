#thats all modules imported, except file4.py, becouse file4.py is the file where i want to send it
from test1.test2.test3.file3 import fil3
from test1.test2.file2 import fil2
from test1.file1 import fil1

#this should be send to file4.py v
def funk():
    fil1()
    fil2()
    fil3()

