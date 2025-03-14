from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', idea_list, name='idea_list'),
    path('detail/<int:pk>/', idea_detail, name="idea_detail"),
    path('create/', idea_create, name="idea_create"),
    path('delete/<int:pk>/', idea_delete, name="idea_delete"),
    path('update/<int:pk>/', idea_update, name="idea_update"),
    path('update_like/', update_like, name='update_like'),
    path('update_interest/<int:idea_id>/', update_interest, name="update_interest"),
]
