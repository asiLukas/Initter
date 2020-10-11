from django.urls import path
from .views import index_view, list_view, create_view, update_view, delete_view
app_name = 'post'

urlpatterns = [
    path('p/<int:id>/', index_view, name='detail'),
    path('', list_view),
    path('create/', create_view),
    path('p/<int:id>/delete/', delete_view),
    path('p/<int:id>/update/', update_view),
]