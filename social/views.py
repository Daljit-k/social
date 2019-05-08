from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout,
)
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import table1,reg,img_table,userpost1,Login_records,notifications,comments
#from .formslogin import UserLoginForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage



#-------------------------------------------SignUp---------------------------
def sign(request):
     if 'username1' in request.session:
          return redirect('index')
     if request.method == 'POST':
         data1=request.POST.get('un','')
         data2=request.POST.get('em','')
         data3=request.POST.get('ps','')
         data4=request.POST.get('rps','')
         #d2=reg.objects.get(email=data2)
         #return HttpResponse(data2)
         try:
            d1=reg.objects.get(uname=data1)
            request.session['unameexist'] = d1.uname
            d1=reg.objects.get(uname=data1)
            return render(request,'social/signup.html',{'d1':d1})
            
            
         except reg.DoesNotExist:
            s=reg(uname=data1,email=data2,password=data3,re_password=data4)
            s.save()
            e1=reg.objects.get(uname=data1)
            request.session['step2id'] = e1.id
            return redirect('signup2')
         else:
             return render(request,'social/signup.html')
            
         
     else:
         return render(request,'social/signup.html')
 
 
     return render(request,'social/signup.html')

#---------------------------------------------LogIn--------------------------
def log(request):
    if request.method == "POST":
        uss=request.POST['un']
        pss=request.POST['ps']
        try:
            d1=reg.objects.get(uname=uss)
            d2=reg.objects.get(password=pss)
        except reg.DoesNotExist:
            d1 = None
            d2 = None
            if(uss==d1 and pss==d2):
                return render(request,'social/signup.html')
            else:
                return render(request,'social/login.html')
        else:
            if(uss==d1.uname and pss==d2.password):
                request.session['username1'] = d1.id
                #m1=reg.objects.get(pk=d1.id)
                #data1=request.POST.get('d1.id','')
                #data2=request.POST.get('un','')
                #data3=request.POST.get('ps','')
                data4=datetime.datetime.today()
                try:
                     d1=Login_records.objects.get(userid=d1.id)
                #else:
                     #Login_records.objects.filter(userid=d1.id).update(login_time=data4)
                except Login_records.DoesNotExist:
                     s=Login_records(userid=d1.id,username=uss,password=pss,login_time=data4)
                     s.save()
                     return redirect('index')
                 #    
                else:
                     Login_records.objects.filter(username=uss).update(login_time=data4)
                     

                
                return redirect('index')
            else:
                return render(request,'social/signup1.html')
    return render(request,'social/login.html')
#-----------------------------------------------Log Out--------------------
def logout(request):
     #auth.logout(request)
     asd=request.session['username1']
     data4=datetime.datetime.today()
     Login_records.objects.filter(userid=asd).update(logout_time=data4)
     
     
     try:
          del request.session['username1']
     except KeyError:
          pass
                     
     return redirect('login')
#--------------------------------------------------------------------------Index-------

def index(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)

          newreq=notifications.objects.filter(toid=asd,reqstatus='pending')
          r1=[ ]
          for r in newreq:
               s1=r.fromid
               r1.extend([s1])
          reqname=img_table.objects.filter(uid__in=r1)

          
          cmnts=comments.objects.all()
          
          
          no_req=img_table.objects.filter(uid__in=r1).count()


          acceptedreq=notifications.objects.filter(toid=asd,reqstatus='approved')
          r2=[ ]
          for r in acceptedreq:
               s2=r.fromid
               r2.extend([s2])
          accreqname=img_table.objects.filter(uid__in=r2)

          allreq=img_table.objects.all()
          m2=img_table.objects.get(uid=asd)

          #----------show following user post-----------
          following1=notifications.objects.filter(fromid=asd,reqstatus='approved')
          t1=[ ]
          for t in following1:
               s=t.toid
               t1.extend([s])
#----------------------------You can delet this------------#
               #t1.extend(",")
          #return HttpResponse(t1)
          #t2="-".join(t1)
          #t2=t1[0]
          #return HttpResponse(t2)
          #ss=userpost1.objects.filter(userid=notifications.objects.filter(fromid=asd,reqstatus='approved'))
          #Post.objects.select_related('job','tender','news').all().order_by('-pubdat')
          '''ss=userpost1.objects.all()
          for t2 in ss:
               s2=t2.userid
               if t1 in s2:
                    u'''
          #ss=userpost1.objects.filter(userid__toid__in=t1)
          #ss=userpost1.objects.filter(userid=t1).order_by('-id')
          #ss=userpost1.objects.all(userid=following1.toid).order_by('-id')
          #ss=userpost1.objects.all().order_by('-id')
