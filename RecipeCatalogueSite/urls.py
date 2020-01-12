from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from users import views as user_views  
from recipe import views
from recipe.views import product_detail_view, product_create_view, dynamic_lookup_view


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),   
    path('recipe/', include('recipe.urls')),
    path('', views.home_view, name='home'),
    # test
    path('test/', views.test, name='test'),
    # path('initial/', render_initial_data),
    path('create/', product_create_view),
    path('product/', product_detail_view),
    path('recipe/<int:id>/', dynamic_lookup_view, name='recipe'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
