from django.db import models
from django.db import models
from apps.account.models import User
# Create your models here.
class AnalyticsReport(models.Model):

    REPORT_TYPE = [
        ("daily", "Daily"),
        ("weekly", "Weekly"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=10, choices=REPORT_TYPE)

    total_views = models.BigIntegerField(default=0)
    total_posts = models.IntegerField(default=0)
    top_post_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)