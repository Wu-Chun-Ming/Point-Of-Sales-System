
def readFile():     
    fo=open('itmLST.txt','r')
    lines=fo.readlines()
    itmLst=[]
    for x in lines:
        tlst=x.strip('\n').split('|')
        itmLst.append(tlst)
    fo.close()
    return itmLst
#------------------------------------------------------------------
def showRecord(itmLst):   
    print("-"*70)
    print('ItemCode   ItemName               Price             Stocks')
    print("-"*70)
    for y in range(len(itmLst)):
         print("%8s   %-20.20s   %-6.2f    %10d"%(itmLst[y][0],itmLst[y][1],
                                                  float(itmLst[y][2]),
                                                  int(itmLst[y][3])))
#------------------------------------------------------------------
def DelFunc(itmLst):    #delete item
    loop=True
    while loop:
        itm=input('ENTER THE ITEM CODE <Q>uit >>')
        if itm in [x[0] for x in itmLst]:
            print('Valid item')
            confirm=input('confirm remove? <Y>es <N>o >>').upper()
            if confirm == 'Y':
                loop=False
            elif confirm == 'N':
                loop=True
            else:
                print("INVALID OPTION")
        elif itm.upper()=='Q':
            print ('Returning')
            loop=False
            itm=0
        elif len(itm) != 8:
            print('Invalid item code')
        else:
            print("Item not exist")
    return itm
#------------------------------------------------------------------
def addNewitem(itmLst):     #add new item
    loop=True
    step=1
    while loop:
        if step==1:
            itm=input("Enter item Code             <Q>uit >>").upper()
            if itm=="Q":
                step=99
            elif len(itm) !=8:
                print("Invalid item code added")
            elif itm in [y[0] for y in itmLst]:
                print('ITEM EXIST')
            else:  #need to check if item exists
                step+=1
        if step==2:
            itmDesc=input("Enter item Name             <Q>uit >>")
            if itmDesc=="Q":
                step=99
            else:
                step+=1
        if step==3:
            itmPr=input("Enter item price            <Q>uit >>")
            if itmPr=="Q":
                step=99
            try:
                float(itmPr)
                step+=1
            except:
                print("INVALID PRICE ENTERED")
        if step==4:
            itmStk=input("Enter item stock            <Q>uit >>")
            if itmStk=="Q":
                step=99
            elif not itmStk.isdigit():
                print('Invalid item Stock')
            else:  #need to check for floating point number
                step+=1
        if step==5:  #complete input
            tLst=[itm,itmDesc, itmPr, itmStk]
            loop=False
        if step==99:
            tLst=[]
            loop=False
    return tLst
#------------------------------------------------------------------
def updateItm(itmLst):  #update item detail
    loop=True
    step=1
    itmCodeLst=[]
    for k in range(len(itmLst)):
        itmCodeLst.append(itmLst[k][0])
    while loop:
        if step==1:
            itm=input("Enter item              <Q>uit >>").upper()
            if itm=="Q":
                step=99
            elif len(itm) !=8:
                print("Invalid item code added")
            elif itm in [y[0] for y in itmLst]:
                idx3=itmCodeLst.index(itm)
                step+=1
            else:
                print("Item code not exist")
        if step==2:
            print('UPDATE MENU: 1.NAME 2.PRICE 3.STOCK Q.QUIT')
            changeAT=input('WHICH PART TO CHANGE? >>')
            
            if changeAT == '1':
                itmDesc=input("Enter NEW item Name              <Q>uit >>")
                itmPr=itmLst[idx3][2]
                itmStk=itmLst[idx3][3]
                step+=1       
                    
            elif changeAT == '2':
                loop1=True
                while loop1:
                    itmPr=input("Enter item price        <Q>uit >>")
                    try:
                        float(itmPr)
                        itmDesc=itmLst[idx3][1]
                        itmStk=itmLst[idx3][3]
                        step+=1
                        loop1=False
                    except:
                        print("INVALID PRICE ENTERED")
            elif changeAT == '3':
                loop2=True
                while loop2:
                    itmStk=input("Enter item stock        <Q>uit >>")
                    try:
                        int(itmStk)
                        itmDesc=itmLst[idx3][1]
                        itmPr=itmLst[idx3][2]
                        step+=1
                        loop2=False
                    except:
                        print("INVALID STOCK ENTERED")
            elif changeAT.upper() == 'Q':
                step=1
            else:
                print('Invalid input')
        if step==3:
            tLst=[itm,itmDesc, itmPr, itmStk]
            loop=False
        if step==99:
            tLst=[]
            idx3=0
            loop=False
    return tLst,idx3
#------------------------------------------------------------------
def SaveRecord(itmLst):     #save record to file
    files=open('itmLST.txt','w')
    for y in range(len(itmLst)):
        lists="%s|%s|%0.2f|%2d\n"%(itmLst[y][0],itmLst[y][1],float(itmLst[y][2]),int(itmLst[y][3]))                                         
        files.write(lists)
    files.close()
#------------------------------------------------------------------
def CRUD(itmLst):   
    loop=True
    while loop:
        showRecord(itmLst) 
        print('-'*70)
        print('<A>DD ITEM | <D>elete ITEM | <U>PDATE ITEM | <S>AVE CHANGES |\n'
               '<Q>uit')
        print('-'*70)
        opt=input('ENTER your OPT >>').upper()
        if opt=='Q':
            print('EXITING SYSTEM...')
            loop=False
        elif opt == 'D':    
            itm=DelFunc(itmLst)
            if itm != 0:
                itmLst.pop([x[0] for x in itmLst].index(itm))
        elif opt == 'A':    
            tLst=addNewitem(itmLst)
            if tLst != []:
                itmLst.append(tLst)
        elif opt == 'S':    
            SaveRecord(itmLst)
            print('CHANGES SAVED...')
        elif opt == 'U':    
            tLst,idx3=updateItm(itmLst)
            if tLst != []:
                itmLst[idx3]=tLst
        else:  
            print("INVALID OPTION")


