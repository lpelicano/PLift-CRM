from django.core.management.base import BaseCommand
from Lfit.models import PersonalInfo, CompResults, Payments, CycleCreate

class Command(BaseCommand):
    def handle(self, *args, **options):
        PersonalInfo.objects.all().delete()
        CompResults.objects.all().delete()
        Payments.objects.all().delete()
        CycleCreate.objects.all().delete()

