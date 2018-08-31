
#print current day using datetime module
import datetime
print(datetime.date.today().strftime('%A'))



#using webrowser module
import webbrowser
s=input("enter song")
webbrowser.open_new_tab('https://www.youtube.com/search?btnG=1&q=%s'%s)


#change to jpg

import os,glob,fnmatch
os.chdir(r"C:\Users\ThunderGirl\Desktop\assignment-12\pics")
for files in glob.glob("*.jpg"):
    print(files)


