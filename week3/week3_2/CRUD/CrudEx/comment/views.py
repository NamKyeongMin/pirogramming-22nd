from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Comment, Board

def comment_create(request, pk):
    if request.method == 'POST':
        findBoard = Board.objects.get(id=pk)
        Comment.objects.create(
            board = findBoard,
            content = request.POST['content']
        )
        return redirect('board:board_detail', pk=findBoard.id)
    
def comment_delete(request, pk):
    if request.method == 'POST':
        findComment = Comment.objects.get(id=pk)
        board_pk = findComment.board.id
        findComment.delete()
        return redirect('board:board_detail', pk=board_pk)