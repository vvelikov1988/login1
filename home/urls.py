from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
#     path('new', views.index),
#     path('create', views.create),
#     path('<int:show_id>', views.showdetails),
#     path('<int:show_id>/edit', views.editshow),
#     path('<int:show_id>/update', views.update),
#     path('<int:show_id>/destroy', views.destroy),

]