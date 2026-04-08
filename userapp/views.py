from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import mysql.connector
import datetime
import random
import requests
from django.http import JsonResponse

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="nutrifit_db")
    return mydb

def uindex(request):
    try:
        sel = "select * from specialization_tb where s_status ='Active' order by s_id desc"
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sel)
        sdata = mycursor.fetchall() 

        selfd = "select * from feedback_tb where f_status ='Show' order by f_id desc"
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(selfd)
        fdata = mycursor.fetchall() 

        alldata = {
            'sdata' : sdata,
            'fdata' : fdata,
        }

        return render(request,'uindex.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uprofile(request):
    try:
        if request.POST:
            
            uid = request.session["uid"]
            u_name = request.POST.get("u_name")
            u_address = request.POST.get("u_address")
            u_gender = request.POST.get("u_gender")
            u_image = request.POST.get("u_image")

            if request.POST.get("u_image")!= "":
                u_image = request.FILES["u_image"]
                img = FileSystemStorage()
                old_image = img.save(u_image.name,u_image)
            else:
                old_image = request.POST.get("old_image")

            u_dob = request.POST.get("u_dob")
            u_bloodgroup = request.POST.get("u_bloodgroup")
            u_password = request.POST.get("u_password")
           
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            update = "update user_tb set u_name='"+str(u_name)+"',u_address = '"+str(u_address)+"',u_gender = '"+str(u_gender)+"',u_image = '"+str(old_image)+"',u_dob = '"+str(u_dob)+"',u_bloodgroup = '"+str(u_bloodgroup)+"',u_password = '"+str(u_password)+"',u_udate = '"+cdate+"' where u_id = '"+str(uid)+"'"
      
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()

            return redirect("uindex")
        
        
        else:
            uid = request.session["uid"]

            usel = "select * from user_tb where u_id = '"+str(uid)+"'"
           
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(usel)
            u_data = mycursor.fetchall()

            return render(request,'uprofile.html',{'u_data':u_data})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uappointment(request):

    try:
        msg=""
        if request.POST:
          
            u_id = request.session["uid"]
            n_id = request.GET.get("nid") 
            s_id = request.POST.get("s_id")
            a_title = request.POST.get("a_title")
            a_symptoms = request.POST.get("a_symptoms")
            a_date = request.POST.get("a_date")
            a_fees = request.POST.get("a_fees")
            a_remarks = request.POST.get("a_remarks")
            
            a_status = 'Pending'
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            selapp = "select * from appointment_tb a,nutritionist_tb n, user_tb u where a.n_id=n.n_id and a.u_id = u.u_id and  a.a_status ='Pending' and a.n_id = '"+str(n_id)+"' and a.u_id = '"+str(u_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(selapp)
            a_data = mycursor.fetchall()

            if len(a_data) > 0:
                msg = "Appointment is Already Booked.!"                 
                return render(request,'uappointment.html',{'msg':msg})  

            else:
                ins = "INSERT INTO `appointment_tb`(`u_id`, `n_id`, `s_id`, `a_title`, `a_symptoms`, `a_date`, `a_fees`, `a_remarks`, `a_status`, `a_cdate`, `a_udate`) VALUES ('"+str(u_id)+"','"+str(n_id)+"','"+str(s_id)+"','"+str(a_title)+"','"+str(a_symptoms)+"','"+str(a_date)+"','"+str(a_fees)+"','"+str(a_remarks)+"','"+str(a_status)+"','"+cdate+"','"+cdate+"')"
                
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()

                last_id = mycursor.lastrowid 

                return redirect(f"/uapayment?last_id={last_id}&nid={n_id}&afees={a_fees}")  
                
        
        else:
            n_id = request.GET.get("nid") 
            
            sel = "select * from nutritionist_tb n, specialization_tb s where n.s_id = s.s_id and s.s_status ='Active' and  n.n_id = '"+str(n_id)+"'"
            
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall()
            
            alldata= {
                'a_data':a_data,
                'msg':msg,
            }
            

            return render(request,'uappointment.html',alldata)

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ucontactus(request):

    try:
        if request.POST:
            f_name = request.POST.get("f_name")
            f_contact = request.POST.get("f_contact")
            f_message = request.POST.get("f_message")
            f_status = "Hide"

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
            ins = "insert into feedback_tb(f_name,f_contact,f_message,f_status,f_cdate,f_udate) values('"+str(f_name)+"','"+str(f_contact)+"','"+str(f_message)+"','"+str(f_status)+"','"+cdate+"','"+cdate+"')"

            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(ins)
            mydb.commit()

        return render(request,'ucontactus.html',{})

    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uaboutus(request):
    try:
        

                
        return render(request,'uaboutus.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def ulogin(request):
    try:
        msg = ""
        if request.POST:
            contact = request.POST.get("u_contact")
            password = request.POST.get("u_password")

            sellogin = "select * from user_tb where u_contact =  '"+str(contact)+"' and u_password = '"+str(password)+"'  and u_status ='Active'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(sellogin)
            ldata = mycursor.fetchall()
          
            if len(ldata) > 0:
                    
                request.session["uid"] = ldata [0] [0]
                request.session["uname"] = ldata [0] [1]
                request.session["ucontact"] = contact
              

                return redirect("uindex")
            else:
                msg = "Invalid Contact Or Password.!"                 
                return render(request,'ulogin.html',{'msg':msg})  

        else:
            return render(request,'ulogin.html',{'msg':msg})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def logout(request):
    try:
        uid = request.session["uid"] 
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        update = "update user_tb set u_udate = '"+cdate+"' where u_id = '"+str(uid)+"'"
        mydb = getdb()
        mycursor = mydb.cursor()
        mycursor.execute(update)
        mydb.commit()

        request.session["uid"] = None
        request.session["uname"] = None
        request.session["ucontact"] = None       


        return redirect("uindex")
            
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def usignup(request):
    try:
        msg = ""
        if request.POST:

            rtype = request.GET.get("verify")

            if rtype == 'number':

                u_contact = request.POST.get("u_contact")
                
                usel = "select * from user_tb where u_contact = '"+str(u_contact)+"'"
           
                mydb = getdb()
                mycursor = mydb.cursor(dictionary=True)
                mycursor.execute(usel)
                u_data = mycursor.fetchall()

                if len(u_data) > 0:
                    msg = "This Contact Number is Already Registered."
                    return render(request,'usignup.html',{'msg' : msg})
                
                else:
                    otp = random.randrange(1000,9999)
                    mtype = "OTP"
                    request.session['otp'] = otp
                    request.session['contact'] = u_contact

                    sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={u_contact}&message={otp}&type={mtype}"
                    response = requests.post(sms_url)
                    return redirect('/usignup?verify=otp')
                
            elif rtype == 'otp':
                u_otp = request.POST.get("u_otp")
                otp = request.session['otp']
                if u_otp == str(otp):
                    return redirect('/usignup?verify=usignup')
                else:
                     msg = "Invalid OTP..!"
                     return render(request,'usignup.html',{'msg':msg}) 
            else:

                u_name = request.POST.get("u_name")
                u_address = request.POST.get("u_address")
                u_gender = request.POST.get("u_gender")
                u_contact = request.POST.get("u_contact")
                
                u_image = request.FILES["u_image"]
                img = FileSystemStorage()
                u_image = img.save(u_image.name,u_image)
     
                u_dob = request.POST.get("u_dob")
                u_bloodgroup = request.POST.get("u_bloodgroup")            
                u_password = request.POST.get("u_password")
                u_status = "Active"
           
                cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                
                ins = "INSERT INTO user_tb(`u_name`, `u_contact`, `u_address`, `u_gender`, `u_image`, `u_dob`, `u_bloodgroup`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES ('"+str(u_name)+"','"+str(u_contact)+"','"+str(u_address)+"','"+str(u_gender)+"','"+str(u_image)+"','"+str(u_dob)+"','"+str(u_bloodgroup)+"','"+str(u_password)+"','"+str(u_status)+"','"+cdate+"','"+cdate+"')"
                
                
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()

                return redirect("ulogin")
       
        else:
            return render(request,'usignup.html',{'msg' : msg})
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def resendotp(request):
    try:
        otp = random.randrange(1000,9999)
        mtype = "OTP"
        request.session['otp'] = otp
        u_contact = request.session['contact'] 

        sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={u_contact}&message={otp}&type={mtype}"
        response = requests.post(sms_url)
        return redirect('/usignup?verify=otp')
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def uforgotpassword(request):
    try:
        msg = ""
        if request.POST:
            u_contact = request.POST.get("u_contact")
           
            sel = "select * from user_tb where u_contact =  '"+str(u_contact)+"' and u_status = 'Active'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            udata = mycursor.fetchall()
            
   
            if len(udata) > 0:
                
                upassword = udata[0]["u_password"]

                mtype = "Forgotpassword"

                sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={u_contact}&message={upassword}&type={mtype}"
                response = requests.post(sms_url)

                return redirect('/ulogin?alert=1')
                
            else:
                msg = "Contact Number Is Not Registered.!" 
                return render(request,'uforgotpassword.html',{'msg':msg})  
        else:
            return render(request,'uforgotpassword.html',{'msg' : msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')    

def unsignup(request):
    try:
        msg = ""
        if request.POST:
            
            rtype = request.GET.get("verify")
            
            if rtype == 'number':
                
                n_contact = request.POST.get("n_contact")

                sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and n_contact = '"+str(n_contact)+"'"
                mydb = getdb()
                mycursor = mydb.cursor(dictionary=True)
                mycursor.execute(sel)
                n_data = mycursor.fetchall()
                
                if len(n_data) > 0:
                    
                    msg = "This Contact Number is Already Registered."
                    sels="SELECT * FROM specialization_tb  where s_status = 'Active' "
                    mydb = getdb()
                    mycursor = mydb.cursor(dictionary=True)
                    mycursor.execute(sels)
                    sp_data = mycursor.fetchall()

                    alldata= {
                    
                    'sp_data':sp_data,
                    'msg':msg

                    }  
                    return render(request,'unsignup.html',alldata)
                
                else:
                    otp = random.randrange(1000,9999)
                    mtype = "OTP"
                    request.session['notp'] = otp
                    request.session['ncontact'] = n_contact

                    sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={n_contact}&message={otp}&type={mtype}"
                    response = requests.post(sms_url)
                    return redirect('/unsignup?verify=otp')
                
            elif rtype == 'otp':
                u_otp = request.POST.get("n_otp")
                otp = request.session['notp']
                if u_otp == str(otp):
                    return redirect('/unsignup?verify=unsignup')
                else:
                    msg = "Invalid OTP..!"
                    sels="SELECT * FROM specialization_tb  where s_status = 'Active' "
                    mydb = getdb()
                    mycursor = mydb.cursor(dictionary=True)
                    mycursor.execute(sels)
                    sp_data = mycursor.fetchall()

                    alldata= {
                    
                    'sp_data':sp_data,
                    'msg':msg

                    }  
                    return render(request,'unsignup.html',alldata) 
            else:
                n_contact = request.POST.get("n_contact")
                s_id = request.POST.get("s_id")
                n_name = request.POST.get("n_name")
                
                n_address = request.POST.get("n_address")
                n_gender = request.POST.get("n_gender")

            
                n_image = request.FILES["n_image"]  
                img = FileSystemStorage()
                n_image = img.save(n_image.name,n_image)

                n_experience = request.POST.get("n_experience")

                n_certificate = request.FILES["n_certificate"]  
                img = FileSystemStorage()
                n_certificate = img.save(n_certificate.name,n_certificate)
           
                n_fees = request.POST.get("n_fees")
                n_password = request.POST.get("n_password")
                n_status = "Active"

                cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             
                ins="INSERT INTO nutritionist_tb(s_id, n_name, n_contact, n_address, n_gender, n_image, n_experience, n_certificate, n_fees, n_password, n_status, n_cdate, n_udate) VALUES ('"+str(s_id)+"','"+str(n_name)+"','"+str(n_contact)+"','"+str(n_address)+"','"+str(n_gender)+"','"+str(n_image)+"','"+str(n_experience)+"','"+str(n_certificate)+"','"+str(n_fees)+"','"+str(n_password)+"','"+str(n_status)+"','"+cdate+"','"+cdate+"')"
               
                mydb = getdb()
                mycursor = mydb.cursor()
                mycursor.execute(ins)
                mydb.commit()

                return redirect("uindex")

        else:
            
            sels="SELECT * FROM specialization_tb  where s_status = 'Active' "
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sels)
            sp_data = mycursor.fetchall()

            alldata= {
                
                'sp_data':sp_data,
                'msg':msg

            }  

            return render(request,'unsignup.html',alldata)

        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def nresendotp(request):
    try:
        otp = random.randrange(1000,9999)
        mtype = "OTP"
        request.session['notp'] = otp
        u_contact = request.session['ncontact'] 

        sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={u_contact}&message={otp}&type={mtype}"
        response = requests.post(sms_url)
        return redirect('/unsignup?verify=otp')
        
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def unforgotpassword(request):
    try:
        msg = ""
        if request.POST:
            n_contact = request.POST.get("n_contact")
           
            sel = "select * from nutritionist_tb where n_contact =  '"+str(n_contact)+"' and n_status = 'Active'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            ndata = mycursor.fetchall()
            
   
            if len(ndata) > 0:

                upassword = ndata[0]["n_password"]

                mtype = "Forgotpassword"

                sms_url = f"https://invisionsoftwaresolution.in/Student/isssmssend.php?contact={n_contact}&message={upassword}&type={mtype}"
                response = requests.post(sms_url)

                return redirect('/unsignup?verify=number&alert=1')
                
            else:
                msg = "Contact Number Is Not Registered.!" 
                return render(request,'unforgotpassword.html',{'msg':msg})  
        else:
            return render(request,'unforgotpassword.html',{'msg' : msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')    

def umyappointment(request):

    try:

        if request.GET.get("adel")!= None:
            adel = request.GET.get("adel")

            delete = "delete from appointment_tb where a_id ='"+str(adel)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(delete)
            mydb.commit()
            return redirect("umyappointment")
        else:
            u_id = request.session["uid"]

            sel = "select * from appointment_tb a,user_tb u,nutritionist_tb n, specialization_tb s where  a.u_id=u.u_id and a.n_id=n.n_id and a.s_id = s.s_id and  s.s_status ='Active' and n.n_status = 'Active' and u.u_status = 'Active' and u.u_id='"+str(u_id)+"' order by a.a_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            a_data = mycursor.fetchall   

            
            return render(request,'umyappointment.html',{'a_data':a_data})

    except NameError:

        print("internal error")

    except:

        print('Error returned')

def uconsult(request):

    try:
        a_id = request.GET.get("a_id")

        sel = "select * from consult_tb c,user_tb u,nutritionist_tb n,appointment_tb a where  c.u_id=u.u_id and c.n_id=n.n_id and c.a_id=a.a_id and c.a_id='"+str(a_id)+"' and u.u_status ='Active' and  n.n_status ='Active'"        
       
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sel)
        c_data = mycursor.fetchall()   


        
        return render(request,'uconsult.html',{'c_data':c_data})

    except NameError:

        print("internal error")

    except:

        print('Error returned')


def uourteam(request):
    try:
        if request.GET.get("sid")!=None:
            sid = request.GET.get("sid")

            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and  n.n_status ='Active' and n.s_id = '"+str(sid)+"' order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'uourteam.html',{'n_data':n_data})

        else:
            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and  n.n_status ='Active' order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'uourteam.html',{'n_data':n_data})

    except NameError:
        print("internal error")
    except:
        print('Error returned')


def uteamdetails(request):
    try:
        if request.GET.get("nid")!=None:
            nid = request.GET.get("nid")

            sel = "select * from nutritionist_tb n,specialization_tb s where n.s_id = s.s_id and  s.s_status ='Active' and  n.n_status ='Active' and n.n_id='"+str(nid)+"'  order by n.n_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(sel)
            n_data = mycursor.fetchall()

            return render(request,'uteamdetails.html',{'n_data':n_data})


    except NameError:
        print("internal error")
    except:
        print('Error returned')


def uprivacypolicy(request):
    try:        
        return render(request,'uprivacypolicy.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def umypayment(request):
    try:
        u_id = request.session["uid"]
    
        sel = "select * from payment_tb p,user_tb u,nutritionist_tb n where p.u_id=u.u_id and p.n_id=n.n_id and u.u_id='"+str(u_id)+"'  order by p.p_id desc"
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sel)
        p_data = mycursor.fetchall()

        alldata= {
                'p_data':p_data,  
                }
         
        return render(request,'umypayment.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def upayment(request):
    try:
        if request.POST:
          
            p_payment_id= request.GET.get("p_payment_id")    
            p_status = 'Success'
    
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         
            update = "update payment_tb set p_status = '"+str(p_status)+"',p_udate = '"+cdate+"' where p_payment_id = '"+str(p_payment_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(update)
            mydb.commit()
            return redirect("umypayment")
        else:
        
            return render(request,'upayment.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def uapayment(request):
    try:
        if request.POST:
          
            p_payment_id  = request.GET.get("last_id") 
            nid = request.GET.get("nid")
            u_id = request.session["uid"]
            p_amount = request.GET.get("afees")
            p_type = 'Appointment'    
            p_status = 'Success'
    
            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            payins = "INSERT INTO `payment_tb`(`u_id`, `n_id`, `p_type`, `p_payment_id`, `p_amount`, `p_status`, `p_cdate`, `p_udate`) VALUES ('"+str(u_id)+"','"+str(nid)+"','"+str(p_type)+"','"+str(p_payment_id)+"','"+str(p_amount)+"','"+str(p_status)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor()
            mycursor.execute(payins)
            mydb.commit()
            return redirect("umyappointment")
        
        else:
        
            return render(request,'uapayment.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

