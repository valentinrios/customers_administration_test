"""customers_administration_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from customers_admin_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^countries/', views.CountryList.as_view()),
    url(r'^country/(?P<pk>[0-9]+)', views.CountryDetails.as_view()),
    url(r'^country/', views.CountryDetails.as_view()),
    url(r'^customers/', views.CustomerList.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)', views.CustomerDetails.as_view()),
    url(r'^customer/', views.CustomerDetails.as_view()),
    url(r'^sports/', views.SportList.as_view()),    
    url(r'^sport/(?P<pk>[0-9]+)', views.SportDetails.as_view()),
    url(r'^sport/', views.SportDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)