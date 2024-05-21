from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    online_users = models.ManyToManyField(
        to=User, blank=True, related_name="Users_online"
    )
    members = models.ManyToManyField(to=User, blank=True, related_name="Convo_members")

    def get_online_count(self):
        return self.online_users.count()

    def join(self, user):
        self.online_users.add(user)

    def add_member(self, user):
        self.members.add(user)

    def leave(self, user):
        self.online_users.remove(user)

    def __str__(self) -> str:
        return f"{self.name} ({str(self.get_online_count())})"


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )

    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="message_from_me"
    )

    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="message_to_me", blank=True, null=True
    )
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"From {self.from_user.username} to {self.to_user.username}: {self.content} [{self.timestamp}]"
