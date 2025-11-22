import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rxreuse.settings')
django.setup()

from users.models import User

if not User.objects.filter(email='admin@rxreuse.in').exists():
    User.objects.create_superuser('admin@rxreuse.in', 'Admin@2025')
    print('Superuser created: admin@rxreuse.in / Admin@2025')
else:
    print('Superuser already exists')
