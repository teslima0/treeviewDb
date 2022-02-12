from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkinter import ttk
from tkinter import messagebox

root= tk.Tk()
root.title("OAU PGUMMAH DATABASE")
#root.iconphoto(False, tk.PhotoImage(file="C:/Users/TAMAR/Desktop/database_tk/ico.jpg"))
#root.tk.call('wm', 'iconphoto',  tk.PhotoImage(file="C:/Users/TAMAR/Desktop/database_tk/ico.jpg"))
#img=Image.open('ico.jpg')
#p1=PhotoImage(file="C:/Users/TAMAR/Desktop/database_tk/ico.jpg")
#root.iconphoto(False,p1)
#photo=ImageTk.PhotoImage(img)
#root.iconphoto(False, tk.PhotoImage(file=photo))
root.geometry("3000x2550")
#add menue


def query_database():
     #clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record) 
    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()

    c.execute("SELECT rowid,* FROM pgumhcustomers")
    records=c.fetchall()

    #add you data to the screen


    global count
    count=0
    #for record in records:
       # print(record)


    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=("evenrow",))

        else:
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=("oddrow",))

        # increment count 

        count +=1
        #print(records)
       
       #commite change
    conn.commit()

    #close our connection
    conn.close()

def search_records():
    lookup_record=search_entry.get()
    print(lookup_record)
    #close the search box
    search.destroy()
    #clear treeview
    for record in my_tree.get_children():
        my_tree.delete(record) 

    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()

    c.execute("SELECT rowid,* FROM  pgumhcustomers WHERE last_name like ?", (lookup_record,))
    records=c.fetchall()

    #add you data to the screen


    global count
    count=0
    #for record in records:
       # print(record)
 

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=("evenrow",))

        else:
            my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17],record[18]), tags=("oddrow",))

        # increment count 

        count +=1
        #print(records)
       
       #commite change
    conn.commit()

    #close our connection
    conn.close()


#command for search
def lookup_record():
    global search_entry, search
    #root.iconbitmap('pg.ico')
    search=Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    #create label frame

    search_frame= LabelFrame(search, text= "Last Name")
    search_frame.pack(padx=10, pady=10)
    # add entry box
    search_entry= Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(padx=20, pady=20)

    #add button
    search_button= Button(search, text="Search Records", command=search_records)
    search_button.pack(padx=20, pady=20)

my_menu=Menu(root)
root.config(menu=my_menu)

#configure menue

search_menu=Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
#drop down menue

search_menu.add_command(label="Search", command= lookup_record)
search_menu.add_separator()
search_menu.add_command(label="Reset", command= query_database)

