from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from .forms import PostForm
from django.db import IntegrityError
from django.contrib import messages


def like_view(request, id):
    post = Post.objects.get(id=id)
    likes = post.post.all() # Getting all users that liked this post

    context = {
        'likes': likes
    }
    return render(request, 'posts/like_list.html', context)


def detail_view(request, id):
    post = Post.objects.get(id=id)
    like_count = post.post.filter().values('like').count()
    likes = post.post.all().filter().values('like')
    if {'like': request.user.id} not in likes:
        like = True
    else:
        like = False

    try:
        if like:
            if request.method == 'POST':
                Like.objects.create(like=request.user, post=post)
                return redirect('/p/%d' % post.id)
        else:
            if request.method == 'POST':
                Like.objects.filter(like=request.user, post=post).delete()
                return redirect('/p/%d' % post.id)

    except IntegrityError:
        messages.warning(request, 'no')

    context = {
        'post': post,
        'like_count': like_count,
        'like': like
    }

    return render(request, 'posts/post_index.html', context)


def list_view(request):
    obj = Post.objects.all()

    context = {
        'obj': obj,

    }

    return render(request, 'posts/post_list.html', context)


def create_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'posts/post_create.html', context)


def update_view(request, id):
    obj = get_object_or_404(Post, id=id)
    context = {'obj': obj}
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['form'] = form

    return render(request, 'posts/post_update.html', context)


def delete_view(request, id):
    obj = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {
        'obj': obj
    }
    return render(request, 'posts/post_delete.html', context)
