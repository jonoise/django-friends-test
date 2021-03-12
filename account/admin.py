from django.contrib import admin
from account.models import Account, FriendRequest, RemoveFriend

admin.site.register(Account)
admin.site.register(FriendRequest)
admin.site.register(RemoveFriend)