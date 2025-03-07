from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ReactionSlot(models.Model):
    reaction = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class NoteSlots(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reactions = models.ManyToManyField(ReactionSlot)
