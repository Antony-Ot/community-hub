# home/management/commands/populate_visits.py

import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import PageVisit
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate PageVisit model with random data'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        pages = ['/', '/dashboard/', '/register/', '/login/', '/logout/']
        
        for _ in range(50):  # Generate 50 random visits
            user = random.choice(users)
            page = random.choice(pages)
            visit_time = timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            PageVisit.objects.create(user=user, page=page, visit_time=visit_time)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated PageVisit model with random data'))
