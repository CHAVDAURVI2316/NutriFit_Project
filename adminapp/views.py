from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import mysql.connector
import datetime

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="nutrifit_db")
    return mydb

def index(request):
    try:
        

        selpen = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active'  and a.a_status='Pending' order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selpen)
        apen_data = mycursor.fetchall()

        selap = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Approved' order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selap)
        aap_data = mycursor.fetchall()

        selcan = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Cancel'  order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selcan)
        acan_data = mycursor.fetchall()

        seluser = "select count(u_id) from user_tb order by u_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(seluser)
        user_data = mycursor.fetchall()


        selspe = "select count(s_id) from specialization_tb order by s_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selspe)
        spe_data = mycursor.fetchall()


        selnt = "select count(n_id) from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' order by n.n_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selnt)
        nt_data = mycursor.fetchall()



        selcn = "select count(c_id) from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n where c.a_id = a.a_id and c.u_id=u.u_id and c.n_id=n.n_id and u.u_status ='Active' and n.n_status ='Active' order by c.c_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selcn)
        cn_data = mycursor.fetchall()

        
        selpa = "select count(p_id) from payment_tb p,user_tb u,nutritionist_tb n,appointment_tb a where a.a_id = p.p_payment_id  and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Appointment' order by p.p_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selpa)
        pa_data = mycursor.fetchall()

        selpc = "select count(p_id) from payment_tb p,user_tb u,nutritionist_tb n,consult_tb c where c.c_id = p.p_payment_id and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Consult'order by p.p_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selpc)
        pc_data = mycursor.fetchall()


        selfd = "select count(f_id) from feedback_tb order by f_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selfd)
        fd_data = mycursor.fetchall()

        alldata={
        
            'apen_data':apen_data,
            'aap_data':aap_data,
            'acan_data':acan_data,
            'user_data':user_data,
            'spe_data':spe_data,
            'nt_data':nt_data,
            'cn_data':cn_data,
            'fd_data':fd_data,
            'pa_data':pa_data,
            'pc_data':pc_data,


        }
        
        return render(request,'index.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def specialization(request):

    try:
        if request.POST:
            
            s_name = request.POST.get("s_name")

            s_image = request.FILES["s_image"]
            img = FileSystemStorage()
            s_image = img.save(s_image.name,s_image)
            
            s_status = request.POST.get("s_status")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            ins = "insert into specialization_tb(s_name,s_image,s_status,s_cdate,s_udate) values('"+str(s_name)+"','"+str(s_image)+"','"+str(s_status)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()
            return redirect("specialization")
        
        elif request.GET.get("sdel")!=None:
            sdel = request.GET.get("sdel")

            delete = "delete from specialization_tb where s_id = '"+str(sdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(delete)
            mydb.commit()
            return redirect("specialization")
        
        else:

            sel = "select * from specialization_tb order by s_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            sp_data = mycursor.fetchall()

            return render(request,'specialization.html',{'sp_data':sp_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def specializationedit(request):
    try:
        if request.POST:
            sedit = request.GET.get("sedit")
            s_name = request.POST.get("s_name")

            if request.POST.get("s_image")!= "":
                s_image = request.FILES["s_image"]
                img = FileSystemStorage()
                old_image = img.save(s_image.name,s_image)
            else:
                old_image = request.POST.get("old_image")
            
            s_status = request.POST.get("s_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            update = "update specialization_tb set s_name = '"+str(s_name)+"',s_image='"+str(old_image)+"',s_status = '"+str(s_status)+"',s_udate = '"+cdate+"' where s_id = '"+str(sedit)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()

            return redirect("specialization")
        
        
        else:
            sedit = request.GET.get("sedit")

            sel = "select * from specialization_tb where s_id = '"+str(sedit)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            sp_data = mycursor.fetchall()

            return render(request,'specializationedit.html',{'sp_data':sp_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def user(request):

    try:
        if request.GET.get("udel")!=None:
            udel = request.GET.get("udel")

            delete = "delete from user_tb where u_id = '"+str(udel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(delete)
            mydb.commit()
            return redirect("user")
        
        elif request.GET.get("u_id")!=None:
            u_id = request.GET.get("u_id")
            u_status = request.GET.get("u_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            if u_status == 'Active':
                u_status = 'Deactive'
            else:
                u_status = 'Active'

            update = "update user_tb set u_status = '"+str(u_status)+"',u_udate = '"+cdate+"' where u_id = '"+str(u_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("user")
            
        else:

            sel = "select * from user_tb order by u_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            user_data = mycursor.fetchall()

            return render(request,'user.html',{'user_data':user_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def feedback(request):

    try:
        if request.GET.get("fdel")!=None:
            fdel = request.GET.get("fdel")

            delete = "delete from feedback_tb where f_id = '"+str(fdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(delete)
            mydb.commit()
            return redirect("feedback")
        elif request.GET.get("f_id")!=None:
            f_id = request.GET.get("f_id")
            f_status = request.GET.get("f_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            if f_status == 'Show':
                f_status = 'Hide'
            else:
                f_status = 'Show'

            update = "update feedback_tb set f_status = '"+str(f_status)+"',f_udate = '"+cdate+"' where f_id = '"+str(f_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("feedback")

        else:

            sel = "select * from feedback_tb order by f_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            f_data = mycursor.fetchall()

            return render(request,'feedback.html',{'f_data':f_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nutritionist(request):
    try:
        if request.GET.get("ndel")!= None:
            ndel = request.GET.get("ndel")

            delete = "delete from nutritionist_tb where n_id ='"+str(ndel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()
            return redirect("nutritionist")
        
        elif request.GET.get("n_id")!=None:
            n_id = request.GET.get("n_id")
            n_status = request.GET.get("n_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            

            if n_status == 'Active':
                n_status = 'Deactive'
            else:
                n_status = 'Active'

            update = "update nutritionist_tb set n_status = '"+str(n_status)+"',n_udate = '"+cdate+"' where n_id = '"+str(n_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("nutritionist")

        else:

            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active'  order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'nutritionist.html',{'n_data':n_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def appointment(request):
    try:
        if request.GET.get("adel")!= None:
            adel = request.GET.get("adel")

            delete = "delete from appointment_tb where a_id ='"+str(adel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()
            return redirect("appointment")

        else:

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active'  order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'appointment.html',{'a_data':a_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def consult(request):
    try:
        if request.GET.get("cdel")!= None:
            cdel = request.GET.get("cdel")

            delete = "delete from consult_tb where c_id ='"+str(cdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()

            pdelete = "delete from payment_tb where p_payment_id ='"+str(cdel)+"' and p_type = 'Consult'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(pdelete)
            mydb.commit()

            return redirect("consult")

        else:

            sel = "select * from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n where c.a_id = a.a_id and c.u_id=u.u_id and c.n_id=n.n_id and  u.u_status ='Active' and  n.n_status ='Active'  order by c.c_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            c_data = mycursor.fetchall()

            return render(request,'consult.html',{'c_data':c_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def pappointment(request):
    try:
        if request.GET.get("pdel")!= None:
            pdel = request.GET.get("pdel")

            delete = "delete from payment_tb where p_id ='"+str(pdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()
            return redirect("pappointment")
        
        elif request.GET.get("p_id")!=None:
            p_id = request.GET.get("p_id")
            p_status = request.GET.get("p_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if p_status == 'Success':
                p_status = 'Failed'
            else:
                p_status = 'Success'

            update = "update payment_tb set p_status = '"+str(p_status)+"',p_udate = '"+cdate+"' where p_id = '"+str(p_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("pappointment")

        else:
            sel = "select * from payment_tb p,user_tb u,nutritionist_tb n,appointment_tb a where a.a_id = p.p_payment_id  and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Appointment' order by p.p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            p_data = mycursor.fetchall()

            return render(request,'pappointment.html',{'p_data':p_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def pconsult(request):
    try:
        if request.GET.get("pdel")!= None:
            pdel = request.GET.get("pdel")

            delete = "delete from payment_tb where p_id ='"+str(pdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()
            return redirect("pconsult")
        
        elif request.GET.get("p_id")!=None:
            p_id = request.GET.get("p_id")
            p_status = request.GET.get("p_status")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if p_status == 'Success':
                p_status = 'Failed'
            else:
                p_status = 'Success'

            update = "update payment_tb set p_status = '"+str(p_status)+"',p_udate = '"+cdate+"' where p_id = '"+str(p_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("pconsult")

        else:

            sel = "select * from payment_tb p,user_tb u,nutritionist_tb n,consult_tb c where c.c_id = p.p_payment_id and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Consult' order by p.p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            p_data = mycursor.fetchall()

            return render(request,'pconsult.html',{'p_data':p_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def login(request):
    try:
        msg = ""
        if request.POST:
            username = request.POST.get("l_username")
            password = request.POST.get("l_password")

            sellogin = "select * from login_tb where l_username =  '"+str(username)+"' and l_password = '"+str(password)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sellogin)
            ldata = mycursor.fetchall()

            if len(ldata) > 0:
                
                request.session["id"] = ldata [0] [0]
                request.session["username"] = username
                request.session["time"] = str(ldata[0][4])
                request.session["img"] = ldata [0] [3]
                
                return redirect("index")
            else:
                 msg = "Invalid Username Or Password.!" 
                 return render(request,'login.html',{'msg':msg})  

        else:
            return render(request,'login.html',{'msg':msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def logout(request):
    try:
        username = request.session["username"] 
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        update = "update login_tb set l_lastseen = '"+cdate+"' where l_username = '"+str(username)+"'"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(update)
        mydb.commit()

        request.session["id"] = None
        request.session["username"] = None
        request.session["time"] = None
        request.session["img"] = None
        return redirect("login")
            
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def changepassword(request):
    try:
        msg = ""
        if request.POST:
           
            currentpassword = request.POST.get("currentpassword")
            newpassword = request.POST.get("newpassword")
            confirmpassword = request.POST.get("confirmpassword")

            username = request.session["username"]
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sellogin = "select * from login_tb where l_username =  '"+str(username)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sellogin)
            ldata = mycursor.fetchall()
            
            password = ldata[0][2]

            if password == currentpassword:
                if newpassword == confirmpassword:

                    up = "update login_tb set l_password = '"+str(newpassword)+"', l_lastseen = '"+cdate+"' where l_username = '"+str(username)+"'"
                    mydb = getdb()
                    mycursor = mydb.cursor()
                    mycursor.execute(up)
                    mydb.commit()
                    return redirect("index")

                else:
                    msg = "New Password and Confirm Password Does not Match.!" 
                    return render(request,'changepassword.html',{'msg' : msg})  

            else:
                msg = "Current Password Does not Match.!"
                return render(request,'changepassword.html',{'msg' : msg})   
            
                      
       
        else:
            return render(request,'changepassword.html',{'msg' : msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def userreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            
            sel = "select * from user_tb where DATE(u_cdate) between '"+str(startdate)+"' and '"+str(enddate)+"' order by u_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            u_data = mycursor.fetchall()

            return render(request,'userreport.html',{'u_data':u_data})
        else:
            return render(request,'userreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nutritionistreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")

            sel = "SELECT * FROM nutritionist_tb n, specialization_tb s WHERE n.s_id = s.s_id AND n.n_cdate BETWEEN '" + str(startdate) + "' AND '" + str(enddate) + "' ORDER BY n.n_id DESC;"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'nutritionistreport.html',{'n_data':n_data})
        else:
            return render(request,'nutritionistreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def consultreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")

            sel = "select * from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n  where c.a_id = a.a_id and c.u_id = u.u_id and  c.n_id = n.n_id and c.u_id and n_cdate between '"+str(startdate)+"' and '"+str(enddate)+"' order by c.c_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            c_data = mycursor.fetchall()

            return render(request,'consultreport.html',{'c_data':c_data})
        else:
            return render(request,'consultreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def appointmentreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            status = request.POST.get("status")

            sel = "select * from appointment_tb a, user_tb u, specialization_tb s, nutritionist_tb n where a.u_id = u.u_id and a.s_id = s.s_id and a.n_id = n.n_id and a_status = '"+str(status)+"' and DATE(a_cdate) between '"+str(startdate)+"' and '"+str(enddate)+"' order by a.a_id desc"

            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'appointmentreport.html',{'a_data':a_data})
        else:
            return render(request,'appointmentreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def pending(request):
    try:
        if request.GET.get("adel")!= None:
            adel = request.GET.get("adel")

            delete = "delete from appointment_tb where a_id ='"+str(adel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()

            pdelete = "delete from payment_tb where p_payment_id ='"+str(adel)+"' and p_type = 'Appointment'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(pdelete)
            mydb.commit()


            return redirect("pending")
        
        elif request.GET.get("a_id") !=None:
            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")
            if a_status=="Pending":
                a_status="Approved"
            elif a_status=="Approved":
                a_status="Cancel"
            else:
                a_status="Pending"
            #query exe - run
            updatef="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("pending")

        else:

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active'  and a.a_status='Pending' order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'pending.html',{'a_data':a_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cancel(request):
    try:
        if request.GET.get("adel")!= None:
            adel = request.GET.get("adel")

            delete = "delete from appointment_tb where a_id ='"+str(adel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()

            pdelete = "delete from payment_tb where p_payment_id ='"+str(adel)+"' and p_type = 'Appointment'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(pdelete)
            mydb.commit()

            return redirect("cancel")
        
        elif request.GET.get("a_id") !=None:
            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")
            if a_status=="Pending":
                a_status="Approved"
            elif a_status=="Approved":
                a_status="Cancel"
            else:
                a_status="Pending"
            #query exe - run
            updatef="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("cancel")

        else:

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Cancel'  order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'cancel.html',{'a_data':a_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def approved(request):
    try:
        if request.GET.get("adel")!= None:
            adel = request.GET.get("adel")

            delete = "delete from appointment_tb where a_id ='"+str(adel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()

            pdelete = "delete from payment_tb where p_payment_id ='"+str(adel)+"' and p_type = 'Appointment'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(pdelete)
            mydb.commit()
            
            return redirect("approved")

        elif request.GET.get("a_id") !=None:
            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")
            if a_status=="Pending":
                a_status="Approved"
            elif a_status=="Approved":
                a_status="Cancel"
            else:
                a_status="Pending"
            #query exe - run
            updatef="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()
            return redirect("approved")

        else:

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Approved' order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'approved.html',{'a_data':a_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')