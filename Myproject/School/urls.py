from django.urls import path
from School import views


urlpatterns = [
    path('', views.home, name='home'),
    path('update_shoe/<int:id>/', views.update_shoe, name='update_shoe'), 
    path('delete_shoe/<int:id>/', views.delete_shoe, name='delete_shoe')
]