#fake data
'''
data=[

    
    ["1","Adedolapo",   "Teslim", "Oyedotun", "Computer", "100543", "Oyo","programer","080976545"],
    ["2","Adedolapo1", "Teslim1", "Oyedotun1", "Computer1", "1005431", "hOyo","programer1","0809765452"],
    ["3","Adedolapo2", "Teslim2", "Oyedotun2", "Computer2", "1005432", "dOyo","programer2","0809765453"],
    ["4","Adedolapo3", "Teslim3", "Oyedotun3", "Computer3", "1005433", "tyo","programer3","0809765454"],
    ["5","Adedolapo4", "Teslim4", "Oyedotun4", "Computer4", "1005434", "ayo","programer4","0809765455"],
    ["6","Adedolapo5", "Teslim5", "Oyedotun5", "Computer5", "1005435", "uyo","programer5","0809765456"],
    ["7","Adedolapo6", "Teslim6", "Oyedotun6", "Computer6", "1005436", "Ouo","programer6","0809765457"],
    ["8","Adedolapo7", "Teslim7", "Oyedotun7", "Computer7", "1005437", "Oeo","programer7","0809765458"],
    ["9","Adedolapo8", "Teslim8", "Oyedotun8", "Computer8", "1005438", "Oso","programer8","0809765450"],
    ["1","Adedolapo",   "Teslim", "Oyedotun", "Computer", "100543", "Oyo","programer","080976545"],
    ["2","Adedolapo1", "Teslim1", "Oyedotun1", "Computer1", "1005431", "hOyo","programer1","0809765452"],
    ["3","Adedolapo2", "Teslim2", "Oyedotun2", "Computer2", "1005432", "dOyo","programer2","0809765453"],
    ["4","Adedolapo3", "Teslim3", "Oyedotun3", "Computer3", "1005433", "tyo","programer3","0809765454"],
    ["5","Adedolapo4", "Teslim4", "Oyedotun4", "Computer4", "1005434", "ayo","programer4","0809765455"],
    ["6","Adedolapo5", "Teslim5", "Oyedotun5", "Computer5", "1005435", "uyo","programer5","0809765456"],
    ["7","Adedolapo6", "Teslim6", "Oyedotun6", "Computer6", "1005436", "Ouo","programer6","0809765457"],
    ["8","Adedolapo7", "Teslim7", "Oyedotun7", "Computer7", "1005437", "Oeo","programer7","0809765458"],
    ["9","Adedolapo8", "Teslim8", "Oyedotun8", "Computer8", "1005438", "Oso","programer8","0809765450"],
    ["1","Adedolapo",   "Teslim", "Oyedotun", "Computer", "100543", "Oyo","programer","080976545"],
    ["2","Adedolapo1", "Teslim1", "Oyedotun1", "Computer1", "1005431", "hOyo","programer1","0809765452"],
    ["3","Adedolapo2", "Teslim2", "Oyedotun2", "Computer2", "1005432", "dOyo","programer2","0809765453"],
    ["4","Adedolapo3", "Teslim3", "Oyedotun3", "Computer3", "1005433", "tyo","programer3","0809765454"],
    ["5","Adedolapo4", "Teslim4", "Oyedotun4", "Computer4", "1005434", "ayo","programer4","0809765455"],
    ["6","Adedolapo5", "Teslim5", "Oyedotun5", "Computer5", "1005435", "uyo","programer5","0809765456"],
    ["7","Adedolapo6", "Teslim6", "Oyedotun6", "Computer6", "1005436", "Ouo","programer6","0809765457"],
    ["8","Adedolapo7", "Teslim7", "Oyedotun7", "Computer7", "1005437", "Oeo","programer7","0809765458"],
    ["9","Adedolapo8", "Teslim8", "Oyedotun8", "Computer8", "1005438", "Oso","programer8","0809765450"],
    ["10","Adedolapo9", "Teslim9", "Oyedotun9", "Computer9", "1005439", "Oro","programe9r","0809765459", "next of kin name", "next of kin no"]

   ]
'''
#create a database or connect to the existing db


conn= sqlite3.connect('pgummah.db')

#create a cusor
c=conn.cursor()

#create table

c.execute("""CREATE TABLE if not exists pgumhcustomers(
        id integer,
        first_name text,
        middle_name text,
        last_name text,
        gender text,
        marital text,
        department text,
        Reg_no text,
        admission text,
        program text,
        state text,
        skill text,
        phone_no integer,
        email text,
        employ text,
        post text,
        next_of_kname text,
        next_of_kno integer


    )""")

'''
#add dumy data to database
for record in data:


    c.execute("INSERT INTO pgumhcustomers VALUES(:id, :first_name, :middle_name, :last_name, :gender, :marital, :department, :Reg_no, :admission, :program, :state, :skill, :phone_no, :email, :employ, :post,  :next_of_kname, :next_of_kno )",
       
    {

            'id': record[0],
            'first_name': record[1],
            'middle_name': record[2],
            'last_name': record[3],
            'gender': record[4],
            'marital': record[5],
            'department': record[6],
            'Reg_no': record[7],
            'admission': record[8],
            'program': record[9],
            'state': record[10],
            'skill': record[11],
            'phone_no': record[12],
            'email': record[13],
            'employ': record[14],
            'department': record[15],
            'next_of_kname': record[16],
            'next-of_kno': record[17]

     })   
'''
#commite change
conn.commit()

