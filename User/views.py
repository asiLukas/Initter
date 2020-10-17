from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth.forms import User
from Post.models import Post
from .models import UserProfile, Following
from django.db import IntegrityError
from django.contrib import messages


def register_view(request):
    form = RegisterForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None, request.FILES or None)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('/login')
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'registration/register.html', context)


def register_update_view(request, username):
    usr = get_object_or_404(User, username=username)
    context = {}
    form = RegisterForm(request.POST or None, request.FILES or None, instance=usr)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['form'] = form
    context['usr'] = usr

    return render(request, 'user/register_update.html', context)


def profile_update_view(request, user):
    usr = get_object_or_404(UserProfile, user=user)
    context = {}
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=usr)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['form'] = form
    context['usr'] = usr

    return render(request, 'user/profile_update.html', context)


def search_view(request):
    obj = User.objects.all()
    context = {
        'user': obj
    }
    return render(request, 'user/search.html', context)


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    current_user = request.user
    post = Post.objects.all()
    followers = user.follower.filter().values('follower').count()
    follows = user.follow.filter().values('follow').count()
    follower_list = current_user.follow.all().filter().values('follower')

    if {'follower': user.id} not in follower_list:
        follow = True
    else:
        follow = False

    try:
        if follow:
            if request.method == 'POST':
                Following.objects.create(follower=user, follow=current_user)
                return redirect('/profile/%s' % user)
        else:
            if request.method == 'POST':
                Following.objects.filter(follow=current_user, follower=user).delete()
                return redirect('/profile/%s' % user)

    except IntegrityError:
        messages.warning(
            request,
            'someone tried to follow twice'
        )

    context = {
        'profile_user': user,
        'post': post,
        'follow': follow,
        'followers': followers,
        'follows': follows,
    }
    return render(request, 'user/profile.html', context)


def followers_list_view(request, username):
    usr = get_object_or_404(User, username=username)
    obj = usr.follower.all()
    context = {
        'obj': obj,
        'usr': usr
    }

    return render(request, 'follow/followers_list.html', context)


def follows_list_view(request, username):
    usr = get_object_or_404(User, username=username)
    obj = usr.follow.all()
    context = {
        'obj': obj,
        'usr': usr
    }

    return render(request, 'follow/follows_list.html', context)
