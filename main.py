from time import sleep
import mysql.connector as mycon
d = input('Enter Database name: ')
p = input('Enter MySQL password: ')
con = mycon.connect(host = 'localhost', user = 'root', passwd = p, database = d)
if con.is_connected():
    print('Connection with database succeded!')
    print()
cur = con.cursor()
ex_coun=0

def ch():
    global ex_coun
    ex_coun = 0
    print('Welcome to Book My Movie')
    op = int(input('''
Select an option:

1. Book tickets
2. Cancel tickets
3. View details of ticket

Enter serial number: '''))

    if op == 1:
        a = bookmovie()
        while a ==1:
            print('')
            print('Try Again')
            print('')
            a = bookmovie()
            return ex_coun
    elif op == 2:
        b = deltik()
        while b ==1:
            print('')
            print('Try Again')
            print('')
            b = deltik()
            return ex_coun
    elif op == 3:
        c= shwtick()
        while c==1:
            print('')
            print('Try again')
            print('')
            c=shwtick()
            return ex_coun
    else :
        print('Invalid option selected')
        ex_coun+=1
        return ex_coun
        
def disp(mlis,name):
    cmd2='select * from '+mlis+' where name='+'\''+name+'\' ;'
    cur.execute(cmd2)
    r = cur.fetchall()
    emp = []
    if r == emp:
        print('Name',name, 'is not present in the database')
    else:
        print(r)

def shwtick() :
    global ex_coun
    ex_coun = 0
    sno=int(input('Enter the serial number of movie: '))
    t=int(input('Enter issued time slot: '))
    if t not in [1,2]:
        print('Invalid Show Time Selected!')
        ex_coun += 1
        return ex_coun
    
    name=input('Enter name of the customer: ')
    if sno==1 :
        if t==1 :
            disp('m_list1',name)
        elif t==2 :
            disp('m_list2',name)
    elif sno==2 :
        if t==1 :
            disp('m_list3',name)
        elif t==2 :
            disp('m_list4',name)
    elif sno==3 :
        if t==1 :
            disp('m_list5',name)
        elif t==2 :
            disp('m_list6',name)
    elif sno==4 :
        if t==1 :
            disp('m_list7',name)
        elif t==2 :
            disp('m_list8',name)
    else:
        print('Invalid serial number entered')
        ex_coun+=1
        return ex_coun
    return ex_coun

def bookmovie() :
    global ex_coun
    ex_coun = 0
    dic_m = {1: 750, 2: 600, 3: 400, 4: 400}
    dic_f = {'a':40, "b": 150, "c": 45, "d": 0}
    dict_ex = {'a': 'Popcorn','b': 'Pizza','c': 'Pepsi','d': 'None'}
    tempz = 0
    list1 = []
    t_cost = 0
    
    n_movie = int(input('''
Please choose a movie from here

1. Venom: Let There Be Carnage
2. The Suicide Squad
3. Zack Snyder`s Justice League
4. The Conjuring: The Devil Made Me Do It

Enter serial number of the movie: '''))

    if n_movie not in [1,2,3,4]:
        print('Invalid Movie Name Selected!')
        ex_coun += 1
        return ex_coun

    t_movie = int(input('''
Please choose a suitable show time

1. 5 PM to 7 PM
2. 8 PM to 10 PM

Please enter the serial number of show time: '''))
    

    if t_movie not in [1,2]:
        print('Invalid Show Time Selected!')
        ex_coun += 1
        return ex_coun

    cus_name = input('Enter your name: ')
    p_num = int(input('Enter your mobile number: '))
    if len(str(p_num)) != 10:
        print('Please provide a 10 digit phone number')
        ex_coun +=1
        return ex_coun
    
    email= input('Enter your email: ')
    if '@' not in email:
        print('Please provide a valid email address')
        ex_coun +=1
        return ex_coun
    
    extra_s = input('''
Do you like to buy some snacks?
a. Popcorn
b. Pizza
c. Pepsi
d. No thanks!

Enter your choice: ''')

    if extra_s not in ['a','b','c','d']:
        print('Invalid Snack Opted!')
        ex_coun += 1
        return ex_coun

