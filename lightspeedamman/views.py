from django.shortcuts import render, get_object_or_404, redirect
from .forms import TestDriveForm, CarConfigurationForm, RegisterForm, LoginForm
from django.http import JsonResponse

from django.contrib.auth import login


def index(request):
    return render(request, 'pages/index.html')


def about_us(request):
    return render(request, 'pages/about_us.html')


def contact(request):
    return render(request, 'pages/contact.html')


def book_test_drive(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'pages/book_test_drive.html',
                {'form': TestDriveForm(), 'success': True}
            )
    else:
        form = TestDriveForm()

    return render(request, 'pages/book_test_drive.html', {'form': form})


def configure(request, model=None):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'login_required'}, status=401)

        form = CarConfigurationForm(request.POST, selected_model=model)
        if form.is_valid():
            config = form.save(commit=False)
            config.user = request.user
            config.car_model = model
            config.save()
            return JsonResponse({'success': True})

    else:
        form = CarConfigurationForm(selected_model=model)

    return render(request, 'pages/configure.html', {
        'form': form,
        'car_model': model
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log the user in
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
