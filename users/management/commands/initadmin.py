from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Creates a superuser if it does not exist'

    def handle(self, *args, **options):
        email = 'admin@rxreuse.in'
        password = 'Admin@2025'
        
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser created: {email}'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
