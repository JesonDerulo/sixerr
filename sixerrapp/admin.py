from django.contrib import admin
from .models import Profile,Gig,Purchase
from .models import Review
# Register your models here.
admin.site.register(Profile)
admin.site.register(Gig)
admin.site.register(Purchase)
admin.site.register(Review)

