from django.urls import path
from .views import *

app_name = 'comment'

urlpatterns = [
    # comment create
    path('comment/<int:pk>/create', comment_create, name="comment_create" ),
    # comment delete
    path('comment/<int:pk>', comment_delete, name="comment_delete" ),
]