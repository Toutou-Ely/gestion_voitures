from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from voitures import views
from django.views.decorators.http import require_GET

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voitures.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

