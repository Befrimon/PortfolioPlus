from djongo import models
from django import forms


class TDObject(models.Model):
    title = models.TextField()
    description = models.TextField()

    class Meta:
        abstract = True


class TDObjectForm(forms.ModelForm):
    class Meta:
        model = TDObject
        fields = (
            "title", "description"
        )


class RaceCreate(models.Model):
    age = models.TextField()
    height = models.TextField()
    speed = models.IntegerField()

    class Meta:
        abstract = True


class RaceInfo(models.Model):
    countries = models.TextField()
    lands = models.TextField()
    languages = models.TextField()
    religions = models.TextField()

    class Meta:
        abstract = True


class RaceSkill(models.Model):
    skill = models.TextField()
    value = models.IntegerField()

    class Meta:
        abstract = True


class CostObj(models.Model):
    gold = models.IntegerField()
    silver = models.IntegerField()
    copper = models.IntegerField()

    class Meta:
        abstract = True


class DamageObj(models.Model):
    dice = models.IntegerField()
    ttype = models.TextField()

    class Meta:
        abstract = True


class GameRace(models.Model):
    _id = models.ObjectIdField()

    name_rus = models.TextField()
    name_eng = models.TextField()
    description = models.TextField()

    info = models.EmbeddedField(RaceInfo)
    create = models.EmbeddedField(RaceCreate)
    skills = models.EmbeddedField(RaceSkill)
    spec = models.ArrayField(
        model_container=TDObject,
        model_form_class=TDObjectForm
    )
    acting = models.ArrayField(
        model_container=TDObject,
        model_form_class=TDObjectForm
    )

    def __str__(self):
        return self.name_eng


class GameWeapon(models.Model):
    _id = models.ObjectIdField()

    name_rus = models.TextField()
    name_eng = models.TextField()

    costs = CostObj()
    damage = DamageObj()
    weight = models.IntegerField()

    group_type = models.TextField()

