
def receipt(itm,itmLst2,memberstatus,dis,orderNum,date,times,price):    #generate receipt     
    print ('-'*60)
    print ('SPORT PLANETT')
    print ('Date : ', date)
    print ('Order Number: %-10d'%(orderNum))
    print ('ItemName               Price         amount          total')
    print ('-'*60)
    for g in range(len(itmLst2)):
        print("%-20.20s   %-6.2f       %2d               %6.2f"%(itmLst2[g][1],float(itmLst2[g][2]),int(itmLst2[g][4]),(float(itmLst2[g][2])*(int(itmLst2[g][4])))))
    print ('\n')
    print ('-'*60)
    print ('MEMBER STATUS : %-10s'%memberstatus)
    print ('DISCOUNT RATE : %-3d'%(100-(dis*100)),'%')
    print ('NET AMOUT     : %-20.2f'%(price))
    print ('Thanks for ur purchase ^.^')
    print ('-'*60)
    print()

    file=open('receipt.txt', 'a')
    file.write('-'*60)
    file.write('\n')
    file.write('Order Number: %-10d\n'%(orderNum))
    file.write('-'*60)
    file.write('\n')
    file.write('SPORT PLANETT')
    file.write('\n')
    file.write(date)
    file.write('\n')
    file.write(times)
    file.write('\n')
    file.write('ItemName               Price         amount          total\n')
    file.write('-'*60)
    file.write('\n')
    for y in range(len(itmLst2)):
        file.write ("%-20.20s   %-6.2f       %2d               %6.2f"%(itmLst2[y][1],float(itmLst2[y][2]),int(itmLst2[y][4]),(float(itmLst2[y][2])*(int(itmLst2[y][4])))))
        file.write('\n')
    file.write ('\n')
    file.write ('MEMBER STATUS : %-10s'%memberstatus)
    file.write ('\n')
    file.write ('DISCOUNT RATE : %-3d'%(100-(dis*100)))
    file.write ('%')
    file.write ('\n')
    file.write ('Net amount    : %-20.2f'%(price))
    file.write ('\n')
    file.write ('THANK YOU FOR YOUR PURCHASE\n')
    file.write ('-'*60)
    file.write ('\n')
    file.write ('%-10d'%orderNum)
    file.write ('\n')
    file.write ('-'*60)
    file.write ('\n')
    file.close()

def saleRec(itmLst2,memberstatus,dis,price,orderNum,date,times):

    file=open('saleshistory.txt','a')
    file.write('%-10d'%orderNum)
    file.write('\n')                      
    file.write('-'*60)
    file.write('\n')
    file.write(date)
    file.write('\n')
    file.write(times)
    file.write('\n')
    file.write('-'*60)
    file.write('\n')
    for y in range(len(itmLst2)):
        file.write ("%-20.20s   %-6.2f       %2d               %6.2f"%(itmLst2[y][1],float(itmLst2[y][2]),int(itmLst2[y][4]),(float(itmLst2[y][2])*(int(itmLst2[y][4])))))
        file.write('\n')
    file.write ('\n')
    file.write ('MEMBER STATUS : %-10s'%memberstatus)
    file.write ('\n')
    file.write ('DISCOUNT RATE : %-3d'%(100-(dis*100)))
    file.write ('%')
    file.write ('\n')
    file.write ('Net amount    : %-20.2f'%(price))
    file.write ('\n')
    file.write ('-'*60)
    file.write ('\n')
    file.write('%-10d'%orderNum)
    file.write ('\n')
    file.write ('-'*60)
    file.write ('\n')
    file.close()

def orderNumG(orderNum):
    orderNum=orderNum+1
    return orderNum

def latON(orderNum):
    file=open('saleshistory.txt','r')
    lines=file.readlines()
    orderLst=[]
    for x in lines:
        olst=x.strip('\n')
        orderLst.append(olst)
    orderNum=int(orderLst[-2])
    file.close()
    return orderNum

