from django.urls import path
from .views import register_view, profile_view, base_profile_view, register_update_view, profile_detail_update_view, \
    followers_list_view, follows_list_view
app_name = 'login'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('profile/<username>', profile_view, name='user_profile'),
    path('profile/', base_profile_view, name='base_profile'),
    path('profile/<username>/register_update', register_update_view),
    path('profile/<user>/update', profile_detail_update_view),
    path('profile/<username>/followers', followers_list_view),
    path('profile/<username>/follows', follows_list_view)
]