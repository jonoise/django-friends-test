from django.db import models
from django.contrib.auth.models import User
from .utils import COUNTRY_CHOICES

class Account(models.Model):
    # GENERAL
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    # SOCIAL
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    # ACCOUNT STATUS
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} account'.capitalize()

    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        else:
            return f'{self.user.username}'
    
    def get_friends(self):
        return self.friends.all()

    def get_friends_number(self):
        return self.friends.all().count()

class FriendRequest(models.Model):
    FRIEND_REQUEST_OPTIONS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=20,default=FRIEND_REQUEST_OPTIONS[0], choices=FRIEND_REQUEST_OPTIONS)

    def __str__(self):
        return f'{self.sender} to {self.receiver}'

class RemoveFriend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    affected = models.ForeignKey(User, on_delete=models.CASCADE, related_name='affected')

########## Friend Request Notification ##########
class FriendRequestNotification(models.Model):
    friend_request = models.ForeignKey(FriendRequest, on_delete=models.CASCADE, related_name='notification')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_receiver')

    def __str__(self):
        return f'Notification from {self.sender} to {self.receiver}'

    def notify(self):
        return f'{self.sender} te ha enviado una solicitud de amistad.'

