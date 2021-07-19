from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from adint.models import AddNews
import wikipedia
import webbrowser
from googlesearch import search

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')    
            return redirect('login')


    else:
        return render(request,'login.html')
            


def register(request):
    
    if request.method == 'POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email =request.POST['email']

        
        if User.objects.filter(username = username).exists():
            messages.info(request,'User Already Exists!!!!')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request,'Email Id Already Exists!!!!')            
            return redirect('register')
        elif password1==password2:                
            user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.save()
            print('User Created')
            return redirect('login')
        elif password1!=password2:
            messages.info(request,'Password Not Matching!!!!')        
            return redirect('register')
        return redirect('home')
        

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def test(request):   
    ins=AddNews.objects.all()
    news1 = request.POST['news']
    if AddNews.objects.filter(title = news1).exists() or AddNews.objects.filter(description = news1).exists():
        # x=AddNews.objects.get(id=1)
        
        return render(request, 'result.html',{'name1':news1,'msg':'The News is Real','ins':ins})
    else:
        res = wikipedia.summary(news1, sentences=10)
        gle= search(news1,tld='com',lang='en',num=1,stop=1,pause=2.0)
        for i in gle:
            x=i
        return render(request, 'result.html',{'name1':news1,'msg':'The News is Fake','wiki':res,'google':x})
