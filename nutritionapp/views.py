from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import mysql.connector
import datetime

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="nutrifit_db")
    return mydb

def nindex(request):
    try:
        
        nid = request.session["id"]

        selpen = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active'  and a.a_status='Pending' and n.n_id = '"+str(nid)+"' order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selpen)
        apen_data = mycursor.fetchall()

        selap = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Approved' and n.n_id = '"+str(nid)+"' order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selap)
        aap_data = mycursor.fetchall()

        selcan = "select count(a_id) from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Cancel' and n.n_id = '"+str(nid)+"' order by a.a_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selcan)
        acan_data = mycursor.fetchall()

        seluser = "select count(u_id) from user_tb   order by u_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(seluser)
        user_data = mycursor.fetchall()


        selspe = "select count(s_id) from specialization_tb order by s_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selspe)
        spe_data = mycursor.fetchall()


        selnt = "select count(n_id) from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and n.n_id != '"+str(nid)+"' order by n.n_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selnt)
        nt_data = mycursor.fetchall()

        selcn = "select count(c_id) from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n where c.a_id = a.a_id and c.u_id=u.u_id and c.n_id=n.n_id and  u.u_status ='Active' and  n.n_status ='Active'  and n.n_id = '"+str(nid)+"' order by c.c_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selcn)
        cn_data = mycursor.fetchall()

        selpa = "select count(p_id) from payment_tb p,user_tb u,nutritionist_tb n,appointment_tb a where a.a_id = p.p_payment_id  and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Appointment' and n.n_id = '"+str(nid)+"' order by p.p_id desc"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(selpa)
        pa_data = mycursor.fetchall()

        selpc = "select count(p_id) from payment_tb p,user_tb u,nutritionist_tb n,consult_tb c where c.c_id = p.p_payment_id and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Consult' and n.n_id = '"+str(nid)+"' order by p.p_id desc"
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
            'pa_data':pa_data,
            'pc_data':pc_data,
            'fd_data':fd_data,


        }
        
        return render(request,'nindex.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nlogin(request):
    try:
        msg = ""
        if request.POST:
            contact = request.POST.get("n_contact")
            password = request.POST.get("n_password")

            sellogin = "select * from nutritionist_tb where n_contact =  '"+str(contact)+"' and n_password = '"+str(password)+"'  and n_status ='Active'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sellogin)
            ldata = mycursor.fetchall()

            if len(ldata) > 0:
                
                request.session["id"] = ldata [0] [0]
                request.session["name"] = ldata [0] [2]
                request.session["contact"] = contact
                request.session["time"] = str(ldata[0][13])
                request.session["img"] = ldata [0] [6]
                
                return redirect("nindex")
            else:
                 msg = "Invalid Contact Or Password.!" 
                 
                 return render(request,'nlogin.html',{'msg':msg})  

        else:
            return render(request,'nlogin.html',{'msg':msg})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nlogout(request):
    try:
        contact = request.session["contact"] 
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        update = "update nutritionist_tb set n_udate = '"+cdate+"' where n_contact = '"+str(contact)+"'"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(update)
        mydb.commit()

        request.session["id"] = None
        request.session["contact"] = None
        request.session["name"] = None
        request.session["time"] = None
        request.session["img"] = None

        return redirect("nlogin")
            
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nprofile(request):
    try:
        if request.POST:
            
            nid = request.session["id"]
            n_name = request.POST.get("n_name")
            n_image = request.POST.get("n_image")
            s_id = request.POST.get("s_id")
            n_address = request.POST.get("n_address")
            n_gender = request.POST.get("n_gender")
            
            n_experience = request.POST.get("n_experience")
            n_fees = request.POST.get("n_fees")
            n_password = request.POST.get("n_password")
           

            if request.POST.get("n_image")!= "":
                n_image = request.FILES["n_image"]
                img = FileSystemStorage()
                old_image = img.save(n_image.name,n_image)
            else:
                old_image = request.POST.get("old_image")

            if request.POST.get("n_certificate")!= "":
                n_certificate = request.FILES["n_certificate"]
                img = FileSystemStorage()
                old_image1 = img.save(n_certificate.name,n_certificate)
            else:
                old_image1 = request.POST.get("old_image1")
            
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            update = "update nutritionist_tb set s_id = '"+str(s_id)+"',n_name='"+str(n_name)+"',n_address = '"+str(n_address)+"',n_gender = '"+str(n_gender)+"',n_experience = '"+str(n_experience)+"',n_fees = '"+str(n_fees)+"',n_password = '"+str(n_password)+"',n_image = '"+str(old_image)+"',n_certificate = '"+str(old_image1)+"',n_udate = '"+cdate+"' where n_id = '"+str(nid)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()

            return redirect("nindex")
        
        
        else:
            nid = request.session["id"]

            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and n.n_id = '"+str(nid)+"'  order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            sel = "select * from specialization_tb  where s_status = 'Active' order by s_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            sp_data = mycursor.fetchall()

            alldata= {
                'n_data':n_data,
                'sp_data':sp_data,
            }
            

            return render(request,'nprofile.html',alldata)
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def napproved(request):

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

            return redirect("napproved")

        elif request.GET.get("a_id") !=None:

            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")

            if a_status=="Pending":

                a_status="Approved"

            elif a_status=="Approved":

                a_status="Cancel"

            else:

                a_status="Pending"


            updatef="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()

            return redirect("napproved")

        else:            

            nid = request.session["id"]

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Approved' and n.n_id='"+str(nid)+"' order by a.a_id desc"

            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'napproved.html',{'a_data':a_data})

    except NameError:

        print("internal error")

    except:

        print('Error returned')

