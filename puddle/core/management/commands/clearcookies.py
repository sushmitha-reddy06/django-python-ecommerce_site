# core/management/commands/clearcookies.py

from django.core.management.base import BaseCommand
from django.http import HttpResponse

class Command(BaseCommand):
    help = 'Clears all cookies'

    def handle(self, *args, **options):
        response = HttpResponse()
        response.delete_cookie('sessionid')
        self.stdout.write(self.style.SUCCESS('All cookies cleared successfully'))
