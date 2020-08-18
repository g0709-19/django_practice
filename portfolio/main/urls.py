from django.urls import path
from .views import index, detail, create, delete

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:post_id>/', delete, name='delete'),
]