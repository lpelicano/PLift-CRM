from django.core.management.base import BaseCommand
from Lfit.models import PersonalInfo

class Command(BaseCommand):
    def handle(self, *args, **options):
        PersonalInfo.objects.all().delete()
