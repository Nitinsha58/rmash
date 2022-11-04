from django.urls import path
from .views import  index, logout_user, dashboard, report


urlpatterns = [
    path('', index,  name='home'),
    path('logout/', logout_user, name='logout-user'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('report/', report, name='report') 
]    
