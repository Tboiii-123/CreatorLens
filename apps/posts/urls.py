from django.urls import path

from .views import (
    create_post,
    get_all_posts,
    post_detail,
    update_post,
    delete_post,
)

urlpatterns = [
    path("", get_all_posts, name="get_all_posts"),
    path("create/", create_post, name="create_post"),
    path("<int:pk>/", post_detail, name="post_detail"),
    path("<int:pk>/update/", update_post, name="update_post"),
    path("<int:post_id>/delete/", delete_post, name="delete_post"),
]