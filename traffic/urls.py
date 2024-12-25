"""
URL configuration for traffic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore
from . import views  # type: ignore
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('predict/', views.upload_and_predict, name='predict'),
    path('signup_login/', views.signup_login, name='signup_login'),
    path('sample/',views.sample, name='sample'),
    path('sample_index/', views.index1, name='index1'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