# Writer part of the program
    if n_movie == 1 :
        if t_movie == 1 :
            fc = open('counter1.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list1 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : Venom: Let There Be Carnage')
                print('Show Time : 5 PM to 7 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter1.txt','w')
            fc1.write(str(counter))
            fc1.close
            
        elif t_movie == 2 :
            fc = open('counter1a.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out 0f 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list2 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : Venom: Let There Be Carnage')
                print('Show Time : 8 PM to 10 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter1a.txt','w')
            fc1.write(str(counter))
            fc1.close
            
        else:
            print('Invalid input (Show time)')

    if n_movie == 2 :
        if t_movie == 1 :
            fc = open('counter2.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list3 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : The Suicide Squad')
                print('Show Time : 5 PM to 7 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter2.txt','w')
            fc1.write(str(counter))
            fc1.close
            
        elif t_movie == 2 :
            fc = open('counter2a.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list4 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : The Suicide Squad')
                print('Show Time : 8 PM to 10 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter2a.txt','w')
            fc1.write(str(counter))
            fc1.close
            
        else:
            print('Invalid input (Show time)')

    if n_movie == 3 :
        if t_movie == 1 :
            fc = open('counter3.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list5 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : Zack Snyder`s Justice League')
                print('Show Time : 5 PM to 7 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter3.txt','w')
            fc1.write(str(counter))
            fc1.close
    
        elif t_movie == 2 :
            fc = open('counter3a.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list6 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : Zack Snyder`s Justice League')
                print('Show Time : 8 PM to 10 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter3a.txt','w')
            fc1.write(str(counter))
            fc1.close
                        
        else:
            print('Invalid input (Show time)')

    if n_movie == 4 :
        if t_movie == 1 :
            fc = open('counter4.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list7 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : The Conjuring: The Devil Made Me Do It')
                print('Show Time : 5 PM to 7 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter4.txt','w')
            fc1.write(str(counter))
            fc1.close            

        elif t_movie == 2 :
            fc = open('counter4a.txt','r')
            counter = int(fc.read())
            print('Number of seats booked (out of 60): ', counter)
            sno_mov = int(input("Please enter the number of seats to be booked:"))
            if counter<60:
                for i in range(1,sno_mov+1):
                    counter+=1
                    if counter < 60 :
                        list1.append(counter)
                        tempz+=1
                    else :
                        break

                t_cost = tempz*dic_m[1]+dic_f[extra_s]
                
                cmd='''insert into m_list8 (name,m_no,email,seat,extra,cost) values(%s, %s, %s, %s, %s, %s)'''
                val=(cus_name,p_num,email,str(list1),dict_ex[extra_s],t_cost)
                cur.execute(cmd,val)
                con.commit()

                print('Total cost payable :',t_cost)
                print('')
                print('Your ticket is booked!')
                print('Name of the customer: ', cus_name)
                print('Movie Name : The Conjuring: The Devil Made Me Do It')
                print('Show Time : 8 PM to 10 PM')
                print('Number of seats booked :', tempz)
                print('Seats number are: ', list1)
                print('Snack Ordered :', dict_ex[extra_s])
                print('Total amount paid :', t_cost)
            else:
                print('Seats are full! Please select another show time.')
            fc.close()
            fc1 = open('counter4a.txt','w')
            fc1.write(str(counter))
            fc1.close

        else :
            print('Invalid input (Show time)')

def deltik():
    global ex_coun
    ex_count=0
    sno=int(input('Enter the serial number of the movie: '))
    if sno not in [1,2,3,4]:
        print('Invalid Movie Name Selected!')
        ex_coun += 1
        return ex_coun

    t=int(input('Enter issued time slot: '))
    if t not in [1,2]:
        print('Invalid Show Time Selected!')
        ex_coun += 1
        return ex_coun

    name=input('Enter customer name: ')

    if sno == 1:

        if t == 1:
   
            cmd1='delete from m_list1 where name ='+'\''+name+'\''       
            cur.execute(cmd1) 
            print('Ticket Cancelled!')          
            con.commit()
            return ex_coun
        
        elif t == 2:
          
            cmd1='delete from m_list2 where name ='+'\''+name+'\''
            cur.execute(cmd1)         
            print('Ticket Cancelled!')        
            con.commit()
            return ex_coun
        
        
    elif sno== 2 :

        if t == 1:
          
            cmd1='delete from m_list3 where name ='+'\''+name+'\''       
            cur.execute(cmd1) 
            print('Ticket Cancelled!')          
            con.commit()
            return ex_coun
        
        elif t == 2:
          
            cmd1='delete from m_list4 where name ='+'\''+name+'\''
            cur.execute(cmd1)         
            print('Ticket Cancelled!')        
            con.commit()
            return ex_coun
        
    elif sno== 3 :

        if t == 1:
                  
            cmd1='delete from m_list5 where name ='+'\''+name+'\''       
            cur.execute(cmd1) 
            print('Ticket Cancelled!')          
            con.commit()
            return ex_coun
                
        elif t == 2:
          
            cmd1='delete from m_list6 where name ='+'\''+name+'\''
            cur.execute(cmd1)         
            print('Ticket Cancelled!')        
            con.commit()
            return ex_coun
        
    elif sno== 4 :

        if t == 1:
          
            cmd1='delete from m_list7 where name ='+'\''+name+'\''       
            cur.execute(cmd1) 
            print('Ticket Cancelled!')          
            con.commit()
            return ex_coun
        
        elif t == 2:
          
            cmd1='delete from m_list8 where name ='+'\''+name+'\''
            cur.execute(cmd1)         
            print('Ticket Cancelled!')        
            con.commit()
            return ex_coun
       
    
#_main_
a = ch()
while a ==1:
    print('')
    print('Try Again')
    print('')
    a = ch()
sleep(15)
