from django.db import models


class GameRace(models.Model):
    name_rus = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    description = models.CharField(max_length=2047)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name_eng


