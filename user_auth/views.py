from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm, LoginForm
from .models import Users

# Create your views here.
def login(request):
    if request.method == 'POST':
        body = request.POST
        form = LoginForm(body)
        if not form.is_valid():
            return render(request, 'login.html', {"form": LoginForm})

        email = body['email']
        password = body['password']
        try:
            user = Users.objects.get(Q(user_name=email) | Q(email=email))
        except ObjectDoesNotExist:
            return render(request, 'login.html', {"form": LoginForm})

        is_password = check_password(password, user.hashed_password)
        if is_password:
            return redirect('/welcome')

    return render(request, 'login.html', {"form": LoginForm})

def sign_up(request):
    if request.method == 'POST':
        body = request.POST
        form = UserForm(body)
        if not form.is_valid():
            return render(request, 'sign_up.html', {"form": form})

        user = Users.objects.create(
            user_name = body['user_name'],
            age = body["age"],
            email = body["email"],
        )
        user.hashed_password = make_password(body["password"], hasher='bcrypt_sha256')
        user.save()
        return redirect("/login")
    return render(request, 'sign_up.html', {"form": UserForm})


def main_page(request):
    return render(request, 'welcome.html')