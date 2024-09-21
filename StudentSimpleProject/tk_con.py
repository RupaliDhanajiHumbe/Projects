from tkinter import*
from tkinter import messagebox
import mysql.connector as sql

def insert():
    rollno=s_rollno.get()
    name=s_name.get()
    address=s_address.get()
    if(rollno=="" or name=="" or address==""):
         messagebox.showinfo("insert status","All filed are required")
    else:
            con=sql.connect(host="localhost",user="Rupali",password="root",database="Student")
            cur=con.cursor()
            cur.execute("insert into Student values('"+ rollno +"','"+ name +"','"+ address +"')")
            cur.execute("commit")

            s_rollno.delete(0,'end')
            s_name.delete(0,'end')
            s_address.delete(0,'end')
            # show()
            messagebox.showinfo("insert status","Record insert successfully")
            con.close()
def delete():
    if(s_rollno.get() == ""):
       messagebox.showinfo("Delete status","rollno is complsary for delete")
    else:
        con=sql.connect(host="localhost",user="Rupali",password="root",database="Student")
        cur=con.cursor()
        cur.execute("delete from Student where rollno='"+ s_rollno.get() +"'")
        cur.execute("commit")

        s_rollno.delete(0,'end')
        s_name.delete(0,'end')
        s_address.delete(0,'end')
        #show()
        messagebox.showinfo("delete status","Record delete successfully")
        con.close()

def update():
    rollno=s_rollno.get()
    name=s_name.get()
    address=s_address.get()
    if(rollno=="" or name=="" or address==""):
         messagebox.showinfo("update status","All filed are required")

    else:
            con=sql.connect(host="localhost",user="Rupali",password="root",database="Student")
            cur=con.cursor()
            cur.execute("update bca2 set rollno='"+ rollno +"',address='"+ address +"' where name='"+ name +"'")
            cur.execute("commit")

            s_rollno.delete(0,'end')
            s_name.delete(0,'end')
            s_address.delete(0,'end')

           # show()
            messagebox.showinfo("update status","Record update successfully")
            con.close()

def get():
    if(s_rollno.get() == ""):
       messagebox.showinfo("fetch status","rollno is complsary for search record")
    else:
        con=sql.connect(host="localhost",user="Rupali",password="root",database="Student")
        cur=con.cursor()
        cur.execute("select *from Student where rollno='"+s_rollno.get() +"'")
        rows=cur.fetchall()
        for row in rows:
            s_name.insert(0,row[1])
            s_address.insert(0,row[2])
        con.close()    
def show():
    con=sql.connect(host="localhost",user="Rupali",password="root",database="Student")
    cur=con.cursor()
    cur.execute("select *from Student")
    rows=cur.fetchall()
    for row in rows:
        insertData=str(row[0])+'      '+ str(row[1])
        list.insert(list.size()+1,insertData)
        s_rollno.delete(0,'end')
        s_name.delete(0,'end')
        s_address.delete(0,'end')
    con.close()            



root=Tk()
root.geometry("600x400")
root.title("Databace connection with GUI")

rollno=Label(root,text="Enter rollno",font=('bold',10))
rollno.place(x=20,y=30)
name=Label(root,text="Enter name",font=('bold',10))
name.place(x=20,y=60)
address=Label(root,text="Enter address",font=('bold',10))
address.place(x=20,y=90)
s_rollno=Entry()
s_rollno.place(x=150,y=30)
s_name=Entry()
s_name.place(x=150,y=60)
s_address=Entry()
s_address.place(x=150,y=90)

insert=Button(root,text='Insert',font=("italic",10),bg="White",command=insert)
insert.place(x=105,y=140)

delete=Button(root,text='Delete',font=("italic",10),bg="White",command=delete)
delete.place(x=155,y=140)
    
update=Button(root,text='update',font=("italic",10),bg="White",command=update)
update.place(x=210,y=140)

get=Button(root,text='Get',font=("italic",10),bg="White",command=get)
get.place(x=270,y=140)
list=Listbox(root,bg="pink")
list.place(x=350,y=30)
show()
root.mainloop()
    
        

        

        
