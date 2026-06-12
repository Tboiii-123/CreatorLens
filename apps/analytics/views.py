from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes

from apps.posts.models import Post

from config.redis import redis_client



def get_performance_label(views):
    if views < 20:
        return "low"
    elif views < 1000:
        return "medium"
    else:
        return "high"

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):

    user = request.user

    posts = Post.objects.filter(user=user)

    total_views = sum(p.views for p in posts)

    top_post = posts.order_by("-views").first()

    return Response({
        "total_views": total_views,
        "post_count": posts.count(),
        "top_post": {
            "id": top_post.id if top_post else None,
            "title": top_post.title if top_post else None,
            "views": top_post.views if top_post else 0,
            
        },
            "performance": get_performance_label(total_views)
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_analytics(request, pk):

    post = get_object_or_404(Post, id=pk)

    return Response({
        "post_id": post.id,
        "views": post.views
    })