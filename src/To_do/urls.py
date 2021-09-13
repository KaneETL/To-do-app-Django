
import django
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from todo.views import todo_list
from todo.views import homeview
from users import views as v


urlpatterns = [

   
    path('', include("django.contrib.auth.urls")),
    path('homepage/', homeview.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('todos/', todo_list),
    path('', v.users, name='users'),
    
     
]
