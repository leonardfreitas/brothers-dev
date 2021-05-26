from django.db import models

from accounts.models import User
from services.models import Action


class Ticket(models.Model):
    user = models.ForeignKey(
        User, related_name='tickets', on_delete=models.CASCADE)
    action = models.ForeignKey(
        Action, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {} -> {}'.format(self.action, self.action.target, self.action.target.service)
