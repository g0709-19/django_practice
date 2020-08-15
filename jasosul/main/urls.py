from django.contrib import admin
from django.urls import path
from .views import index, create, detail, update, delete, my_index, create_comment, delete_comment

urlpatterns = [
    path('', index, name='index'),
    path('my_index/', my_index, name='my_index'),
    path('create/', create, name='create'),
    path('detail/<int:post_id>', detail, name='detail'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),
    
    # comment
    path('create_comment/<int:jss_id>', create_comment, name="create_comment"),
    path('delete_comment/<int:jss_id>/<int:comment_id>', delete_comment, name="delete_comment"),
]
