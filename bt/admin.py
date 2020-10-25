from django.contrib import admin

# Register your models here.
from .models import Contact,Register, inquiry

admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(inquiry)
