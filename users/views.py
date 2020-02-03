from django.shortcuts import render

from blog.models import PostPage
from users.models import User


def user_profile(request, username):
    user = User.objects.get(username=username)

    posts = PostPage.objects.live().filter(owner=user)

    return render(request, 'users/userprofile_page.html',
                  {'user': user, 'username': username, 'posts': posts})
