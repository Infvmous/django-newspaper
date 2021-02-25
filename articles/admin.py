from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):  # or use admin.StackedInline
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    """Allow add comment creation section inline with article"""
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
