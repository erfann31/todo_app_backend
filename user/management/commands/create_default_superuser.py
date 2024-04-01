from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Create a default superuser with custom default values'

    def handle(self, *args, **options):
        if not User.objects.filter(email='test@mail.com').exists():
            User.objects.create_superuser('test@mail.com', 'test123')

            self.stdout.write(self.style.SUCCESS('Successfully created default superuser'))
        else:
            self.stdout.write(self.style.SUCCESS('Default superuser already exists'))
