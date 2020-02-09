from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    RecipeListView,
    RecipeDetailView,
)


app_name='recipe'
urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    # path('about', views.about, name='about'),
]

# if settings.DEBUG:
#     urlspatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlspatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