#----------------------------------------------------  
          
          ss=userpost1.objects.filter(userid__in=t1)
          t3=[ ]
          for t in ss:
               s=t.id
               t3.extend([s])

          
          ss1=comments.objects.filter(postid__in=t3)
          #------------------
          try:
               pss1=request.GET['comid']
          except:
               flag=0
               allcom=0
               pss1=0
               modimg12="dummy.jpg"
               pass
          else:
               allcom=comments.objects.filter(postid=pss1)
               modimg=userpost1.objects.filter(id=pss1)
               for ht in modimg:
                    modimg12=ht.img
               flag=1
          #----------------------------

          
          context={'all_post':ss}
          #--------------------------
          if request.method == "POST":
               qwe=request.POST['pid']
               lik=userpost1.objects.get(pk=qwe)
               likecount=int(lik.likes)
               asd=str(asd)
               wholiked=str(lik.user_liked)
               if asd in wholiked:
                    #list1=[26,28]
                    wholiked=wholiked.split(',')
                    #list1.extend([wholiked])
                    #whosplit=list1
                    #whosplit=type(whosplit)
                    #return HttpResponse(whosplit)
                    #list1.remove(asd)
                    #wholiked=list1
                    #asd=int(asd)
                    wholiked.remove(asd)
                    wholiked=','.join(wholiked)
                    #return HttpResponse(wholiked)
                    userpost1.objects.filter(pk=qwe).update(likes=likecount-1,user_liked=wholiked)

                    
                    


                    
               else:
                    #userpost1.objects.filter(userid=asd).update(likes=likecount+1,user_liked=wholiked+","+asd)
                    userpost1.objects.filter(pk=qwe).update(likes=likecount+1,user_liked=wholiked+","+asd)
                    
                    
          #------------------------------
          return render(request,'social/photo_home.html',{'pss1':pss1,'modimg':modimg12,'allcom':allcom,'flag':flag,'m1':m1,'m2':m2,'all_post':ss,'allreq':allreq,'cmnts':ss1,'no_req':no_req,'reqname':reqname,'accreqname':accreqname})
     else:
          return redirect('signup')

def profile(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)
          m2=img_table.objects.get(uid=asd)
          ss=userpost1.objects.filter(userid=asd).order_by('-id')
          context={'all_data':ss}
          pn=userpost1.objects.filter(userid=asd).count()
          flrn=notifications.objects.filter(toid=asd,reqstatus='approved').count()
          flngn=notifications.objects.filter(fromid=asd,reqstatus='approved').count()


          newreq=notifications.objects.filter(toid=asd,reqstatus='pending')
          r1=[ ]
          for r in newreq:
               s1=r.fromid
               r1.extend([s1])
          reqname=img_table.objects.filter(uid__in=r1)
          
          
          no_req=img_table.objects.filter(uid__in=r1).count()


          acceptedreq=notifications.objects.filter(toid=asd,reqstatus='approved')
          r2=[ ]
          for r in acceptedreq:
               s2=r.fromid
               r2.extend([s2])
          accreqname=img_table.objects.filter(uid__in=r2)


          
          return render(request,'social/photo_profile - Copy.html',{'m1':m1,'m2':m2,'all_data':ss,'pn':pn,'flrn':flrn,'flngn':flngn,'reqname':reqname,'accreqname':accreqname,'newreq':newreq,'acceptedreq':acceptedreq,'no_req':no_req})
     else:
          return redirect('signup')
    #return render(request,'social/photo_profile.html',{})

def explore(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)
          m2=img_table.objects.get(uid=asd)
          ss=userpost1.objects.all().order_by('-id')[:9]
          users=userpost1.objects.all().order_by('-id')[:4]
          ssss=userpost1.objects.all().order_by('-id')[:3]
          context={'all_data':ss}


          newreq=notifications.objects.filter(toid=asd,reqstatus='pending')
          r1=[ ]
          for r in newreq:
               s1=r.fromid
               r1.extend([s1])
          reqname=img_table.objects.filter(uid__in=r1)
          
          
          no_req=img_table.objects.filter(uid__in=r1).count()


          acceptedreq=notifications.objects.filter(toid=asd,reqstatus='approved')
          r2=[ ]
          for r in acceptedreq:
               s2=r.fromid
               r2.extend([s2])
          accreqname=img_table.objects.filter(uid__in=r2)

          
          return render(request,'social/photo_explore.html',{'m1':m1,'m2':m2,'all_data':ss,'users':users,'ssss':ssss,'newreq':newreq,'reqname':reqname,'accreqname':accreqname,'acceptedreq':acceptedreq,'no_req':no_req})
     else:
          return redirect('signup')
    #return render(request,'social/photo_explore.html',{})

