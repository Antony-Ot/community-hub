# home/management/commands/populate_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate the database with 10 users with African names'

    def handle(self, *args, **kwargs):
        users = [
            {'username': 'kwame_ama', 'email': 'kwame_ama@example.com', 'password': 'password123'},
            {'username': 'oluwaseun', 'email': 'oluwaseun@example.com', 'password': 'password123'},
            {'username': 'zanele', 'email': 'zanele@example.com', 'password': 'password123'},
            {'username': 'tendai', 'email': 'tendai@example.com', 'password': 'password123'},
            {'username': 'amaka', 'email': 'amaka@example.com', 'password': 'password123'},
            {'username': 'kofi', 'email': 'kofi@example.com', 'password': 'password123'},
            {'username': 'nandi', 'email': 'nandi@example.com', 'password': 'password123'},
            {'username': 'chimwemwe', 'email': 'chimwemwe@example.com', 'password': 'password123'},
            {'username': 'nina', 'email': 'nina@example.com', 'password': 'password123'},
            {'username': 'fola', 'email': 'fola@example.com', 'password': 'password123'},
        ]

        for user_data in users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user_data["username"]} already exists'))
