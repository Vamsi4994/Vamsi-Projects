"""
URL configuration for ojp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_users import views as v1
from app_jobs import views as v2
from app_jobs_status import views as v3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.Home,name="Home"), #landing page of server
    path('Signup/',v1.Signup,name="Signup"),
    path('register_user/',v1.register_user,name='register_user'),
    path('Signupsucess/',v2.Signupsucess,name="Signupsucess"),
    path('Signuperror/',v2.Signuperror,name="Signuperror.html"),
    path('Login/',v1.Login,name="Login"),
    path('login_user/',v1.login_user,name="login_user"),
    path('Dashboard/', v1.Dashboard, name='Dashboard'),
    path('logout_user/',v1.logout_user,name="logout_user"),
    path('Aboutus/',v1.Aboutus,name="Aboutus"),
    path('Contactus/',v1.Contactus,name="Contactus"),
    path('Seachjobs/',v2.Searchjobs,name="Searchjobs"),
    path('seach_jobs/',v2.search_jobs,name="search_jobs"),
]
