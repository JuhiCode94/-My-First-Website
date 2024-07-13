from django.contrib import admin
from home.models import Contact, Order, Subscriber

# Register your models here.
# Register the Contact model
admin.site.register(Contact)
# Register the Order model
admin.site.register(Order)
# Register the Subscriber model
admin.site.register(Subscriber)
