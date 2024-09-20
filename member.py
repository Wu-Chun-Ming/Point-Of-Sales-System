
def checkmember(memberId):  #check whether is member or not
    file1=open('premium_membership.txt','r')
    file2=open('normal_membership.txt','r')
    file3=open('gold_membership.txt','r')
    lines1=file1.readlines()
    lines2=file2.readlines()
    lines3=file3.readlines()
    prLst=[]
    norLst=[]
    goldLst=[]
    for x in lines1:
        plst=x.strip('\n')
        prLst.append(plst)
    for x in lines2:
        nlst=x.strip('\n')
        norLst.append(nlst)
    for x in lines3:
        glst=x.strip('\n')
        goldLst.append(glst)
    
    memberLst=[]
    memberLst.append(prLst)
    memberLst.append(norLst)
    memberLst.append(goldLst)
    file1.close()
    file2.close()
    file3.close()

    memberstatusLst=['PREMIUM','NORMAL','GOLD','NON-MEMBER']    
    if memberId in memberLst[0]:    #determine member status and give respective discount
        print('-'*60)
        print('YOU ARE A PREMIUM MEMBER')
        memberstatus=memberstatusLst[0]
    elif memberId in memberLst[1]:
        print('-'*60)
        print('YOU ARE A NORMAL MEMBER')
        memberstatus=memebrstatusLst[1]
    elif memberId in memberLst[2]:
        print('-'*60)
        print('YOU ARE A GOLD MEMBER')
        memberstatus=memberstatusLst[2]
    elif memberId == 'N' or memberId not in memberLst:  
        print('-'*60)
        print('YOU ARE A NON-MEMBER')
        memberstatus=memberstatusLst[3]
    if memberstatus=='PREMIUM':
        dis = 0.80
    elif memberstatus=='GOLD':
        dis = 0.85
    elif memberstatus=='NORMAL':
        dis = 0.95
    else:
        dis = 1
    disRate=dis*100
    print("YOU GET",disRate,"% DISCOUNT")
    return dis, memberstatus

    
   

        

    
