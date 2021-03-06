from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from User.models import UserProfile
from django.db import IntegrityError
from django.contrib import messages


def comment_adjustment_view(request, id, id2): # id is a comment, id2 is a post
    obj = get_object_or_404(Comment, id=id)
    post = get_object_or_404(Post, id=id2)
    form = CommentForm(request.POST or None, instance=obj)
    context = {'obj': obj, 'post': post}

    if form.is_valid():
        form.save()
        return redirect('/')

    context['form'] = form

    if request.method == 'POST' and 'c_delete' in request.POST:
        obj.delete()
        return redirect('/')

    return render(request, 'posts/comment_adjustment.html', context)


def like_view(request, id):
    post = Post.objects.get(id=id)
    likes = post.post.all()  # Getting all users that liked the post

    context = {
        'likes': likes
    }
    return render(request, 'posts/like_list.html', context)


def detail_view(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    like_count = post.post.filter().values('like').count()  # count number of likes
    likes = post.post.all().filter().values('like')  # users that liked the post

    if {'like': user.id} not in likes:  # if user didn't like the pic, he can, else he can unlike
        like = True
    else:
        like = False

    # like twice exception
    try:
        if like:
            if request.method == 'POST' and 'likeform' in request.POST:
                Like.objects.create(like=request.user, post=post)
                return redirect('/p/%d' % post.id)
        else:
            if request.method == 'POST' and 'likeform' in request.POST:
                Like.objects.filter(like=request.user, post=post).delete()
                return redirect('/p/%d' % post.id)

    except IntegrityError:
        messages.warning(request, 'no')

    form = CommentForm()
    comments = post.c_post.all() # Getting all comments of current post

    if request.method == 'POST' and 'commentform' in request.POST:
        form = CommentForm(request.POST or None)
        form.instance.c_post = post
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('/p/%d' % post.id)

    context = {
        'post': post,
        'like_count': like_count,
        'like': like,
        'form': form,
        'comments': comments,
    }

    return render(request, 'posts/post_index.html', context)


def list_view(request):
    obj = Post.objects.all()
    if request.user.is_authenticated:
        pass
    else:
        return redirect('/login')
    follows = request.user.follow.all()

    context = {
        'obj': obj,
        'follows': follows
    }

    return render(request, 'posts/post_list.html', context)


def all_posts_view(request):
    obj = Post.objects.all()
    follows = request.user.follow.all()

    context = {
        'obj': obj,
        'follows': follows
    }
    return render(request, 'posts/all_posts.html', context)


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
