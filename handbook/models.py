from djongo import models


class GameRace(models.Model):
    _id = models.ObjectIdField()

    name_rus = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)

    countries = models.JSONField()
    lands = models.JSONField()
    langs = models.JSONField()
    religions = models.JSONField()

    def __str__(self):
        return self.name_eng
