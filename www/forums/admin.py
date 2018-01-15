from django.contrib import admin

from forums.models import Category, Forum, Topic, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_editable = ('position',)


class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'position', 'is_closed')
    list_editable = ('position', 'is_closed')
    list_filter = ('category',)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'forum')
    list_filter = ('forum',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'created', 'updated')
    list_filter = ('topic',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
