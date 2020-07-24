from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
#     path('new', views.index),
     path('register', views.register),
     path('success', views.success),
     path('login', views.login),
     path('logout', views.logout),

#     path('<int:show_id>/update', views.update),
#     path('<int:show_id>/destroy', views.destroy),

]