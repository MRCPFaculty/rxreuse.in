from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = 'rxreuse@gmail.com'
        password = 'RxReuse@2025'
        
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password=password,
                role='ADMIN'
            )
            self.stdout.write(self.style.SUCCESS(f'Admin user created: {email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin user already exists: {email}'))
