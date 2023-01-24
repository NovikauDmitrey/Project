from django.contrib import admin
from .models import Author, Contact


admin.site.register(Author)
#admin.site.register(Post)
admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass