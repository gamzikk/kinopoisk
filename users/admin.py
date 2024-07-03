from django.contrib import admin
from .models import CustomUser, Profile, UserSubscription, Subscription

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(UserSubscription)
admin.site.register(Subscription)