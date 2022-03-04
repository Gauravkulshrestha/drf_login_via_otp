from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_otp/', send_otp), 
    path('verify_otp/', verify_otp),        
]