#close our connection
conn.close()



#root= Tk()
#root.title("OAU PGUMMAH DATABASE Treeview")
#root.iconbitmap('pg.ico')
#root.geometry("600x600")

#add some style
style= ttk.Style()
#pick a theme
style.theme_use("default")

#configure the threeview color
style.configure("Treeview",
    background= "D3D3D3",
    foreground= "black",
    rowheight=25,
    fieldbackground=" #D3D3D3")

#change selected color
style.map("Treeview", 
    background=[("selected", "#347083")])

#create a Treeview frame
tree_frame=Frame(root)
tree_frame.pack(pady=10)

#create a treeview scrow bar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#create treeview
my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode= "extended")
my_tree.pack()

#configure the scrollbar

tree_scroll.config(command=my_tree.yview)

#define the colomn


'''
hsb=ttk.Scrollbar(root, orient="horizontal")
hsb.configure(command=tree_scroll)
tree_scroll.configure(xyscrollcomand=hsb.set)
hsb.pack(fill=X,side=BOTTOM)
'''
#create a treeview scrow bar
tree_scroll = Scrollbar(tree_frame,orient="horizontal")
tree_scroll.pack(side=BOTTOM, fill=X)

#create treeview
#my_tree=ttk.Treeview(tree_frame, xscrollcommand=tree_scroll.set, selectmode= "extended")
#my_tree.pack()

#configure the scrollbar

tree_scroll.config(command=my_tree.xview)



my_tree["columns"]=("ID", "First Name", "Middle Name", "Last Name", "Gender", "Marial Status", "Department", "Registration No", "Year Of Admission", "Program", "State", "Skill", "Phone No", "Email", "Employment", "Post Held",  "Next Of Kin Name", "Next Of Kin No"  )


#format column

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor= CENTER, width=100)
my_tree.column("First Name", anchor= CENTER, width=140)
my_tree.column("Middle Name", anchor= CENTER, width=140)
my_tree.column("Last Name", anchor= CENTER, width=140)
my_tree.column("Gender", anchor= CENTER, width=140)
my_tree.column("Marial Status", anchor= CENTER, width=140)
my_tree.column("Department", anchor= CENTER, width=140)
my_tree.column("Registration No", anchor= CENTER, width=140)
my_tree.column("Year Of Admission", anchor= CENTER, width=140)
my_tree.column("Program", anchor= CENTER, width=140)
my_tree.column("State", anchor= CENTER, width=140)
my_tree.column("Skill", anchor= CENTER, width=140)
my_tree.column("Phone No", anchor= CENTER, width=140)
my_tree.column("Email", anchor= CENTER, width=140)
my_tree.column("Employment", anchor= CENTER, width=140)
my_tree.column("Post Held", anchor= CENTER, width=140)
my_tree.column("Next Of Kin Name", anchor= CENTER, width=200)
my_tree.column("Next Of Kin No", anchor= CENTER, width=140)




#create heading
my_tree.heading("#0", text="", anchor= W)
my_tree.heading("ID", text="ID", anchor= CENTER)
my_tree.heading("First Name", text="First Name", anchor= CENTER)
my_tree.heading("Middle Name", text="Middle Name", anchor= CENTER)
my_tree.heading("Last Name", text="Last Name", anchor= CENTER)
my_tree.heading("Gender", text="Gender", anchor= CENTER)
my_tree.heading("Marial Status", text="Marial Status", anchor= CENTER)
my_tree.heading("Department", text="Department", anchor= CENTER)
my_tree.heading("Registration No", text="Registration No", anchor= CENTER)
my_tree.heading("Year Of Admission", text="Year Of Admission", anchor= CENTER)
my_tree.heading("Program", text="Program", anchor=CENTER)
my_tree.heading("State", text="State", anchor=CENTER)
my_tree.heading("Skill", text="Skill", anchor= CENTER)
my_tree.heading("Phone No", text="Phone No", anchor= CENTER)
my_tree.heading("Email", text="Email", anchor= CENTER)
my_tree.heading("Employment", text="Employment", anchor=CENTER)
my_tree.heading("Post Held", text="Post Held", anchor= CENTER)
my_tree.heading("Next Of Kin Name", text="Next Of Kin Name", anchor= CENTER)
my_tree.heading("Next Of Kin No", text="Next Of Kin No", anchor= CENTER)



