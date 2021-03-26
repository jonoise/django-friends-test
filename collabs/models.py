from django.db import models
from django.contrib.auth.models import User
from languages.models import Language, Framework


class Collab(models.Model):

    COLLAB_STATUS = (
        ('lfg', 'Looking For Group'),
        ('progress', 'In progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=200, verbose_name='title', blank=True, null=True)
    description = models.TextField(verbose_name='description', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collabs')
    collaborators = models.ManyToManyField(User, related_name='collab', blank=True)
    github = models.URLField(verbose_name='github', blank=True, null=True)
    languages = models.ManyToManyField(Language, related_name='collab')
    frameworks = models.ManyToManyField(Framework, related_name='collab', blank=True)
    status = models.CharField(max_length=20, verbose_name="status", choices=COLLAB_STATUS, default=COLLAB_STATUS[0])
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.title} from ' + f'{self.owner.username}'.capitalize()
    

class Candidate(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collab = models.ForeignKey(Collab, on_delete=models.CASCADE, related_name='candidates')
    status = models.CharField(max_length=20, verbose_name='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0])

    def __str__(self):
        return f'{self.collab.title} - {self.user.username}'