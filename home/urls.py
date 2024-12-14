from django.urls import path 
from . import views

urlpatterns=[
  path('', views.save_task,name='save_task'),
  path('save_task/',views.save_task,name='save_task'),
  path('index/',views.index,name='index'),
  path('Delete/<int:id>', views.delete_task, name='delete_task')
]