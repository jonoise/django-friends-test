from django.contrib import admin
from account.models import Account, FriendRequest, RemoveFriend, FriendRequestNotification

admin.site.register(Account)
admin.site.register(FriendRequest)
admin.site.register(RemoveFriend)
admin.site.register(FriendRequestNotification)