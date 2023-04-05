from django.contrib import admin
from  . import views
from django.urls import path

app_name ='food'

urlpatterns =[
    
   #/food/
    path('',views.index, name='index'),

    #food/1
    path('<int:item_id>/', views.detail, name='detail'),
    
    #add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    
    #update
    path('update/<int:id>',views.update_item, name='update_item'),
    
    #Delete  item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
