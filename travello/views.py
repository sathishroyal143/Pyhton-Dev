from django.shortcuts import render, redirect
from .models import Destination
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def home (request):

    dest1 = Destination()
    dest1.name = 'kolkata'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 700
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = False

    dests = [dest1, dest2, dest3 ]

    return render(request, "home.html", {'dests': dests})




def home_view(request):
    return render(request,"home.html")



def register_view(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
             
             if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register_view')

             elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register_view')

             else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print('user created')
                return redirect("login_view")
        else:
            messages.info(request,'password not matching')
            return redirect('register_view')
        return redirect('/')

    else:
        return render(request,"register.html")




def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password= password)

        if  user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login_view')
            

    else:
        return render(request, "login.html")
    
def logout_view(request):
    auth.logout(request)
    return redirect('/')

