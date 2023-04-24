from django.shortcuts import render, redirect
from .models import users

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_num = request.POST.get('phone_num')
        message = request.POST.get('message')
        print(request.POST)

        new_user = users(name=name, email=email, phone_num=phone_num, message=message)
        new_user.save()
        print("saved succussfully")

        return redirect('index')

    return render(request, 'index.html')



# def savecred(request):
#     name = ''
#     email = ''
#     phone_number = ''
#     message = ''
#     if request.method == 'POST':
#         pass
