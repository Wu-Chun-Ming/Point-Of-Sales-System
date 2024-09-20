
from datetime import datetime
import time,itemMaster as prog1,salemodule as prog2,receipt as prog3,member as prog4,check as prog5

now=str(datetime.now())
date = now[:10]
times = now[11:16]

dis=1 
lowStLst=[] 

memberstatus='NON-MEMBER' 
itmLst=prog1.readFile() 
orderNum=0
orderNum=prog3.latON(orderNum)  

loop=True
while loop:
    print ('-'*70)
    print('SYSTEM OPTION')
    print ('-'*70)
    print ('ITEM MASTER (FOR ADMIN)                  <1>')
    print ('SALE MODULE                              <2>')
    print ('Member Login (DEFAULT NON-MEMBER)        <3>')
    print ('INVENTORY CHECK                          <4>')
    print ('EXIT SYSTEM                              <Q>')
    print ('-'*70)

    opt=input('Enter option >>')
    if opt == '1' :
        prog1.CRUD(itmLst)  #itemMaster.py
    elif opt == '2':
        prog2.sale(itmLst,memberstatus,dis,orderNum,date,times) #salemodule.py
        print('-'*70)
    elif opt == '3':
        memberId=input('ENTER YOUR MEMBER ID (<N>ON-MEMBER) >>')
        dis,memberstatus=prog4.checkmember(memberId)    #member
    elif opt == '4':
        prog5.invenCheck(lowStLst,itmLst,date)  #check.py
        print('-'*70)
    elif opt.upper()=='Q':
        end=99
        while end!='1':
            end=input('EXIT(1)/CONTINUE(2) >>')
            if end == '1':
                print('EXITING SYSTEM....')
                loop=False
            elif end == '2':
                print('-'*70)
                end='1'
            else:
                print('INVALID OPTION')
                print('-'*70)
    else:
        print ('INVALID OPTION')
