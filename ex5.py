n=int(input("enter the no of processes: "))
n1=[]
oh=int(input("enter the overhead: "))
for i in range(n):
    at=int(input(f'enter the arrival time for the {i+1}th process :'))
    bt=int(input(f'enter the burst time for the {i+1}th process :'))
    n1.append([i,at,bt])

# print(n1)
print("pid  at  bt")
print("------------")
for i in n1:
    print(f'P{i[0]+1}   {i[1]}  {i[2]}')

n2=sorted(n1,key=lambda x:x[1])
#print(n2)
n3=[]
r2=''
ct=[0 for i in range(len(n2))]
ct[0]=n2[0][1]+n2[0][2]+oh
for i in range(0,oh):
    r2+='/'
for i in range(n2[0][2]):
    r2+='_'
r2+='|'
n3.append(r2)

n2[0].append(ct[0])
wt=[]
tt=[]

for i in range(1,len(n2)):
    if ct[i-1]<n2[i][1]:
        r=""
        ct[i]=n2[i][1]+n2[i][2]+oh
        n2[i].append(ct[i])
        for j in range(0,oh):
            r+='/'
        for k in range(n2[i][2]):
            r+='*'
        r+='|'
        n3.append(r)
        # print(n3)

    else:
        r4=''
        ct[i]=ct[i-1]+n2[i][2]+oh
        n2[i].append(ct[i])
        for j in range(0,oh):
            r4+='/'
        for k in range(n2[i][2]):
            r4+='_'
        r4+='|'
        n3.append(r4)

for i in range(len(n2)):
    n2[i].append(n2[i][3]-n2[i][1])
    wt.append(n2[i][3]-n2[i][1])
    tt.append(n2[i][4]-n2[i][2])
    n2[i].append(n2[i][4]-n2[i][2])
count=0
count1=0
for i in range(len(wt)):
    count+=wt[i]
    count1+=tt[i]


print("pid  at  bt  ct  tt  wt")
print('-----------------------')
for i in n2:
    print(f'P{i[0]+1}   {i[1]}  {i[2]}  {i[3]}  {i[4]}  {i[5]}')

print("Chart")
r5=''
for i in n3:
    r5+=i
print(r5)



print("Average Waiting Time: ",count1/len(wt))
print("Average Turnaround Time: ",count/len(wt))
