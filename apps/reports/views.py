from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import AnalyticsReport






@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_reports(request):

    reports = AnalyticsReport.objects.filter(user=request.user).order_by("-created_at")

    return Response({
        
        "message":"Report Sent successfully",
    
    "data":[
        {
            "type": r.report_type,
            "views": r.total_views,
            "posts": r.total_posts,
            "top_post_id": r.top_post_id,
            "created_at": r.created_at
        }
        for r in reports
    ]
    },status=status.HTTP_200_OK)
