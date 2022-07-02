from cProfile import label
import time
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import FileDialog, askopenfile
from PIL import Image, ImageTk



root=Tk()
root.geometry("950x500")
root.state('zoomed')
root.title('SFSEC')
w=root.winfo_screenwidth()
h=root.winfo_screenheight()

#Functions definition
def dashboard():
    rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
    rframe.place(x=(3*w)/20,y=(h/20))
    dashboard_btn.configure(background='white',foreground='blue')
    student_btn.configure(background='blue',foreground='white')
    course_btn.configure(background='blue',foreground='white')
    faculty_btn.configure(background='blue',foreground='white')
    heading=Label(rframe,text="Dashboard",font=('Times new roman bold',30),background='white')
    heading.place(x=15,y=15)
    underline=Frame(rframe,width=(17*w)/20,height=2,background='black')
    underline.place(x=1,y=70)

def student():
    rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
    rframe.place(x=(3*w)/20,y=(h/20))
    dashboard_btn.configure(background='blue',foreground='white')
    student_btn.configure(background='white',foreground='blue')
    course_btn.configure(background='blue',foreground='white')
    faculty_btn.configure(background='blue',foreground='white')
    heading=Label(rframe,text="Students",font=('Times new roman bold',30),background='white')
    heading.place(x=15,y=15)
    underline=Frame(rframe,width=(17*w)/20,height=2,background='black')
    underline.place(x=1,y=70)
    #Buttons
    enroll_btn=Button(rframe,text="Enroll New Student",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='green',foreground='white',command=studentEnrollment)
    enroll_btn.place(x=50,y=100)
    view_btn=Button(rframe,text="View Student\'s Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='blue',foreground='white')
    view_btn.place(x=450,y=100)
    modify_btn=Button(rframe,text="Modify Student\'s Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='orange',foreground='white')
    modify_btn.place(x=850,y=100)

def course():
    rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
    rframe.place(x=(3*w)/20,y=(h/20))
    dashboard_btn.configure(background='blue',foreground='white')
    student_btn.configure(background='blue',foreground='white')
    course_btn.configure(background='white',foreground='blue')
    faculty_btn.configure(background='blue',foreground='white')
    heading=Label(rframe,text="Courses",font=('Times new roman bold',30),background='white')
    heading.place(x=15,y=15)
    underline=Frame(rframe,width=(17*w)/20,height=2,background='black')
    underline.place(x=1,y=70)
    #Buttons
    add_course_btn=Button(rframe,text="Add New Course",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='green',foreground='white')
    add_course_btn.place(x=50,y=100)
    view_course_btn=Button(rframe,text="View Course Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='blue',foreground='white')
    view_course_btn.place(x=450,y=100)
    modify_course_btn=Button(rframe,text="Modify Course Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='orange',foreground='white')
    modify_course_btn.place(x=850,y=100)

def faculty():
    rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
    rframe.place(x=(3*w)/20,y=(h/20))
    dashboard_btn.configure(background='blue',foreground='white')
    student_btn.configure(background='blue',foreground='white')
    course_btn.configure(background='blue',foreground='white')
    faculty_btn.configure(background='white',foreground='blue')
    heading=Label(rframe,text="Faculties",font=('Times new roman bold',30),background='white')
    heading.place(x=15,y=15)
    underline=Frame(rframe,width=(17*w)/20,height=2,background='black')
    underline.place(x=1,y=70)
    #Buttons
    add_faculty_btn=Button(rframe,text="Add New Faculty",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='green',foreground='white')
    add_faculty_btn.place(x=50,y=100)
    view_faculty_btn=Button(rframe,text="View Faculty\'s Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='blue',foreground='white')
    view_faculty_btn.place(x=450,y=100)
    modify_faculty_btn=Button(rframe,text="Modify Faculty\'s Details",font=('Times new roman bold',20),height=3,width=round((13*w)/1000),background='orange',foreground='white')
    modify_faculty_btn.place(x=850,y=100)

def studentEnrollment():
    rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
    rframe.place(x=(3*w)/20,y=(h/20))
    dashboard_btn.configure(background='blue',foreground='white')
    student_btn.configure(background='white',foreground='blue')
    course_btn.configure(background='blue',foreground='white')
    faculty_btn.configure(background='blue',foreground='white')
    heading=Label(rframe,text="Student Enrollment Form",font=('Times new roman bold',30),background='white')
    heading.place(x=15,y=15)
    back_btn=Button(rframe,text="Back",font=('arial bold',13),background='blue',foreground='white',command=student)
    back_btn.place(x=w-350,y=15)
    underline=Frame(rframe,width=(17*w)/20,height=2,background='black')
    underline.place(x=1,y=70)
    #Form body
    enroll=StringVar()
    sname=StringVar()
    gname=StringVar()
    gender=StringVar()
    address=StringVar()
    ph1=StringVar()
    ph2=StringVar()
    education=StringVar()
    course=StringVar()
    edate=StringVar()
    cfee=IntVar()
    ctime=StringVar()
    cduration=IntVar()
    #Enrollment No
    enrollmentno_label=Label(rframe,text="Enrollment No. : ",font=('Times new roman',15),background='white')
    enrollmentno_label.place(x=10,y=90)
    enrollmentno_entry=Entry(rframe,font=('Times new roman',15),background='yellow',textvariable=enroll)
    enrollmentno_entry.place(x=160,y=90)
    #Student's Name
    name_label=Label(rframe,text="Name of the Student : ",font=('Times new roman',15),background='white')
    name_label.place(x=10,y=130)
    name_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=30,textvariable=sname)
    name_entry.place(x=205,y=130)
    #Gurdian's Name
    gname_label=Label(rframe,text="Gurdian\'s Name : ",font=('Times new roman',15),background='white')
    gname_label.place(x=10,y=170)
    gname_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=30,textvariable=gname)
    gname_entry.place(x=170,y=170)
    #Gender
    gender_label=Label(rframe,text="Gender : ",font=('Times new roman',15),background='white')
    gender_label.place(x=10,y=210)
    male=Radiobutton(rframe,text="Male",font=('Times new roman',15),background='white',variable=gender,value='Male')
    male.place(x=100,y=210)
    female=Radiobutton(rframe,text="Female",font=('Times new roman',15),background='white',variable=gender,value='Female')
    female.place(x=200,y=210)
    other=Radiobutton(rframe,text="Others",font=('Times new roman',15),background='white',variable=gender,value='Other')
    other.place(x=300,y=210)
    #Address
    address_label=Label(rframe,text="Address : ",font=('Times new roman',15),background='white')
    address_label.place(x=10,y=250)
    address_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=50,textvariable=address)
    address_entry.place(x=100,y=250)
    #Contact Number
    mobile_label=Label(rframe,text="Contact No. : ",font=('Times new roman',15),background='white')
    mobile_label.place(x=10,y=290)
    mobile1_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=15,textvariable=ph1)
    mobile1_entry.place(x=135,y=290)
    mobile2_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=15,textvariable=ph2)
    mobile2_entry.place(x=315,y=290)
    #Education Qualification
    education_label=Label(rframe,text="Educational Qualification : ",font=('Times new roman',15),background='white')
    education_label.place(x=10,y=330)
    education_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=education)
    education_entry.place(x=250,y=330)
    #Course Offered
    course_label=Label(rframe,text="Course Offered : ",font=('Times new roman',15),background='white')
    course_label.place(x=10,y=370)
    course_entry=ttk.Combobox(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=course)
    course_entry['values']=['','Course 1','Course 2','Course 3','Course 4','Course 5']
    course_entry.place(x=165,y=370)    
    #Date of Enrollment
    course_date_label=Label(rframe,text="Date of Enroll : ",font=('Times new roman',15),background='white')
    course_date_label.place(x=10,y=410)
    course_date_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=edate)
    course_date_entry.place(x=150,y=410)
    #Course Fee
    course_fee_label=Label(rframe,text="Course Fee : ",font=('Times new roman',15),background='white')
    course_fee_label.place(x=10,y=450)
    course_fee_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=cfee)
    course_fee_entry.place(x=135,y=450)
    #Course Time
    course_time_label=Label(rframe,text="Batch/Time Selected : ",font=('Times new roman',15),background='white')
    course_time_label.place(x=10,y=490)
    course_time_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=ctime)
    course_time_entry.place(x=210,y=490)
    #Course Duration
    course_duration_label=Label(rframe,text="Course Duration : ",font=('Times new roman',15),background='white')
    course_duration_label.place(x=10,y=530)
    course_duration_entry=Entry(rframe,font=('Times new roman',15),background='yellow',width=10,textvariable=cduration)
    course_duration_entry.place(x=190,y=530)
    '''txt=StringVar()
    l=Label(rframe,textvariable=txt,font=('Times new roman',12),foreground='red')
 
    l.place(x=100,y=100)
    txt.set("Path here")'''
    def upload_photo():
        file=filedialog.askopenfilename(filetypes=[("Image File",'*.png; *.jpg; *.jpeg')])        
        if(file):
            #txt.set(f)
            #img=ImageTk.PhotoImage(Image.open(file))
            img=Image.open(file)
            r_img=img.resize((193,195))
            img=ImageTk.PhotoImage(r_img)
            l=Label(upload_photo_frame,image=img,width=193,height=195)
            l.image=img
            l.configure(image=img)
            l.place(x=0,y=0)

    def upload_sign():
        file=filedialog.askopenfilename(filetypes=[("Image File",'*.png; *.jpg; *.jpeg')])        
        if(file):
            img=Image.open(file)
            r_img=img.resize((200,70))
            img=ImageTk.PhotoImage(r_img)
            l=Label(upload_sign_frame,image=img)
            l.image=img
            l.configure(image=img)
            l.place(x=0,y=0)
    
    def upload_gsign():
        file=filedialog.askopenfilename(filetypes=[("Image File",'*.png; *.jpg; *.jpeg')])        
        if(file):
            img=Image.open(file)
            r_img=img.resize((200,70))
            img=ImageTk.PhotoImage(r_img)
            l=Label(upload_gsign_frame,image=img)
            l.image=img
            l.configure(image=img)
            l.place(x=0,y=0)
    
    
           
    #Student's Photo
    upload_photo_frame=Frame(rframe,width=195,height=195,background="gray")
    upload_photo_frame.place(x=670,y=90)
    upload_photo_label=Label(rframe,text="Student's Photo : ",font=('Times new roman',15),background='white')
    upload_photo_label.place(x=650,y=290)
    upload_photo_btn=Button(rframe,text=" Upload ",font=('Times new roman',13),background='green',foreground='white',command=upload_photo)
    upload_photo_btn.place(x=670,y=320)
    #Student's Signature
    upload_sign_frame=Frame(rframe,width=200,height=70,background='gray')
    upload_sign_frame.place(x=930,y=90)
    upload_sign_label=Label(rframe,text="Student's Signature(.png , 200x70) : ",font=('Times new roman',15),background='white')
    upload_sign_label.place(x=910,y=170)
    upload_sign_btn=Button(rframe,text=" Upload ",font=('Times new roman',13),background='green',foreground='white',command=upload_sign)
    upload_sign_btn.place(x=930,y=200)
    #Gurdian's Signature
    upload_gsign_frame=Frame(rframe,width=200,height=70,background='gray')
    upload_gsign_frame.place(x=930,y=250)
    upload_gsign_label=Label(rframe,text="Gurdian's Signature(.png , 200x70) : ",font=('Times new roman',15),background='white')
    upload_gsign_label.place(x=910,y=330)
    upload_gsign_btn=Button(rframe,text=" Upload ",font=('Times new roman',13),background='green',foreground='white',command=upload_gsign)
    upload_gsign_btn.place(x=930,y=360)
    #Onsubmit
    def submit():
        print(enroll.get(),sname.get(),gname.get(),gender.get(),address.get(),ph1.get(),ph2.get(),education.get(),course.get(),edate.get(),ctime.get(),cduration.get())
    #Submit Button
    submit_btn=Button(rframe,text='Submit',font=('Times new roman bold',15),background='green',foreground='white',command=submit)
    submit_btn.place(x=10,y=600)
    #Reset Button
    reset_btn=Button(rframe,text='Reset',font=('Times new roman bold',15),background='red',foreground='white')
    reset_btn.place(x=100,y=600)
