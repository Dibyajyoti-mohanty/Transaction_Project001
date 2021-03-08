tr = [(('1210','120001','27/02/2021'),('apple',3),('grapes',4)),
      (('1211','120002','27/02/2021'),('pears',6),('mango',8),('orange',6)),
      (('1212','120003','27/02/2021'),('pears',2),('apple',3),('orange',4),('cherry',5),('mango',6),('apple',7)),
      (('1213','120004','28/02/2021'),('orange',9),('pears',8),('pineapple',5)),
      (('1214','120005','28/02/2021'),('grapes',3),('apple',7)),
      (('1215','120006','02/03/2021'),('mango',12),('orange',13),('guava',8),('Strawberry',10),('cherry',7)),
      (('1211','120007','03/03/2021'),('dates',15),('banana',10),('orange',10)),
      (('1214','120008','04/03/2021'),('dates',13),('banana',10),('Blackberry',2)),
      (('1215','120009','05/03/2021'),('dates',12),('apple',10),('mango',10),('cherry',8)),
      (('1216','120010','05/03/2021'),('apple',6),('dates',8),('jelly',5),('jackfruit',50)),
     (('1217','120011','05/03/2021'),('mango',6),('apple',8)),
     (('1218','120012','06/03/2021'),('Blackberry',8),('Strawberry',6),('jackfruit',60),('mango',15),('apple',10),('WaterMelon',95))]




cu = [('1210','Rajesh'),('1211','Rakesh'),('1212','Sahil'),
      ('1213','Jack'),('1214','Steve'),('1215','Rohan',),
      ('1216','Millan',),('1217','mikul'),('1218','smile')]


item_detail = [('1001','apple',60),('1002','orange',40),('1003','pears',30),
               ('1004','mango',50),('1005','grapes',45),('1006','guava',40),
             ('1007','pineapple',60),('1008','dates',100),('1009','banana',10),
               ('1010','Strawberry',150),('1011','Blackberry',110),
             ('1012','cherry',90),('1013','jelly',20),('1014','jackfruit',40)]





tr_cu_un = []

tr_item_un = []

tr_un_bill = []

tr_un_date = []

def cu_name_id(c_id):
    c_id = c_id
    for i in range(len(cu)):
        cu_id = cu[i][0]
        cu_name = cu[i][1]
        if cu_id == c_id:
            return cu_name
        elif cu_name == c_id:
            return cu_id 

def item_name_code(i_code):
    i_code = i_code
    for i in range(len(item_detail)):
        tr_i_code = item_detail[i][0]
        tr_i_name = item_detail[i][1]
        if tr_i_code == i_code:
            return tr_i_name
        elif tr_i_name == i_code:
            return tr_i_code


for i in range(len(tr)):
    for j in range(1,len(tr[i])):
        cu_un_id = tr[i][0][0]
        item_un_name = tr[i][j][0]
        tr_bill = tr[i][0][1]
        tr_date = tr[i][0][2]

        if cu_un_id not in tr_cu_un:
            tr_cu_un.append(cu_un_id)
            

        if item_un_name not in tr_item_un:
            tr_item_un.append(item_un_name)


        if tr_date not in tr_un_date:
            tr_un_date.append(tr_date)
        
    tr_un_bill.append(tr_bill)

#******************************************************************************************************************************************************


