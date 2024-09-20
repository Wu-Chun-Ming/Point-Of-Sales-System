def invenCheck(lowStLst,itmLst,date):   #check inventory if low stock
    lowStLst=[]
    for y in range(len(itmLst)):
        if int(itmLst[y][3]) <= 50:
            lowStLst.append(itmLst[y])
    print('ITEM WITH LOW STOCK')
    print('-'*20)
    print('NAME                            STOCK LEFT')
    print('-'*60)
    for x in range(len(lowStLst)):
        print("%-20s            %-10d"%(lowStLst[x][1],int(lowStLst[x][3])))
    print('-'*60)
    print('KINDLY UPDATE IN ITEM MASTER SYSTEM AFTER RESTOCK')
    print('-'*60)
    choice=input('SAVE IT AS TEXT FILE? (Y/N) >> ').upper()
    loop=True
    while loop:
        if choice == 'Y':
            file=open('LowStockList.txt','w')
            file.write(date)
            file.write('\n')
            file.write('ITEM WITH LOW STOCK\n')
            file.write('-'*19)
            file.write('\n')
            file.write('NAME                            STOCK LEFT\n')   
            file.write('-'*60)
            file.write('\n')
            for x in range(len(lowStLst)):
                file.write("%-20s            %-10d"%(lowStLst[x][1],int(lowStLst[x][3])))
                file.write('\n')
            file.write('\n')
            file.write('KINDLY UPDATE IN ITEM MASTER SYSTEM AFTER RESTOCK\n')
            file.close()
            loop=False
            print('SAVED...')
        elif choice == 'N':
            print('-'*60)
            loop=False
        else:
            print('INVALID INPUT')
            print('-'*60)
            choice=input('SAVE IT AS TEXT FILE? (Y/N) >> ').upper()
            

    
    

