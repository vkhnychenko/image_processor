from django.urls import path
from .views import ImageDetailView, ImageCreateView, ImageListView

app_name = 'main'

urlpatterns = [
    path('', ImageListView.as_view(), name='index'),
    path('create-image', ImageCreateView.as_view(), name='create_image'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
]
