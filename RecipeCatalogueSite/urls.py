from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views
# below, please add 'as recipe_views' in a cruch atm  
from recipe import views
from recipe.views import product_detail_view, product_create_view, dynamic_lookup_view


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),   
    path('profile', user_views.profile, name='profile'),   
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),   
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
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
