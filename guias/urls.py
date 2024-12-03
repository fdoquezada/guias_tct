from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_guia, name='crear_guia'),
    path('listar/', views.listar_guias, name='listar_guias'),
    path('logout/', views.logout_view, name='logout'),
]

