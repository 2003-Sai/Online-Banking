"""
URL configuration for onlinebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from services import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("adminlogin/", views.adminlogin),
    path("AdminLoginDB/", views.AdminLoginDB),
    path("logout/", views.logout),
    path("employlogin/", views.employlogin),
    path("EmployLoginDB/", views.EmployLoginDB),
    path("customerlogin/", views.customerlogin),
    path("CustomerloginDB/", views.CustomerloginDB),
    path("viewemploy/", views.viewemploy),
    path("ViewCustomer/", views.ViewCustomer),
    path("addemploy/", views.addemploy),
    path("addemployDB/", views.addemployDB),
    path("addCustomer/", views.addcustomer),
    path("addcustomerDB/", views.addcustomerDB),
    path("edit/", views.edit),
    path("UpdateEmployDB/", views.UpdateEmployDB),
    path("deleteEmploy/", views.deleteEmploy),
    path("deposit/", views.deposit),
    path("depositDB/", views.depositDB),
    path("withdrawl/", views.withdrawl),
    path("withdrawlDB/", views.withdrawlDB),
    path("Transfer/", views.transfer),
    path("transferDB/", views.transferDB),
    path("ViewProfile/", views.ViewProfile),

    
    

]
