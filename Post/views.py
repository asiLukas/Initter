from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import User


def index_view(request, id):
    obj = Post.objects.get(id=id)
    context = {
        'obj': obj,

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
