from djongo import models
from django import forms
from django.core.validators import int_list_validator


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
    dice_count = models.IntegerField()
    dice = models.IntegerField()
    ttype = models.TextField()

    class Meta:
        abstract = True


class RangedObj(models.Model):
    isr = models.BooleanField()
    distance = models.Field()

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

    costs = models.EmbeddedField(
        model_container=CostObj
    )
    damage = models.EmbeddedField(
        model_container=DamageObj
    )
    ranged = models.EmbeddedField(
        model_container=RangedObj
    )

    weight = models.IntegerField()
    group_type = models.TextField()
    twohanded = models.BooleanField()


class GameArmor(models.Model):
    _id = models.ObjectIdField()
    name_rus = models.TextField()

    ac = models.IntegerField()
    material = models.TextField()
    weight = models.IntegerField()

    costs = models.EmbeddedField(
        model_container=CostObj
    )

