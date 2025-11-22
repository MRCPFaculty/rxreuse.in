import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rxreuse.settings')
django.setup()

from users.models import User

if not User.objects.filter(email='admin@rxreuse.org').exists():
    User.objects.create_superuser('admin@rxreuse.org', 'admin123')
    print('Superuser created: admin@rxreuse.org / admin123')
else:
    print('Superuser already exists')
