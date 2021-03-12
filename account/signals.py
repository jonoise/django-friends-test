from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Account, FriendRequest, RemoveFriend

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        acc = Account(user=instance)
        instance.account.save()

@receiver(post_save, sender=FriendRequest)
def friend_request(sender, instance, *args, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'accepted':
        sender_.account.friends.add(receiver_) 
        receiver_.account.friends.add(sender_)
        instance.delete()
    if instance.status == 'declined':
        instance.delete()

@receiver(post_save, sender=RemoveFriend)
def remove_friend(sender, instance, *args, **kwargs):
    owner = instance.owner
    affected = instance.affected
    owner.account.friends.remove(affected)
    affected.account.friends.remove(owner)
    instance.delete()