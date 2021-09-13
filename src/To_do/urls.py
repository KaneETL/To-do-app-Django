
import django
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from todo.views import todo_list
from users import views as v


urlpatterns = [

   
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('homepage/', todo_list),
    path('', v.users, name='users'),
    
     
]
