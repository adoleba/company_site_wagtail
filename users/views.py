from django.shortcuts import render

from blog.models import PostPage
from users.models import User


def user_profile(request, username):
    user = User.objects.filter(username__iexact=username)
    ctx = {}
    for field in user:
        ctx['about'] = field.about
        ctx['first_name'] = field.first_name
        ctx['last_name'] = field.last_name

    posts = PostPage.objects.live().filter(owner=user[0])

    return render(request, 'users/userprofile_page.html',
                  {'user': user, 'username': username, 'posts': posts, **ctx})
