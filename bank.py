'''
def interface():

        while True:
            print("""
            1: total amount
            2: deposit amount
            3: cash withdrawal
            4: lotto
            Q: Quit
            """)
            ui=input()
'''

r=open('./bank.txt','r')

l=r.readlines()[0].split(',')

sum=0
for i in l:
    sum+=int(i)
    print(i)
print(l)

#print(",'",str(d),"'")
trn=input('total/deposit/withdrawal')
if trn=='total':
    print(sum)
elif trn=='deposit':

    d=int(input('deposit meblegi daxil edin'))
    sum += d
    cnt=","+str(d)
    with open('./bank.txt', 'a') as w:
        w.write(cnt)
elif trn=='withdrawal':

    wd=-(int(input('withdraw meblegi daxil edin')))
    sum+=wd
    cnt=","+str(wd)
    with open('./bank.txt', 'a') as w:
        w.write(cnt)
else:
    print('duzgun variant sec')


