from django.shortcuts import render

from blog.models import PostPage
from users.models import User


def user_profile(request, username):
    user = User.objects.filter(username=username)
    for field in user:
        about = field.about
        first_name = field.first_name
        last_name = field.last_name
        username = field.username

        posts = PostPage.objects.live().filter(owner=request.user)

    return render(request, 'users/userprofile_page.html',
                  {'user': user, 'about': about, 'last_name': last_name, 'first_name': first_name,
                   'username': username, 'posts': posts})
