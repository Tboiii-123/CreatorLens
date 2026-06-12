import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from apps.posts.models import Post  # change to your model

FAKE_TITLES = [
    "The Power of Faith", "Morning Reflections", "Finding Peace Within",
    "Journey to Truth", "Blessings in Disguise", "Light in Darkness",
    "Words of Wisdom", "Daily Gratitude", "Path of Righteousness",
    "Moments of Grace", "Sacred Thoughts", "Inner Strength",
    "Hope Renewed", "Divine Mercy", "Walking in Faith",
]

FAKE_CONTENT = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.",
    "Alhamdulillah for every blessing. Life is a journey filled with lessons and growth every single day.",
    "Every morning is a new beginning. Embrace it with gratitude and a heart full of hope and purpose.",
    "Subhanallah, the beauty of this world reminds us of the greatness of the Creator above all things.",
    "Faith moves mountains. Trust the process and believe that everything happens for a greater reason.",
    "In the midst of chaos, find your calm. Breathe, reflect, and remember what truly matters most.",
    "Kindness is a language the deaf can hear and the blind can see. Spread it everywhere you go.",
    "The strongest among us are those who remain patient in times of trial and grateful in times of ease.",
    "Never underestimate the power of a sincere prayer. It can change what seems impossible into possible.",
    "Life is short. Make it meaningful by doing good, being kind, and leaving the world better than you found it.",
]

IMAGE_URL = "https://res.cloudinary.com/dugjy3sff/image/upload/v1781202713/qjoqcivkbk3slobjlfzj.jpg"

class Command(BaseCommand):
    help = 'Seed 100 fake posts'

    def handle(self, *args, **kwargs):
        # Post.objects.all().delete()  # optional: clear existing
        
        posts = []
        now = timezone.now()

        for i in range(100):
            created_at = now - timedelta(days=random.randint(1, 365))
            updated_at = created_at + timedelta(
                hours=random.randint(1, 72)
            )

            posts.append(Post(
                user_id=random.randint(1, 3),
                title=random.choice(FAKE_TITLES) + f" #{i+1}",
                image=IMAGE_URL,
                content=random.choice(FAKE_CONTENT),
                views=0,
                created_at=created_at,
                updated_at=updated_at,
            ))

        Post.objects.bulk_create(posts)
        self.stdout.write(self.style.SUCCESS('✅ 100 fake posts created!'))