from django.urls import path
from napp import views

app_name="napp"

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name="register"),

]