#create stripe row tags
my_tree.tag_configure("oddrow", background="white")
my_tree.tag_configure("evenrow", background="lightblue")

#add data to the screen
'''
global count
count=0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[8],record[8],record[8]), tags=("evenrow",))

    else:
        my_tree.insert(parent="", index="end", iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[8],record[8],record[8]), tags=("oddrow",))

  # increment count 

    count +=1

'''
#add record entry boxes
data_frame=LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label=Label(data_frame, text="ID")
id_label.grid(row=0,column=0, padx=10,pady=10)
id_entry=Entry(data_frame)
id_entry.grid(row=0,column=1, padx=10, pady=10)

fn_label=Label(data_frame, text="First Name")
fn_label.grid(row=0,column=2, padx=10,pady=10)
fn_entry=Entry(data_frame)
fn_entry.grid(row=0,column=3, padx=10, pady=10)

mn_label=Label(data_frame, text="Middle Name")
mn_label.grid(row=0,column=4, padx=10,pady=10)
mn_entry=Entry(data_frame)
mn_entry.grid(row=0,column=5, padx=10, pady=10)

ln_label=Label(data_frame, text="Last Name")
ln_label.grid(row=0,column=6, padx=10,pady=10)
ln_entry=Entry(data_frame)
ln_entry.grid(row=0,column=7, padx=10, pady=10)

ad_label=Label(data_frame, text="Year Of Admission")
ad_label.grid(row=0,column=8, padx=10,pady=10)
ad_entry=Entry(data_frame)
ad_entry.grid(row=0,column=9, padx=10, pady=10)

gd_label=Label(data_frame, text="Gender")
gd_label.grid(row=1,column=0, padx=10,pady=10)
gd_entry=Entry(data_frame)
gd_entry.grid(row=1,column=1, padx=10, pady=10)

mr_label=Label(data_frame, text="Marital Status")
mr_label.grid(row=1,column=2, padx=10,pady=10)
mr_entry=Entry(data_frame)
mr_entry.grid(row=1,column=3, padx=10, pady=10)

dp_label=Label(data_frame, text="Department")
dp_label.grid(row=1,column=4, padx=10,pady=10)
dp_entry=Entry(data_frame)
dp_entry.grid(row=1,column=5, padx=10, pady=10)

reg_label=Label(data_frame, text="Registration")
reg_label.grid(row=1,column=6, padx=10,pady=10)
reg_entry=Entry(data_frame)
reg_entry.grid(row=1,column=7, padx=10, pady=10)



pg_label=Label(data_frame, text="Program")
pg_label.grid(row=1,column=8, padx=10,pady=10)
pg_entry=Entry(data_frame)
pg_entry.grid(row=1,column=9, padx=10, pady=10)

st_label=Label(data_frame, text="State Of Origin")
st_label.grid(row=2,column=0, padx=10,pady=10)
st_entry=Entry(data_frame)
st_entry.grid(row=2,column=1, padx=10, pady=10)

sk_label=Label(data_frame, text="Soft Skill")
sk_label.grid(row=2,column=2, padx=10,pady=10)
sk_entry=Entry(data_frame)
sk_entry.grid(row=2,column=3, padx=10, pady=10)

ph_label=Label(data_frame, text="Phone No")
ph_label.grid(row=2,column=4, padx=10,pady=10)
ph_entry=Entry(data_frame)
ph_entry.grid(row=2,column=5, padx=10, pady=10)

