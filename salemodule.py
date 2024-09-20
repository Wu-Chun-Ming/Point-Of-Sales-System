
def readFile(): 
    fo=open('itmLST.txt','r')
    lines=fo.readlines()
    itmLst=[]
    for x in lines:
        tlst=x.strip('\n').split('|')
        itmLst.append(tlst)
    fo.close()
    return itmLst
    
def showRecord():   #0123
    itmLst=readFile()
    print('ItemCode   ItemName               Price             Stocks')
    print("-"*60)
    for y in range(len(itmLst)):
        print("%8s   %-20.20s   %-6.2f    %10d"%(itmLst[y][0],itmLst[y][1],float(itmLst[y][2]),int(itmLst[y][3])))

def showRecord1(itmLst2):   #0124
    for g in range(len(itmLst2)):
        print("%8s   %-20.20s   %-6.2f       %10d"%(itmLst2[g][0],itmLst2[g][1],float(itmLst2[g][2]),int(itmLst2[g][4])))

def SaveRecord(itmLst): #save record to file
    files=open('itmLST.txt','w')
    for y in range(len(itmLst)):
        lists="%s|%s|%0.2f|%-2d\n"%(itmLst[y][0],itmLst[y][1],float(itmLst[y][2]),int(itmLst[y][3]))                                                        
        files.write(lists)
    files.close()

def sale(itmLst,memberstatus,dis,orderNum,date,times):
    import receipt as prog
    itmLst2=[]
    itm=[]
    loop=True
    while loop:
        print ('Sales Transaction Menu -->     Date : %10s  Time : %5s'%(date,times))
        print ('-'*60)
        showRecord()
        print('-'*60)
        price=float('%0.2f'%sum(itm)) * dis
        price=str(price)
        rLst=[0.01,0.02]       
        roundp=int(price[-1:])
        if roundp in [1,2,6,7]: #round up or down 
            if roundp in [1,6]:
                price=float(price)-rLst[0]
            elif roundp in [2,7]:
                price = float(price)-rLst[1]
        elif roundp in [3,4,9,8]:
            if roundp in [3,8]:
                price = float(price)+rLst[1]
            elif roundp in [4,9]:
                price = float(price)+rLst[0]
        else:
            price=float(price)        
        itmCodeLst=[]   
        for k in range(len(itmLst)):
            itmCodeLst.append(itmLst[k][0])
        itmCode=input('ENTER THE ITEM CODE <P>ayment <Q>uit >>').upper()
        if itmCode not in ['P','Q',] and len(itmCode) != 8:
            print('Invalid item code')
        elif itmCode not in ['P','Q'] and itmCode not in itmCodeLst:
            print('Item unavailable')
        elif itmCode == 'P':
            if itmLst2 ==[]:
                print ('-'*60)
                print('NO ITEM IN CART')
                print ('-'*60)
            else:
                print ('-'*60)
                showRecord1(itmLst2)
                print ()
                print ('MEMBER STATUS :', memberstatus)
                print ('DISCOUNT RATE : %-3d'%(100-(dis*100)),'%')
                print ('Total price   : %-10.2f'%(price))
                print ('-'*60)
                cpay=(input('Confirm Payment? (Y/N)>>')).upper()
                loop1=True
                while loop1:
                    if cpay == 'Y':
                        orderNum=prog.orderNumG(orderNum)
                        prog.receipt(itm,itmLst2,memberstatus,dis,orderNum,date,times,price)
                        SaveRecord(itmLst)
                        prog.saleRec(itmLst2,memberstatus,dis,price,orderNum,date,times)
                        itmLst2=[]
                        itm=[]
                        itmLst=readFile()
                        loop1=False
                    elif cpay == 'N':
                        itmLst2=[]
                        itm=[]
                        itmLst=readFile()
                        loop1=False
                    else:
                        print('Invalid input')
                        cpay=input('Comfirm Payment? (Y/N)>>').upper()
        elif itmCode == 'Q':
            loop=False
            itmLst2=[]
            itm=[]
            itmLst=readFile()
        else:
            idx=itmCodeLst.index(itmCode)
            num=input('ENTER THE AMOUNT FOR THIS ITEM <Q>uit >>')
            loop1=True
            while loop1:
                if num.isdigit() and num != '0':
                    stock=int(itmLst[idx][3]) - int(num)
                    if stock >= 0 :
                        itmLst2.append(itmLst[idx])
                        idx2=itmLst2.index(itmLst[idx])
                        itmLst2[idx2].append(int(num))
                        itm.append((float(itmLst[idx][2]))*itmLst2[idx2][4])
                        itmLst[idx][3]=stock
                        print()
                        print('-'*60)
                        print('CART|')
                        print('-'*60)
                        showRecord1(itmLst2)
                        print()
                        loop1=False
                    else:
                        print('Sorry, insufficient stock T^T')
                        print()
                        itm=[]
                        itmLst=readFile()
                        loop1=False
                elif num.upper()=='Q':
                    itmLst2=[]
                    itm=[]
                    loop1=False
                    itmLst=readFile()
                else:
                    print('Invalid amount input')
                    num=input('ENTER THE AMOUNT FOR THIS ITEM        >> ')
        
                
            
            


    


    