#Upper frame (Width 100% height 5%)
uframe=Frame(root,width=w,height=h/20,background='dark blue')
uframe.place(x=0,y=0)
heading=Label(uframe,text="Siliguri Future Scope Education Centre",font=('Times new roman bold',15),background='dark blue',foreground='white')
heading.place(x=20,y=5)
logout_btn=Button(uframe,text="Logout",font=('Arial bold',10),background='red',foreground='white')
logout_btn.place(x=w-100,y=6)

#Left frame (Width 15% , height 95%)
lframe=Frame(root,width=(3*w)/20,height=(19*h)/20,background='gray')
lframe.place(x=0,y=(h/20))
dashboard_btn=Button(lframe,text="Dashboard",font=('Times new roman bold',18),background='blue',foreground='white',height=1,width=round(w/99),command=dashboard)
dashboard_btn.place(x=1,y=150)
student_btn=Button(lframe,text="Students",font=('Times new roman bold',18),background='blue',foreground='white',height=1,width=round(w/99),command=student)
student_btn.place(x=1,y=200)
course_btn=Button(lframe,text="Courses",font=('Times new roman bold',18),background='blue',foreground='white',height=1,width=round(w/99),command=course)
course_btn.place(x=1,y=250)
faculty_btn=Button(lframe,text="Faculties",font=('Times new roman bold',18),background='blue',foreground='white',height=1,width=round(w/99),command=faculty)
faculty_btn.place(x=1,y=300)

#Right frame (Width 85% height 95%)
rframe=Frame(root,width=(17*w)/20,height=(19*h)/20,background='white')
rframe.place(x=(3*w)/20,y=(h/20))
dashboard()

root.mainloop()