def npending(request):

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

            return redirect("npending")

        
        elif request.GET.get("a_id") !=None:

            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")

            if a_status=="Pending":

                a_status="Approved"

            elif a_status=="Approved":

                a_status="Cancel"

            else:

                a_status="Pending"


            updatef="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(updatef)
            mydb.commit()

            return redirect("npending")

        else:            

            nid = request.session["id"]
            
            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active'  and a.a_status='Pending' and n.n_id='"+str(nid)+"' order by a.a_id desc"

            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'npending.html',{'a_data':a_data})

    except NameError:

        print("internal error")

    except:

        print('Error returned')

def ncancel(request):

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

            return redirect("ncancel")  

        elif request.GET.get("a_id") !=None:

            a_id = request.GET.get("a_id")
            a_status=request.GET.get("a_status")

            if a_status=="Pending":

                a_status="Approved"

            elif a_status=="Approved":

                a_status="Cancel"

            else:

                a_status="Pending"

            update="update appointment_tb set a_status= '"+str(a_status)+"' where a_id='"+str(a_id)+"'" 

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()

            return redirect("ncancel")

        else:

            nid = request.session["id"]

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and a.a_status='Cancel' and n.n_id='"+str(nid)+"' order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'ncancel.html',{'a_data':a_data})

    except NameError:

        print("internal error")

    except:

        print('Error returned')

def nappointmentreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            status = request.POST.get("status")
            nid = request.session["id"]

            sel = "select * from appointment_tb a, user_tb u, specialization_tb s, nutritionist_tb n where a.u_id = u.u_id and a.s_id = s.s_id and a.n_id = n.n_id and a_status = '"+str(status)+"' and DATE(a_cdate) between '"+str(startdate)+"' and '"+str(enddate)+"' and n.n_id='"+str(nid)+"' order by a.a_id desc"

            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()

            return render(request,'nappointmentreport.html',{'a_data':a_data})
        else:
            return render(request,'nappointmentreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nconsult(request):
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

            return redirect("nconsult")

        else:

            nid = request.session["id"]
            
            sel = "select * from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n where c.a_id = a.a_id and c.u_id=u.u_id and c.n_id=n.n_id and  u.u_status ='Active' and  n.n_status ='Active'  and n.n_id='"+str(nid)+"' order by c.c_id desc"
            
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            c_data = mycursor.fetchall()

            return render(request,'nconsult.html',{'c_data':c_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nconsultreport(request):
    try:
        if request.POST:
            startdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            nid = request.session["id"]

            sel = "select * from consult_tb c,appointment_tb a,user_tb u,nutritionist_tb n  where c.a_id = a.a_id and c.u_id = u.u_id and  c.n_id = n.n_id and c.u_id and n_cdate between '"+str(startdate)+"' and '"+str(enddate)+"' and n.n_id='"+str(nid)+"' order by c.c_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            c_data = mycursor.fetchall()

            return render(request,'nconsultreport.html',{'c_data':c_data})
        else:
            return render(request,'nconsultreport.html',{})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def naddconsult(request):
    try:
        if request.POST:
            a_id = request.GET.get("aedit") 
            u_id = request.POST.get("u_id") 
            nid = request.POST.get("n_id") 
            c_title = request.POST.get("c_title")
            c_treatment = request.POST.get("c_treatment")
            
            if request.POST.get("c_file")!= "": 
                c_file = request.FILES["c_file"]
                img = FileSystemStorage()
                c_file = img.save(c_file.name,c_file)

            else:
                c_file = "nofile.jpg"

            c_fees = request.POST.get("c_fees")
            p_type = 'Consult'
            p_status = 'Failed'
            c_date = request.POST.get("c_date")
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO `consult_tb`( `a_id`, `u_id`, `n_id`, `c_title`, `c_treatment`, `c_file`, `c_fees`, `c_date`, `c_cdate`, `c_udate`) VALUES ('"+str(a_id)+"','"+str(u_id)+"','"+str(nid)+"','"+str(c_title)+"','"+str(c_treatment)+"','"+str(c_file)+"','"+str(c_fees)+"','"+str(c_date)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

            last_id = mycursor.lastrowid 

            payins = "INSERT INTO `payment_tb`(`u_id`, `n_id`, `p_type`, `p_payment_id`, `p_amount`, `p_status`, `p_cdate`, `p_udate`) VALUES ('"+str(u_id)+"','"+str(nid)+"','"+str(p_type)+"','"+str(last_id)+"','"+str(c_fees)+"','"+str(p_status)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(payins)
            mydb.commit()

            return redirect("nconsult")
        
        else:

            a_id = request.GET.get("aedit")
            
            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n where a.u_id = u.u_id and a.n_id = n.n_id and  u.u_status ='Active' and  n.n_status ='Active'  and a.a_id='"+str(a_id)+"'"
            
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            c_data = mycursor.fetchall()

            return render(request,'naddconsult.html',{'c_data':c_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nuser(request):

    try:
        if request.GET.get("u_id")!=None:
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
            return redirect("nuser")
            
        else:

            sel = "select * from user_tb order by u_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            user_data = mycursor.fetchall()

            return render(request,'nuser.html',{'user_data':user_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nnutritionist(request):
    try:
            
            nid = request.session["id"]
            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and n.n_id != '"+str(nid)+"' order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'nnutritionist.html',{'n_data':n_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nspecialization(request):

    try:
        
        if request.GET.get("sdel")!=None:
            sdel = request.GET.get("sdel")

            delete = "delete from specialization_tb where s_id = '"+str(sdel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(delete)
            mydb.commit()
            return redirect("nspecialization")
        
        else:

            sel = "select * from specialization_tb order by s_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            sp_data = mycursor.fetchall()

            return render(request,'nspecialization.html',{'sp_data':sp_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def npappointment(request):
    try:
        if request.GET.get("p_id")!=None:
            
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
            return redirect("npappointment")

        else:
            
            nid = request.session["id"]
            sel = "select * from payment_tb p,user_tb u,nutritionist_tb n,appointment_tb a where a.a_id = p.p_payment_id  and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Appointment' and n.n_id = '"+str(nid)+"' order by p.p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            p_data = mycursor.fetchall()

            return render(request,'npappointment.html',{'p_data':p_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def npconsult(request):
    try:
        if request.GET.get("p_id")!=None:
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
            return redirect("npconsult")

        else:
            nid = request.session["id"]

            sel = "select * from payment_tb p,user_tb u,nutritionist_tb n,consult_tb c where c.c_id = p.p_payment_id and p.u_id=u.u_id and p.n_id=n.n_id and n.n_status = 'Active' and u.u_status = 'Active' and p.p_type = 'Consult' and n.n_id = '"+str(nid)+"' order by p.p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            p_data = mycursor.fetchall()

            return render(request,'npconsult.html',{'p_data':p_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nfeedback(request):

    try:
        if request.GET.get("f_id")!=None:
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
            return redirect("nfeedback")

        else:

            sel = "select * from feedback_tb order by f_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            f_data = mycursor.fetchall()

            return render(request,'nfeedback.html',{'f_data':f_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

