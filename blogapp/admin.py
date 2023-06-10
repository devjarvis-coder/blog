from django.contrib import admin
from .models import*
# Register your models here.
# admin.site.register(Userdata)
admin.site.register(Blog)
admin.site.register(Categorie)



admin.site.register(ContactUs)
admin.site.register(Profile)

@admin.register(Hotel)
class adminview(admin.ModelAdmin):
    list_display=["hotel","places"]