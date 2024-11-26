from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        body = request.POST
        form = UserForm(body)
        if not form.is_valid():
            return render(request,'sign_up.html', {"form": form})

        user = Users.objects.create(
            user_name = body['user_name'],
            age = body["age"],
            email = body["email"],
        )
        user.hashed_password = make_password(body["password"], hasher='bcrypt_sha256')
        user.save()
        return redirect("/login")
    return render(request, 'sign_up.html', {"form": UserForm})
