from django.core.management.base import BaseCommand, CommandError

from smaller.models import smallurl

class Command(BaseCommand):
	help='refresher'
	
	def add_arguments(self,parser):
		parser.add_argument('items',type = int)

	def handle(self,*args,**options):
		
		return smallurl.objects.refresh(items=options['items']) 