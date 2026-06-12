from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "title",
            "image",
            "content",
            "views",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["id", "user", "views", "created_at", "updated_at"]