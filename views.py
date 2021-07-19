from django.shortcuts import render,redirect
from .models import AddNews
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    return render(request,'index.html')

def alogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user= auth.authenticate(username=username,password=password)

        if user is not None and user.is_staff :
            auth.login(request,user)
            return redirect('insert')
        elif user is not None and not user.is_staff :    
            messages.error(request,'You are not Authorized to access Employer Login')    
            return redirect('alogin')
    
        else:
            messages.error(request,'Invalid Credentials')    
            return redirect('alogin')


    else:
        return render(request,'alogin.html')
            


def insert(request):
    

    if request.method == 'POST':

        date=request.POST['date']
        title=request.POST['title']
        description=request.POST['description']
        url=request.POST['url']
                    
        AN= AddNews.objects.create(date=date, title=title, description=description, url=url)
        AN.save()
        print('Data Saved')
        messages.info(request,'Thank you, You have successfully added a News !!!')      
        return redirect('insert')
    
    else:
        return render(request,'insert.html')
   


