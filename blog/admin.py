from django.contrib import admin
from blog.models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title', 'published_date', 'status',)
    list_display = ('title', 'author', 'status',
                    'created_date', 'counted_view')
    list_filter = ('status', 'author', 'category')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
