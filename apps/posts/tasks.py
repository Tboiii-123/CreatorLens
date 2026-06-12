from celery import shared_task
from django.db import transaction
from .models import Post
from config.redis import redis_client
from django.db.models import F


@shared_task
def sync_post_views():
    print("🔥 TASK STARTED")

    #  STEP 1: GET ALL VIEW KEYS
    keys = redis_client.keys("post:*:views")

    #  STEP 2: IF NOTHING TO SYNC → EXIT EARLY
    if not keys:
        return "No views to sync - skipped"

    updates = []

    # STEP 3: COLLECT DATA FROM REDIS
    for key in keys:
        try:
            post_id = key.split(":")[1]
            views = int(redis_client.get(key) or 0)

            updates.append((post_id, views))

        except Exception:
            continue

    #  STEP 4: BULK UPDATE DB (SAFE TRANSACTION)
    with transaction.atomic():
      for post_id, views in updates:
         Post.objects.filter(id=post_id).update(
            views=F("views") + views
        )
            

    #  STEP 5: CLEAR REDIS AFTER SYNC
    redis_client.delete(*keys)

    return f"Synced {len(updates)} posts"