from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=50)

    service = models.ForeignKey(
        Service, related_name='targets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Action(models.Model):

    class ActionType(models.IntegerChoices):
        VIEW = 0, 'VIEW'  # list and detail
        CREATE = 1, 'CREATE'
        CHANGE = 2, 'CHANGE'
        DELETE = 3, 'DELETE'

    name = models.IntegerField(
        choices=ActionType.choices, default=ActionType.VIEW)
    target = models.ForeignKey(
        Target, related_name='actions', on_delete=models.CASCADE)

    def __str__(self):
        return self.get_name_display()
