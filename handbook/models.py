from djongo import models
from django import forms


class Spec(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True


class SpecForm(forms.ModelForm):
    class Meta:
        model = Spec
        fields = (
            "title", "description"
        )


class GameRace(models.Model):
    _id = models.ObjectIdField()

    name_rus = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)

    info = models.ArrayField(
        model_container=Spec,
        model_form_class=SpecForm
    )

    spec = models.ArrayField(
        model_container=Spec,
        model_form_class=SpecForm
    )
    create = models.ArrayField(
        model_container=Spec,
        model_form_class=SpecForm
    )

    def __str__(self):
        return self.name_eng


class Heroes(models.Model):
    _id = models.ObjectIdField()

    name = models.CharField(max_length=255)
    hits = models.IntegerField()
    max_hits = models.IntegerField()
    energy = models.IntegerField()
    max_energy = models.IntegerField()

    def __str__(self):
        return self.name

