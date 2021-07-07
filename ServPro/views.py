from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import service
from math import ceil
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def Home(request):
    return render(request, "Html/index.html")

@login_required(login_url='/')
def ServPage(request):
    Services = service.objects.filter(creater=request.user)
    n = len(Services)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides,'range':range(1,nSlides),'Service':Services}
    return render(request, 'Html/ServPage.html',params)

@login_required(login_url='/')
def ClientPage(request):
    Services = service.objects.all()
    n = len(Services)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides,'range':range(1,nSlides),'Service':Services}
    return render(request, 'Html/ClientPage.html',params)

@login_required(login_url='/')
def ContactUs(request):
    return render(request, "Html/ContactUs.html")

@login_required(login_url='/')
def AddService(request):
    return render(request, "Html/AddService.html")

def handleLogIn(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        User = authenticate(username = login_username, password=login_password)

    if User is not None:
        login(request, User)
        if request.user.is_superuser:
            return redirect("/admin/")
        else:
            if request.user.is_staff:
                return redirect("/ServPage/")
            else:
                return redirect("/ClientPage/")
    else:
        messages.info(request,'Username Or Password is Incorrect')
        return render(request, "Html/index.html")

def handleLogOut(request):
    logout(request)
    return redirect("/")

def Service(request):
        if request.method == 'POST':
            ServiceCreater = request.user
            Service_Name = request.POST.get('Name','')
            Service_Description = request.POST.get('Description','')
            Charges = request.POST.get('Charges','')
            services = service(Service_Name=Service_Name, Service_Description=Service_Description, Charges=Charges, creater=ServiceCreater)
            services.save()
            return redirect("/ServPage/")

def Contact(request):
    if request.method == "POST":
        contact_email = request.POST['Email']
        contact_name = request.POST['Name']
        message = request.POST['Message']
        send_mail(
           'Email From' + contact_name,
            contact_email,
            message,
            ['Service@Contact.com'],
        )
        return redirect("/ClientPage/",{'message':messages})
        messages.success(request,'Email send sucessfully')

    else:
        return redirect("/ClientPage/")
