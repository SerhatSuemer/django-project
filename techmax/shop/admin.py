from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Kunde)
admin.site.register(Artikel)
admin.site.register(Bestellung)
admin.site.register(BestellteArtikel)
admin.site.register(Adresse)