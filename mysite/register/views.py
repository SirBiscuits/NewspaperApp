from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})


# def edit(request, user):
#     if request.method == "POST":
#         dob = request.POST.get('dob')
#         print(dob)
#         print(user)
#         UserProfile.objects.filter(email=user).update(dob = dob)
#         return render(request, 'register/edit.html')
#     else:
#         return render(request, 'profile.html')

# def upload(request):
#     if request.method == 'POST':
#         upfile = request.FILES['picture']
#         fs = FileSystemStorage()
#         fs.save(upfile.name, upfile)
#     return render(request, 'account.html')