em_label=Label(data_frame, text="Email")
em_label.grid(row=2,column=6, padx=10,pady=10)
em_entry=Entry(data_frame)
em_entry.grid(row=2,column=7, padx=10, pady=10)


epl_label=Label(data_frame, text="Employment")
epl_label.grid(row=2,column=8, padx=10,pady=10)
epl_entry=Entry(data_frame)
epl_entry.grid(row=2,column=9, padx=10, pady=10)

ps_label=Label(data_frame, text="Post Held")
ps_label.grid(row=3,column=0, padx=10,pady=10)
ps_entry=Entry(data_frame)
ps_entry.grid(row=3,column=1, padx=10, pady=10)



next_kname_label=Label(data_frame, text="Next Of Kin Name")
next_kname_label.grid(row=3,column=2, padx=10,pady=10)
next_kname_entry=Entry(data_frame)
next_kname_entry.grid(row=3,column=3, padx=10, pady=10)

next_kno_label=Label(data_frame, text="Next Of Kin No")
next_kno_label.grid(row=3,column=4, padx=10,pady=10)
next_kno_entry=Entry(data_frame)
next_kno_entry.grid(row=3,column=5, padx=10, pady=10)



#move row up

def up():
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)


#move row down

def down():
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row),my_tree.index(row)+1)



#remove one record

def remove_one():
    x=my_tree.selection()[0]
    my_tree.delete(x)

    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()

    c.execute("DELETE from pgumhcustomers WHERE oid="+ id_entry.get())
    conn.commit()

    #close our connection
    conn.close()
    #clear entry box function
    clear_entry()
    #add a little message box

    messagebox.showinfo("Deleted!", "yor message has been deleted")


#remove many
def remove_many():
    #add a little message bos 
    response=messagebox.askyesno("WOAH!!", "This will DELETE SELECTED Item From Database\n are you sure you want to delete")

    #add logic for message box

    if response ==1:
        #designated selection   
        x=my_tree.selection()

        #create list of id

        ids_to_delete=[]

        
        #add selection to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[0])

            
         
         #delete from treeview

        for record in x:

            my_tree.delete(record)
        conn= sqlite3.connect('pgummah.db')

        #create a cusor
        c=conn.cursor()
        
        #delete lits of seleted item from database
        c.executemany("DELETE FROM pgumhcustomers WHERE id=?", [(a,) for a in ids_to_delete])


        conn.commit()

            #close our connection
        conn.close()
        
            
        


#remove all record

def remove_all():
      #add a little message bos 
     response=messagebox.askyesno("WOAH!!", "This Wll DELETE All The Record In The Database\n are you sure you want to delete?")
     if response== 1:
            for record in my_tree.get_children():
                my_tree.delete(record) 

            conn= sqlite3.connect('pgummah.db')

                #create a cusor
            c=conn.cursor()
                
                #delete everything from the table
            c.execute("DROP TABLE pgumhcustomers")


            conn.commit()

                    #close our connection
            conn.close()
            # clear entry
            clear_entry()
            #recreate the table
            create_table_again()

#add data to database
def add_record():
    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()
    c.execute("INSERT INTO pgumhcustomers VALUES (:id, :f_name, :middle_name, :last_name, :gender, :marital, :department, :Reg_no, :admission, :program, :state, :skill, :phone_no, :email, :employ, :post, :next_of_kname, :next_of_kno)",
              {
                  'id': id_entry.get(),
                  'f_name': fn_entry.get(),
                  'middle_name': mn_entry.get(),
                  'last_name': ln_entry.get(),
                  'gender': gd_entry.get(),
                  'marital': mr_entry.get(),
                  'department': dp_entry.get(),
                  'Reg_no': reg_entry.get(),
                  'admission': ad_entry.get(),
                  'program': pg_entry.get(),
                  'state': st_entry.get(),
                  'skill': sk_entry.get(),
                  'phone_no': ph_entry.get(),
                  'email': em_entry.get(),
                  'employ': epl_entry.get(),
                  'post': ps_entry.get(),
                  'next_of_kname': next_kname_entry.get(),
                  'next_of_kno': next_kno_entry.get()
                        
              } )


    conn.commit()

        #close our connection
    conn.close()
    #clear entry box
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    mn_entry.delete(0,END)
    ln_entry.delete(0,END)
    gd_entry.delete(0,END)
    mr_entry.delete(0,END)
    dp_entry.delete(0,END)
    reg_entry.delete(0,END)
    ad_entry.delete(0,END)
    pg_entry.delete(0,END)
    st_entry.delete(0,END)
    sk_entry.delete(0,END)
    ph_entry.delete(0,END)
    em_entry.delete(0,END)
    epl_entry.delete(0,END)
    ps_entry.delete(0,END)
    next_kname_entry.delete(0,END)
    next_kno_entry.delete(0,END)

    #clear the treeview table

    my_tree.delete(*my_tree.get_children())
    #run database on start
    query_database()

