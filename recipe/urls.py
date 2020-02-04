from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PostListView
from django.contrib.auth.decorators import login_required
from . import views


app_name='recipe'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('test', views.test, name='test')
    # path('about', views.about, name='about'),
]

# if settings.DEBUG:
#     urlspatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlspatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
