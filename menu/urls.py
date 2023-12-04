from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('menu.cardapio.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
]
