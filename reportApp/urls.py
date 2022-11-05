from django.urls import path
from .views import  index, logout_user, dashboard, report, regenerate, generate


urlpatterns = [
    path('', index,  name='home'),
    path('logout/', logout_user, name='logout-user'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('report/<int:pk>/', report, name='report'),
    path('regenerate/<int:pk>/', regenerate, name='regenerate'),
    path('generated-report/', generate, name='generate'),
]