def main_tr_db():

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    a_sum = 0
    x = 0

    print("{}     {}     {}  {:<8}  {:<10} {:>3} {:>3} {:>4} {:>5} ".format('bill','date','tr_cu_id','tr_cu_name','item','item_rate','quantity','amount','a_sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity
            a_sum = a_sum + amount
            x = x+1




            
            print("{} {}  {}       {:<8}  {:<10} {:>3}        {:>3}     {:>4}   {:>5} ".format(bill,date,tr_cu_id,tr_cu_name,item,item_rate,quantity,amount,a_sum))
    print()
    print("Total ::                                                             {:>5}".format(a_sum))

#******************************************************************************************************************************************************

def bill_wise_detail(c_bill):
    c_bill = c_bill

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    x = 0
    a_sum = 0


    print("{}      {}     {:<8}  {}    {:<10} {} {:>4} {:>3}  {:>6}  {:>6}".format('Bill','Date','Cu_Name','Cu_ID','Item','Item_code','Item_rate','Quantity','Amount','a_sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            
            amount = item_rate * quantity
            
            if bill == c_bill:
                a_sum = a_sum + amount
                t_name = tr_cu_name
                t_id = tr_cu_id


                print("{}  {}  {:<8} {}    {:<10}    {}     {:>4}    {:>3}      {:>6}   {:>6}".format(bill,date,t_name,t_id,item,item_code,item_rate,quantity,amount,a_sum))
    print()
    print("Total ::                                                                     {:>6}".format(a_sum))
    print()

#******************************************************************************************************************************************************


def bill_wise_detail_all():
    for i in range(len(tr_un_bill)):
        bill_wise_detail(tr_un_bill[i])
        print()
        print()

#******************************************************************************************************************************************************

def bill_wise_total(c_bill):

    c_bill = c_bill
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    a_sum = 0
    c_sum = 0
    x = 0

    print(" {:<8}   {}     {}   {}   {:>6} {:>6}".format('Bill','Date','Cu_ID','Cu_Name','Amount_Sum','C_Sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity

            if bill == c_bill:
                a_sum = a_sum + amount
                t_name = tr_cu_name
                t_id = tr_cu_id
                t_bill = bill 
                t_date = date
                t_name = tr_cu_name
    c_sum = c_sum + a_sum
    print("{:<8} {}  {}    {:<8}  {:>6}    {:>6}".format(t_bill,t_date,t_id,t_name,a_sum,c_sum))
    
#******************************************************************************************************************************************************

def bill_wise_summary():
    
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    x = 0

    print(" {:<8}   {}     {}   {}   {:>6} {:>6}".format('Bill','Date','Cu_ID','Cu_Name','Amount_Sum','C_Sum'))
    print()

    for u in range(len(tr_un_bill)):
        c_bill = tr_un_bill[u]
        a_sum = 0

        for i in range(len(tr)):
            for j in range(1,len(tr[i])):
                item = tr[i][j][0]
                quantity = tr[i][j][1]
                tr_cu_id = tr[i][0][0]
                bill = tr[i][0][1]
                date = tr[i][0][2]


                for k in range(len(cu)):
                    if tr_cu_id == cu[k][0]:
                        tr_cu_name = cu[k][1]
                for l in range(len(item_detail)):
                    if item == item_detail[l][1]:
                        item_code = item_detail[l][0]
                        item_rate = item_detail[l][2]
                amount = item_rate * quantity

                if bill == c_bill:
                    a_sum = a_sum + amount
                    t_name = tr_cu_name
                    t_id = tr_cu_id
                    t_bill = bill 
                    t_date = date
                    t_name = tr_cu_name
        c_sum = c_sum + a_sum
        print("{:<8} {}  {}    {:<8}  {:>6}    {:>6}".format(t_bill,t_date,t_id,t_name,a_sum,c_sum))
    print()
    print("Total ::                               {:>6}".format(c_sum))

#******************************************************************************************************************************************************

def cust_wise_detail(cust_id):

    cust_id = cust_id
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    a_sum = 0
    c_sum = 0
    x = 0

    print("{:<8}   {:<5}    {:<8}    {:<10} {:<10} {:>6}   {:>4}    {:>3}     {:>6}  {:>6}".format('Cu_Name','Cu_ID','Date','Bill','Item','Item_code','Item_rate','Quantity','Amount','a_sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity
        

            if tr_cu_id == cust_id:
                a_sum = a_sum + amount
                t_name = tr_cu_name
                t_id = tr_cu_id

                print("{:<8}   {:<5}   {:<8}  {:<10} {:<10} {:>6}        {:>4}          {:>3}       {:>6}   {:>6}".format(t_name,t_id,date,bill,item,item_code,item_rate,quantity,amount,a_sum))
    print()
    print("Total ::                                                                                   {:>6}".format(a_sum))
    print()

#******************************************************************************************************************************************************                

def cust_wise_detail_all():
    for i in range(len(tr_cu_un)):
        cust_wise_detail(tr_cu_un[i])
        print()
        print()

#******************************************************************************************************************************************************

def cust_wise_summary():

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    x = 0

    print("{:<8}     {:<6}  {:>6}   {:>6}".format('Cu_Name','Cu_ID','Amount_Sum','C_Sum'))
    print()

    for u in range(len(tr_cu_un)):
        cust_id = tr_cu_un[u]
        a_sum = 0

        for i in range(len(tr)):
            for j in range(1,len(tr[i])):
                item = tr[i][j][0]
                quantity = tr[i][j][1]
                tr_cu_id = tr[i][0][0]
                bill = tr[i][0][1]
                date = tr[i][0][2]


                for k in range(len(cu)):
                    if tr_cu_id == cu[k][0]:
                        tr_cu_name = cu[k][1]
                for l in range(len(item_detail)):
                    if item == item_detail[l][1]:
                        item_code = item_detail[l][0]
                        item_rate = item_detail[l][2]
                amount = item_rate * quantity

                if tr_cu_id == cust_id:
                    a_sum = a_sum + amount
                    t_name = tr_cu_name
                    t_id = tr_cu_id
                    t_bill = bill 
                    t_date = date
                    t_name = tr_cu_name
        c_sum = c_sum + a_sum
        print("{:<8}     {:<6}  {:>6}      {:>6}".format(t_name,t_id,a_sum,c_sum))
    print()
    print("Total ::                         {:>6}".format(c_sum))

#******************************************************************************************************************************************************

def date_wise_summary():
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    x = 0


    print("  {:<10}    {:>6}   {:>6}".format('Date','Amount','a_sum'))
    print()

    for u in range(len(tr_un_date)):
        cu_date = tr_un_date[u]
        a_sum = 0

        for i in range(len(tr)):
            for j in range(1,len(tr[i])):
                item = tr[i][j][0]
                quantity = tr[i][j][1]
                tr_cu_id = tr[i][0][0]
                bill = tr[i][0][1]
                date = tr[i][0][2]


                for k in range(len(cu)):
                    if tr_cu_id == cu[k][0]:
                        tr_cu_name = cu[k][1]
                for l in range(len(item_detail)):
                    if item == item_detail[l][1]:
                        item_code = item_detail[l][0]
                        item_rate = item_detail[l][2]
                amount = item_rate * quantity

                if date == cu_date:
                    a_sum = a_sum + amount
                    t_name = tr_cu_name
                    t_id = tr_cu_id
                    t_date = date
                    t_amount = amount
        c_sum = c_sum + a_sum
        print("{:<10}    {:>6}    {:>6}".format(t_date,a_sum,c_sum))
    print()
    print("Total ::      {:>6}".format(c_sum))
                    
#******************************************************************************************************************************************************

def date_wise_amount(i_date):

    i_date = i_date
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    a_sum = 0
    x = 0


    print("  {}         {:>6}".format('Date','Amount','a_sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity

            if date == i_date:
                a_sum = a_sum + amount
                t_name = tr_cu_name
                t_id = tr_cu_id
                t_date = date
                t_amount = amount

                
    c_sum = c_sum + a_sum
    print("{}    {:>6}".format(t_date,c_sum))
    print()

#***************************************************************************************************************************************************** 
   

def date_wise_detail_all():
    for i in range(len(tr_un_date)):
        date_wise_detail(tr_un_date[i])
        print()
        print()

#******************************************************************************************************************************************************

def date_wise_detail(cu_date):

    cu_date = cu_date
    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    a_sum = 0
    x = 0

    print("{}          {}    {}   {:<8}  {:<10} {} {:>4}  {:>3}     {:>6}  {:>6}".format('Date','Bill','Cu_ID','Cu_Name','Item','Item_code','Item_rate','Qty','Amount','a_sum'))
    print()


    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity
            
            if date == cu_date:
                a_sum = a_sum + amount
                t_name = tr_cu_name
                t_id = tr_cu_id
                t_date = cu_date
                print("{}    {}   {}   {:<8}  {:<10}  {}     {:>4}     {:>3}     {:>6}   {:>6}".format(t_date,bill,t_id,t_name,item,item_code,item_rate,quantity,amount,a_sum))
    print()
    print("Total ::                                                                      {:>6}".format(a_sum))
    print()
                
#******************************************************************************************************************************************************

# 23480

def item_wise_detail(i_name):
    i_name = i_name

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    a_sum = 0
    q_sum = 0
    x = 0
    
    print("{:>3}     {:<10} {:<8}  {:<6}   {:<5}   {:<5}   {:<8}  {:>3}  {:>3}  {:>6} {:>6}".format('x','date','bill','item','item_code','cu_id',\
                'cu_name','item_rate','qty','amount','a_sum'))
    print()


    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity


            if item == i_name:
                a_sum = a_sum + amount
                q_sum = q_sum + quantity
                x = x+1

                print("{:>3}  {:<10}   {:<8}  {:<10} {:<5}      {:<5}   {:<8}    {:>3}    {:>3} {:>6}   {:>6}".format(x,date,bill,item,\
                    item_code,tr_cu_id,tr_cu_name,item_rate,quantity,amount,a_sum))
    print()
    print("Total ::                                                                    {:>4} {:>6}".format(q_sum,a_sum))
                
  


def item_wise_detail_all():
    for u in range(len(tr_item_un)):
        item_wise_detail(tr_item_un[u])
        print()
        print()


def item_wise_summary():


    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    x = 0

    print("  {:<10}   {:<6}   {:>3}   {:>6}   {:>6}  {:>6}".format('Item_name','Item_Code','Item_Rate','Quantity','T_Amount','C_Sum'))
    print()

    for u in range(len(tr_item_un)):
        i_name = tr_item_un[u]
        a_sum = 0
        q_sum = 0

        for i in range(len(tr)):
            for j in range(1,len(tr[i])):
                item = tr[i][j][0]
                quantity = tr[i][j][1]
                tr_cu_id = tr[i][0][0]
                bill = tr[i][0][1]
                date = tr[i][0][2]


                for k in range(len(cu)):
                    if tr_cu_id == cu[k][0]:
                        tr_cu_name = cu[k][1]
                for l in range(len(item_detail)):
                    if item == item_detail[l][1]:
                        item_code = item_detail[l][0]
                        item_rate = item_detail[l][2]
                amount = item_rate * quantity

                if item == i_name:
                    a_sum = a_sum + amount
                    q_sum = q_sum + quantity
                    t_item_code = item_code
                    t_item_name = item
                    t_item_rate = item_rate
                    

                    
        c_sum = c_sum + a_sum        
        print("  {:<10}     {:<6}      {:>3}     {:>6}       {:>6}    {:>6}".format(t_item_name,t_item_code,t_item_rate,q_sum,a_sum,c_sum))
    print()
    print("Total ::                                          {:>6}".format(c_sum))
    print()




def item_wise_amount(i_name):
    i_name = i_name

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    a_sum = 0
    q_sum = 0
    x = 0

    print("  {:<10}   {:<6}   {:>3}   {:>6}   {:>6}".format('Item_name','Item_Code','Item_Rate','Quantity','T_Amount'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity
        
            

            if item == i_name:
                a_sum = a_sum + amount
                q_sum = q_sum + quantity
                t_item_name = i_name
                t_item_code = item_code
                t_item_rate = item_rate
                
                        
    print("  {:<10}     {:<6}      {:>3}     {:>6}       {:>6}".format(t_item_name,t_item_code,t_item_rate,q_sum,a_sum))
    print()

#******************************************************************************************************************************************************



def item_cust(i_name,c_name):
    i_name = i_name
    c_name = c_name

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    s_amount = 0
    x = 0
    prn2 = 0
    

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity

            if item == i_name:
                if tr_cu_name == c_name:
                    s_amount = s_amount + amount   
                    prn2 = s_amount
    return prn2
                
#******************************************************************************************************************************************************

def col_sum(cst_name):
    s = 0
    cst_name = cst_name
    for i in range(len(tr_item_un)):
        k = tr_item_un[i]
        a = item_cust(k,cst_name)
        pr_h = "{:<10} {:>3}".format(k,a)
        pr_o = "{:>3}".format(a)
        s = s + a
    return s

#******************************************************************************************************************************************************



def item_cust_matrix():

    print("{:<10}".format('Item_Name'),end = '  ')
    for i in range(len(tr_cu_un)):
        cm_name = cu_name_id(tr_cu_un[i])
        print("{:<7} ".format(cm_name),end = ' ')
    print("{:>5}   {:>8}".format('Sum','C_Sum'))
    print()


    sum_g = 0   #This is for cumulative total sum
    it = 0
    co_sum = 0
    s_sum = 0

    for j in range(len(tr_item_un)):
        sum1 = 0   #This is for each total sum
        ina = tr_item_un[j]
        print("{:<10}".format(ina),end = '  ')

        for i in range(len(tr_cu_un)):
            n = cu_name_id(tr_cu_un[i])
            it = item_cust(ina,n)
            sum1 = sum1 + it
            sum_g = sum_g + it
            print("{:>5} ".format(it),end = '   ')
        print("{:>5} {:>10}".format(sum1,sum_g))

    print()

    print("{:<10}".format('Col_Total'),end = '  ')
    for i in range(len(tr_cu_un)):
        q = cu_name_id(tr_cu_un[i])
        pr = col_sum(q)
        s_sum = s_sum + pr
        print("{:>5} ".format(pr),end = '   ')
    print(s_sum)    

#******************************************************************************************************************************************************



def item_cust_detail(i_name,c_name):
    i_name = i_name
    c_name = c_name

    item = ''
    quantity = 0
    tr_cu_id = ''
    bill = ''
    date = ''
    tr_cu_name = ''
    item_code = ''
    item_rate = 0
    amount = 0
    c_sum = 0
    s_amount = 0
    x = 0
    prn2 = 0
    q_sum = 0
    x = 0

    print("{:>3}     {:<10} {:<8}  {:<6}   {:<5}   {:<5}   {:<8}  {:>3}  {:>3}  {:>6} {:>6}".format('Sn','date','bill','item','item_code','cu_id',\
                'cu_name','item_rate','qty','amount','a_sum'))
    print()

    for i in range(len(tr)):
        for j in range(1,len(tr[i])):
            item = tr[i][j][0]
            quantity = tr[i][j][1]
            tr_cu_id = tr[i][0][0]
            bill = tr[i][0][1]
            date = tr[i][0][2]


            for k in range(len(cu)):
                if tr_cu_id == cu[k][0]:
                    tr_cu_name = cu[k][1]
            for l in range(len(item_detail)):
                if item == item_detail[l][1]:
                    item_code = item_detail[l][0]
                    item_rate = item_detail[l][2]
            amount = item_rate * quantity

            if item == i_name:
                if tr_cu_name == c_name:
                    s_amount = s_amount + amount   
                    q_sum = q_sum + quantity
                    x = x+1
                    #prn2 = s_amount
                    print("{:>3}  {:<10}   {:<8}  {:<10} {:<5}      {:<5}   {:<8}    {:>3}    {:>3} {:>6}   {:>6}".format(x,date,bill,item,\
                    item_code,tr_cu_id,tr_cu_name,item_rate,quantity,amount,s_amount))
    print()
    print("Total ::                                                                    {:>4} {:>6}".format(q_sum,s_amount))
    

main_tr_db()


item_wise_summary()