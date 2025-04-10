from django.contrib import admin
from website.models import contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'created_date', 'email',)
    list_filter = ('name',)


admin.site.register(contact,ContactAdmin)
