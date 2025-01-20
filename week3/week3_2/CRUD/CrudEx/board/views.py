from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Board
from comment.models import Comment

def board_create(request):
    if request.method == 'POST':
        board = Board.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect(reverse('board:board_detail', args=[board.pk]))
    return render(request, 'board/create.html')

def board_detail(request, pk):
    boards = Board.objects.get(id=pk)
    comments = Comment.objects.filter(board=boards) # get-1개만 찾음, filter-여러 개를 찾음
    context = {
        'board': boards,
        'comment': comments
    } # 넘겨야 할 데이터가 많아질 수 있기 때문에
    return render(request, 'board/read.html', context)

def board_list(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/list.html', context)

def board_update(request, pk):
    board = Board.objects.get(id=pk)
    
    if request.method == 'POST':
        title2 = request.POST.get('title')
        content2 = request.POST.get('content')
        board.title = title2
        board.content = content2
        board.save()
        return redirect('board:board_detail', pk=board.pk)
    
    context = {
        'board': board
    }
    return render(request, 'board/update.html', context)

def board_delete(request, pk):
    if request.method == "POST":
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('board:board_list')
    return redirect('home:main') # 이건 그냥 POST 예외처리