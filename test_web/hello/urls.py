from django.url import path
from . import views

urlpatterns=[
    path('users',views.show,name="users"),
]