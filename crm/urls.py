"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from users.views import SignupView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

# Other URL confs up here

# Do not import anything for the handler404,
# or whatnot from the django.conf.urls
# Just list them below

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html', email_template_name='auth/password_reset_email.html', subject_template_name='auth/password_reset_subject.txt'), name='password-reset'),
    url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),  name='password_reset_confirm'),
    url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='auth/password_change.html'),
    name='password_change'),
url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'),
    name='password_change_done'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('leads/',  include('leads.urls', namespace="leads")),
    path('categories/', include('categories.urls', namespace="categories")),
    path('sources/',  include('sources.urls', namespace="sources")),
    path('users/',  include('users.urls', namespace="users")),
    path('csvs/',  include('csvs.urls', namespace="csvs")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
