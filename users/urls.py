from django.urls import path

from users.views import user_profile

app_name = 'users'

urlpatterns = [
    path('<username>/', user_profile, name='user_profile'),
]