def create_table_again():
    
    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()

    #create table

    c.execute("""CREATE TABLE if not exists pgumhcustomers(
            id integer,
            first_name text,
            middle_name text,
            last_name text,
            gender text,
            marital text,
            department text,
            Reg_no text,
            admission text,
            program text,
            state text,
            skill text,
            phone_no integer,
            email text,
            employ text,
            post text,
            next_of_kname text,
            next_of_kno integer

        )""")

    '''
    #add dumy data to database
    for record in data:


        c.execute("INSERT INTO pgumhcustomers VALUES(:id, :first_name, :middle_name, :last_name, :gender, :marital, :department, :Reg_no, :admission, :program, :state, :skill, :phone_no, :email, :employ, :post, :next_of_kname, :next_of_kno )",
        
        {

                'id': record[0],
                'first_name': record[1],
                'middle_name': record[2],
                'last_name': record[3],
                'gender': record[4],
                'marital': record[5],
                'department': record[6],
                'Reg_no': record[7],
                'admission': record[8],
                'program': record[9],
                'state': record[10],
                'skill': record[11],
                'phone_no': record[12],
                'email': record[13],
                'employ': record[14],
                'post': record[15],
                'next_of_kname': record[16],
                'next-of_kno': record[17]

        })   
    '''
    #commite change
    conn.commit()

    #close our connection
    conn.close()



#update

def update_record():
    #grab the record

    selected=my_tree.focus()
    #update the record number

    my_tree.item(selected, text="", values=(id_entry.get(),fn_entry.get(),mn_entry.get(),ln_entry.get(), gd_entry.get(), mr_entry.get(),dp_entry.get(), reg_entry.get(), ad_entry.get(), pg_entry.get(), st_entry.get(),sk_entry.get(),ph_entry.get(), em_entry.get(), epl_entry.get(), ps_entry.get(), next_kname_entry.get(), next_kno_entry.get(),))
    
    #updatw the database
    conn= sqlite3.connect('pgummah.db')

    #create a cusor
    c=conn.cursor()

    c.execute(""" UPDATE pgumhcustomers SET
        'first_name' = :first,
        'middle_name' = :m_name,
        'last_name'= :l_name,
        'gender'= :n_gender,
        'marital'= :n_marital,
        'department'= :n_department,
        'Reg_no'= :n_Reg_no,
        'admission'= :n_admission,
        'program'= :n_program,
        'state'= :n_state,
        'skill'= :n_skills,
        'phone_no'= :n_phone_no,
        'email'= :n_email,
        'employ'= :n_employ,
        'post'= :n_post,
        'next_of_kname'= :n_next_of_kname,
        'next_of_kno'= :n_next_of_kno

        WHERE oid = :oid""",
        {
        'first': fn_entry.get(),
        'm_name': mn_entry.get(),
        'l_name': ln_entry.get(),
        'n_gender': gd_entry.get(),
        'n_marital': mr_entry.get(),
        'n_department': dp_entry.get(),
        'n_Reg_no': reg_entry.get(),
        'n_admission': ad_entry.get(),
        'n_program': pg_entry.get(),
        'n_state': st_entry.get(),
        'n_skills': sk_entry.get(),
        'n_phone_no': ph_entry.get(),
        'n_email' : em_entry.get(),
        'n_employ': epl_entry.get(),
        'n_post': ps_entry.get(),
        'n_next_of_kname': next_kname_entry.get(),
        'n_next_of_kno': next_kno_entry.get(),
        'oid': id_entry.get(),
        } )

    #add you data to the screen


    
    conn.commit()

    #close our connection
    conn.close()
    



    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    mn_entry.delete(0,END)
    ln_entry.delete(0,END)
    gd_entry.delete(0,END)
    mr_entry.delete(0,END)
    dp_entry.delete(0,END)
    reg_entry.delete(0,END)
    ad_entry.delete(0,END)
    pg_entry.delete(0,END)
    st_entry.delete(0,END)
    sk_entry.delete(0,END)
    ph_entry.delete(0,END)
    em_entry.delete(0,END)
    epl_entry.delete(0,END) 
    ps_entry.delete(0,END)   
    next_kname_entry.delete(0,END)
    next_kno_entry.delete(0,END)
    #clear entry func


