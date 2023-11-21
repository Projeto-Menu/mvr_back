from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('menu.core.urls')),
    path('admin/', admin.site.urls),
]
