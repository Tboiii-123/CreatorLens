from celery import shared_task
from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone
from .models import  AnalyticsReport
from apps.posts.models import Post
from apps.account.models import User


@shared_task
def generate_weekly_reports():

    users = User.objects.all()

    for user in users:

        posts = Post.objects.filter(user=user)

        total_views = posts.aggregate(Sum("views"))["views__sum"] or 0
        total_posts = posts.count()
        top_post = posts.order_by("-views").first()

        AnalyticsReport.objects.update_or_create(
         user=user,
        report_type="weekly",
        defaults={
        "total_views": total_views,
        "total_posts": total_posts,
        "top_post_id": top_post.id if top_post else None
    }
)