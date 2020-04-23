from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "data_pubblicazione", "author", "publish")
    search_fields = ("title", "text")
    list_filter = ("publish", "author")
    date_hierarchy = "data_pubblicazione"