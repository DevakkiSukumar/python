fo = open ("foo.text","r+")

str = fo.read(20);
print("Read String is : ",str)

position = fo.tell()
print("Current file position : ", position)

position = fo.seek(0,0);
str = fo.read(10)
print("Again read string is : " ,str)

fo.close()

os.rename("foo.text","test1.text")
 
#newdir file
import os
os.mkdir("test")

#changing dir
import os
os.chdir("/

#location
import os
os.getcwd()

#remove 
import os
os.rmdir("/tmp/test")

