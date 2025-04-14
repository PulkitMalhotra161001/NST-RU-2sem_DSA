s=input()

open=0

for i in s:
    if i=='(':
        open+=1
    else:
        open-=1
    
    if open<0:
        break

if open==0:
    print("True")
else:
    print("False")


___________________________________________________
