from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes

from .models import Post
from .serializers import PostSerializer
from config.redis import redis_client


# Content-Type: multipart/form-data

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response({
             "message": "Post created successfully",
            "data":serializer.data},status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_posts(request):

    posts = Post.objects.select_related("user").order_by("created_at")
    

    paginator = PageNumberPagination()
    paginator.page_size = 10

    paginated_queryset = paginator.paginate_queryset(posts,request)

    serializer = PostSerializer(paginated_queryset,many=True)

    return paginator.get_paginated_response(serializer.data)


from config.redis import redis_client

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)

    #  INCREMENT CLOUD REDIS
    redis_client.incr(f"post:{post.id}:views")

    views = redis_client.get(f"post:{post.id}:views") or 0

    data = PostSerializer(post).data
    data["views"] = int(views)

    return Response(data,status=status.HTTP_200_OK)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_post(request, pk):

    post = get_object_or_404(Post, id=pk, user=request.user)

    if post.user != request.user:
        return Response(
            {
                "error": "You are not allowed to delete this post."
            },
            status=status.HTTP_403_FORBIDDEN
        )

    serializer = PostSerializer(post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if post.user != request.user:
        return Response(
            {
                "error": "You are not allowed to delete this post."
            },
            status=status.HTTP_403_FORBIDDEN
        )

    post.delete()

    return Response(
        {
            "message": "Post deleted successfully"
        },
        status=status.HTTP_200_OK
    )