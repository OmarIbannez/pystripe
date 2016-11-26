from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from users.models import User
from users.forms import UserRegisterForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username.lower(), password=password)

        if not user:
            return redirect(settings.LOGIN_URL)

        if not user.is_active:
            return redirect(settings.LOGIN_URL)

        login(request, user)

        if request.POST.get('next', None):
            return redirect(request.POST['next'])

        return redirect(settings.LOGIN_REDIRECT_URL)

    context = {}
    if request.GET.get('next', None):
        context['next'] = request.GET['next']

    return render(request, 'auth/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)


def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            form.cleaned_data['username'] = form.cleaned_data['username'].lower()

            new_user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                username=new_user.username,
                password=form.cleaned_data['password']
            )

            login(request, user)
            return redirect('/add_credit_card/')

    return render(request, 'register.html', {'form': form})
