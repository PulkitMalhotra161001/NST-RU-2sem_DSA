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


def solve(s):
    st = []
    for i in s:
        if i=='(':
            st.append("(")
        else:
            if len(st)==0:
                return "False"
            st.pop()
    
    if len(st)==0:
        return "True"
    return "False"

s=input()
print(solve(s))
