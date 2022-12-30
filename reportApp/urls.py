from django.urls import path, include
from .views import  index, logout_user, dashboard, report, regenerate, generate

from .apiviews import CustomUserCreate, LoginView, ReportViewSet
from rest_framework.routers import DefaultRouter
from .apiviews import LogoutView

rotuer = DefaultRouter()
rotuer.register(r'report', ReportViewSet)


urlpatterns = [
    path('', index,  name='home'),
    path('logout/', logout_user, name='logout-user'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('report/<int:pk>/', report, name='report'),
    path('regenerate/<int:pk>/', regenerate, name='regenerate'),
    path('generated-report/', generate, name='generate'),
    
    path('api/users/', CustomUserCreate.as_view(), name="user_create"),
    path('api/login/', LoginView.as_view(), name="login"),
    path('api/logout/', LogoutView.as_view(), name='logout' ),

    path('api/', include(rotuer.urls))
]