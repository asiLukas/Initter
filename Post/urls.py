from django.urls import path
from .views import detail_view, list_view, create_view, update_view, delete_view, like_view, comment_adjustment
app_name = 'post'

urlpatterns = [
    path('p/<int:id>/', detail_view, name='detail'),
    path('', list_view),
    path('create/', create_view),
    path('p/<int:id>/delete/', delete_view),
    path('p/<int:id>/update/', update_view),
    path('p/<int:id>/like', like_view),
    path('c/<int:id>/<int:id2>', comment_adjustment)
]