from django.contrib import admin
from website.models import Channel, Videos, Comments
# Register your models here.
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name']


class VideosAdmin(admin.ModelAdmin):
    list_display = ['title','like','dislike','views','is_active']

    

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comments','is_active']
    
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Comments, CommentsAdmin)
