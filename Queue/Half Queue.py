from queue import Queue
n = int(input())
l = list(map(int,input().split()))

q = Queue()
for i in l:
    q.put(i)

counter = l.count(0)

operations = 0
while counter<n:
    temp = q.get()
    if temp==1 or temp==-1:
        counter+=1
    q.put(int(temp/2))
    operations+=1

print(operations)
