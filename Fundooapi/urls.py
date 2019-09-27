from django.conf.urls import include
from . import views
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Django API')
# from rest_framework.documentation import include_docs_urls
# app_name = 'Fundooapi'
urlpatterns = [
    path('', views.reg, name='reg'),
    path('forget_view', views.forget_vw, name='forget_vw'),
    path('login_view/', views.login_view, name='log_view'),
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('activate/<token>/', views.activate, name='activate'),
    path('delete', views.delete, name='delete'),
    path('forget', views.forget, name='forget'),
    path('reset/<token>/', views.reset, name='reset'),
    path('delete_vw/', views.delete_vw, name='delete_vw'),
    path('logout', views.logout, name='logout'),
    path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('upload', views.upload, name='upload'),
    path('home/', views.home, name='home')
    # path('user_list', views.user_list, name='user_list'),
]
