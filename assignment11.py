#email validation or not

import re
n=input("enter email")
j=0
m=re.finditer('\w[_a-zA-Z0-9.]*(@)(gmail.com|yahooh.com)$',n)
for i in m:
    j=i.group()
if j==n:
    print("valid")
else:
    print("invalid")




#phone no valid or not
    
import re
n=input("enter no")
j=0
m=re.finditer('^[6-9][0-9]{9}',n)
for i in m:
    j=(i.group())
if j==n:
    print("valid")
else:
    print("invalid")
    
