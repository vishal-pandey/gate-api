from django.contrib import admin

from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
	model = Visitor
	list_display = ["id","visit_date","card_number","name","address","mobile","number_plate","destination","purpose","intime","outtime"]

# Register your models here.
admin.site.register(Visitor, VisitorAdmin)