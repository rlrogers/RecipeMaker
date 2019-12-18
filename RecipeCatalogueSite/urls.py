from django.contrib import admin
from django.urls import include, path
from .views import index, base

urlpatterns = [
    path('recipe/', include('recipe.urls')),
    path('base/', include('base.urls')),
    path('admin/', admin.site.urls),
    path('', index),

]
