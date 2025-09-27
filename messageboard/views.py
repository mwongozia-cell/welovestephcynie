from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Media

@login_required
def shoutout_board(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        post = Post.objects.create(name=name, message=message)

        for file in request.FILES.getlist('media'):
            Media.objects.create(post=post, file=file)

        return redirect('shoutout_board')

    posts = Post.objects.order_by('-created_at')
    return render(request, 'shoutout_board.html', {'posts': posts})

@login_required
def shoutout(request):
    return render(request, 'messageboard/shoutout.html')

