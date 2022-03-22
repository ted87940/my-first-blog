"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


#import sys
#sys.path.insert(0, '..')
#from pathlib import Path
#import sys
#path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
#sys.path.insert(0, path)
#from ..blog.views import CustomLoginView  
#from ..blog.forms import LoginForm
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #old version
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/list'), name='logout'),
    path('', include('blog.urls')),
    #path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='blog/login.html',
    #                                      authentication_form=LoginForm), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]