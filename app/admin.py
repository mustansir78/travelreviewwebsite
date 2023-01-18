import textwrap

from django.contrib import admin

from .models import Item, Review


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "location", "photo", "get_description")

    def get_description(self, obj):
        return textwrap.shorten(obj.description, width=30, placeholder="...")

    get_description.short_description = "description"


admin.site.register(Item, ItemAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("reviewed_by", "reviewed_by_email", "get_description", "reviewed_on", "item")

    def get_description(self, obj):
        return textwrap.shorten(obj.review, width=30, placeholder="...")

    get_description.short_description = "review"


admin.site.register(Review, ReviewAdmin)
