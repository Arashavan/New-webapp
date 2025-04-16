from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title', 'published_date', 'status',)
    list_display = ('title', 'status', 'created_date', 'counted_views')
    list_filter = ('status',)


admin.site.register(Post, PostAdmin)
