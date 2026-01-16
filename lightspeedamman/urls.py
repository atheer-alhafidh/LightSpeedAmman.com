from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('book-test-drive/', views.book_test_drive, name='book_test_drive'),
    path('configure/', views.configure, name='configure'),
    path('configure/<str:model>/', views.configure, name='configure'),
    path("login/", auth_views.LoginView.as_view(
        template_name="login.html",
        redirect_authenticated_user=True
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register')
]
