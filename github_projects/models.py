from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Rating(models.IntegerChoices):
    ONE = 1, _('1')
    TWO = 2, _('2')
    THREE = 3, _('3')
    FOUR = 4, _('4')
    FIVE = 5, _('5')


class ProjectEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField()
    rating = models.PositiveSmallIntegerField(choices=Rating.choices, blank=False, default=Rating.FIVE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{super().__str__()}: {self.name}'


class WebhookConfig(models.Model):
    url = models.URLField()
    method = models.CharField(max_length=7, choices=(('GET', 'GET'), ('POST', 'POST')))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
