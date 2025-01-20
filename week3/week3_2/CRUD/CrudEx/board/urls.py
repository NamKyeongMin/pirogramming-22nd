from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    # create
    path('create', board_create, name='board_create'),
    # detail
    path('detail/<int:pk>', board_detail, name="board_detail"),
    # 글 목록
    path('list', board_list, name='board_list'),
    # update
    path('update/<int:pk>', board_update, name='board_update'),
    # delete
    path('delete/<int:pk>', board_delete, name='board_delete'),
]