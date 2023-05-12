from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Contact)
# admin.site.register(Comment)
# admin.site.register(Category)


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    search_fields = ('title', )
    inlines = [ProductInline]
    prepopulated_fields = {"slug": ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product')
    fields = ('author', 'product', 'body')