def clear_entry():
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    mn_entry.delete(0,END)
    ln_entry.delete(0,END)
    gd_entry.delete(0,END)
    mr_entry.delete(0,END)
    dp_entry.delete(0,END)
    reg_entry.delete(0,END)
    ad_entry.delete(0,END)
    pg_entry.delete(0,END)
    st_entry.delete(0,END)
    sk_entry.delete(0,END)
    ph_entry.delete(0,END)
    em_entry.delete(0,END)
    epl_entry.delete(0,END)
    ps_entry.delete(0,END) 
    next_kname_entry.delete(0,END)
    next_kno_entry.delete(0,END)

#select record

def select_record(e):
    
    id_entry.delete(0,END)
    fn_entry.delete(0,END)
    mn_entry.delete(0,END)
    ln_entry.delete(0,END)
    gd_entry.delete(0,END)
    mr_entry.delete(0,END)
    dp_entry.delete(0,END)
    reg_entry.delete(0,END)
    ad_entry.delete(0,END)
    pg_entry.delete(0,END)
    st_entry.delete(0,END)
    sk_entry.delete(0,END)
    ph_entry.delete(0,END)
    em_entry.delete(0,END)
    epl_entry.delete(0,END)
    ps_entry.delete(0,END) 
    next_kname_entry.delete(0,END)
    next_kno_entry.delete(0,END)

    #output to entry
    

    #grab record no
    selected=my_tree.focus()
    #grap record value
    values=my_tree.item(selected, 'values')
 
     #outputs to entry box
    id_entry.insert(0,values[0])
    fn_entry.insert(0,values[1])
    mn_entry.insert(0,values[2])
    ln_entry.insert(0,values[3])
    gd_entry.insert(0,values[4])
    mr_entry.insert(0,values[5])
    dp_entry.insert(0,values[6])
    reg_entry.insert(0,values[7])
    ad_entry.insert(0,values[8])
    pg_entry.insert(0,values[9])
    st_entry.insert(0,values[10])
    sk_entry.insert(0,values[11])
    ph_entry.insert(0,values[12])
    em_entry.insert(0,values[13])
    epl_entry.insert(0,values[14])
    ps_entry.insert(0,values[15])
    next_kname_entry.insert(0,values[16])
    next_kno_entry.insert(0,values[17])


#add button
button_frame=LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button=Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)


add_button=Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button=Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_many_button=Button(button_frame, text="Remove Many Records", command=remove_many)
remove_many_button.grid(row=0, column=3, padx=10, pady=10)

remove_one_button=Button(button_frame, text="Remove One Record", command=remove_one)
remove_one_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button=Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button=Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button=Button(button_frame, text="Clear Entery Boxes", command=clear_entry)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

#binding the treeview

my_tree.bind("<ButtonRelease-1>", select_record)

#run database on start
query_database()

root.mainloop()