from django.contrib import admin
from .models import Post

# registering Post model in the admin page
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author', 'created', 'status',)
    list_filter = ('title', 'status', 'publish', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)
