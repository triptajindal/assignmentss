
import pymongo
client=pymongo.MongoClient()
database=client['student']
col=database['studentt']
for i in range(0,10):
    name=input("enter name")
    marks=int(input("enter marks"))
    st={'name: ':(name),'Marks: ':(marks)}
    col.insert_one(st)
f = {'Marks: ':{'$gt':80}}
dat = col.find(f)
for i in dat:
    print(i)
