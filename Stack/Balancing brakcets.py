def solve(s):
    st = []
    for i in s:
        if i in "({[":
            st.append(i)
        elif len(st)==0:
            return "NO"
        elif i==')' and st[-1]=='(':
            st.pop()
        elif i==']' and st[-1]=='[':
            st.pop()
        elif i=='}' and st[-1]=='{':
            st.pop()
    
    if len(st)==0:
        return "YES"
    return "NO"
        


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
