from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from recipe import views


urlpatterns = [
   
    path('recipe/', include('recipe.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    # test
    path('test/', views.test, name='test'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)