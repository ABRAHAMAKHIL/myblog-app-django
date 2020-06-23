from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Key','Status', 'Created_On')
    list_filter = ("Status",)
    search_fields = ['Title', 'Content']
    prepopulated_fields = {'Key': ('Title',)}


admin.site.register(Post, PostAdmin)