def stories(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)
          m2=img_table.objects.get(uid=asd)



          newreq=notifications.objects.filter(toid=asd,reqstatus='pending')
          r1=[ ]
          for r in newreq:
               s1=r.fromid
               r1.extend([s1])
          reqname=img_table.objects.filter(uid__in=r1)
          
          
          no_req=img_table.objects.filter(uid__in=r1).count()


          acceptedreq=notifications.objects.filter(toid=asd,reqstatus='approved')
          r2=[ ]
          for r in acceptedreq:
               s2=r.fromid
               r2.extend([s2])
          accreqname=img_table.objects.filter(uid__in=r2)



          
          return render(request,'social/photo_stories.html',{'m1':m1,'m2':m2,'newreq':newreq,'acceptedreq':acceptedreq,'no_req':no_req,'reqname':reqname,'accreqname':accreqname})
     else:
          return redirect('signup')
    #return render(request,'social/photo_stories.html',{})

def upload(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)
          m2=img_table.objects.get(uid=asd)


          newreq=notifications.objects.filter(toid=asd,reqstatus='pending')
          r1=[ ]
          for r in newreq:
               s1=r.fromid
               r1.extend([s1])
          reqname=img_table.objects.filter(uid__in=r1)
          
          
          no_req=img_table.objects.filter(uid__in=r1).count()


          acceptedreq=notifications.objects.filter(toid=asd,reqstatus='approved')
          r2=[ ]
          for r in acceptedreq:
               s2=r.fromid
               r2.extend([s2])
          accreqname=img_table.objects.filter(uid__in=r2)



          
          #---------------
          if request.method == 'POST' and request.FILES['f']:
               myfle = request.FILES['f']
               fs = FileSystemStorage()
               data1=request.POST.get('status','')
               data2=datetime.datetime.today()
               data3=m2.img
               data4=m2.fullname
               info=userpost1(status=data1,userid=asd,posttime=data2,img=myfle,profilepic=data3,fullname=data4)
               info.save()
               #---------------------
          return render(request,'social/photo_upload.html',{'m1':m1,'m2':m2,'newreq':newreq,'acceptedreq':acceptedreq,'no_req':no_req,'reqname':reqname,'accreqname':accreqname})
     else:
          return redirect('signup')
    #return render(request,'social/photo_upload.html',{})

def login(request):
    return render(request,'social/login.html',{})



#----------------------------------Profile------------------------
def signup2(request):
     if 'step2id' in request.session:
          asd=request.session['step2id']
          m1=reg.objects.get(pk=asd)
          if request.method == 'POST' and request.FILES['f']:
               myfle = request.FILES['f']
               fs = FileSystemStorage()
               data1=request.POST.get('name','')
               data2=request.POST.get('bio','')
               info=img_table(uid=asd,fullname=data1,bio=data2,img=myfle)
               info.save()
               return redirect('login')
          else:
               return render(request, 'social/signup - 2.html')
     else:
           return render(request, 'social/signup - 2.html')
     
     return render(request, 'social/signup - 2.html')
#-----------------------------------------------Post----------------
def comment(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          m1=reg.objects.get(pk=asd)
          m2=img_table.objects.get(uid=asd)
          if request.method == 'POST':
               data1=request.POST.get('comment','')
               data2=datetime.datetime.today()
               data3=m2.img
               data4=m2.fullname
               data5=request.POST.get('pid','')
               info=comments(cmntrname=data4,cmntrid=asd,comment=data1,cmntrpic=data3,cmntttime=data2,postid=data5)
               info.save()
               f1=comments.objects.filter(postid=data5)
               return redirect('index')
          else:
               return render(request, 'social/signup - 2.html')
     else:
           return render(request, 'social/signup - 2.html')
     
     return render(request, 'social/signup - 2.html')





def img(request):
     if request.method == 'POST' and request.FILES['f']:
          myfle = request.FILES['f']
          fs = FileSystemStorage()
          data1=request.POST.get('nm','')
          data2=request.POST.get('em','')
          data3=request.POST.get('ps','')
          song_obj=img_table(username=data1,email=data2,password=data3,img=myfle)
          song_obj.save()
          #-------------
          ss=img_table.objects.all()
          context={'all_data':ss}
      #----------
          return render(request, 'reviews/fetch img.html',context)
     else:
           return render(request, 'reviews/image form.html')
     return render(request, 'reviews/image form.html')


def sendreq(request,sr):
     if 'username1' in request.session:
          asd=request.session['username1']
          if (notifications.objects.filter(fromid=asd,toid=sr,reqstatus='pending')):
               notifications.objects.filter(fromid=asd,toid=sr,reqstatus='pending').delete()
          #except notifications.DoesNotExist:
          else:               
               status='pending'
               song_obj=notifications(fromid=asd,toid=sr,reqstatus=status)
               song_obj.save()
               return redirect('index')
          
     return redirect('index')
     
def acceptreq(request):
     if 'username1' in request.session:
          asd=request.session['username1']
          if (notifications.objects.filter(toid=asd,reqstatus='pending')):
               notifications.objects.filter(toid=asd,reqstatus='pending').update(reqstatus='approved')
          #except notifications.DoesNotExist:
          else:               
               status='pending'
               song_obj=notifications(fromid=asd,toid=asd,reqstatus=status)
               song_obj.save()
               return redirect('index')
          
     return redirect('index')
