from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'subject', 'created_at')
  list_filter = ('status',)

admin.site.register(Contact, ContactAdmin)