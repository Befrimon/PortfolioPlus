# Generated by Django 3.1.12 on 2024-01-31 09:40

from django.db import migrations, models
import djongo.models.fields
import handbook.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRace',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name_rus', models.TextField()),
                ('name_eng', models.TextField()),
                ('description', models.TextField()),
                ('info', djongo.models.fields.EmbeddedField(model_container=handbook.models.RaceInfo)),
                ('create', djongo.models.fields.EmbeddedField(model_container=handbook.models.RaceCreate)),
                ('skills', djongo.models.fields.EmbeddedField(model_container=handbook.models.RaceSkill)),
                ('spec', djongo.models.fields.ArrayField(model_container=handbook.models.TDObject, model_form_class=handbook.models.TDObjectForm)),
                ('acting', djongo.models.fields.ArrayField(model_container=handbook.models.TDObject, model_form_class=handbook.models.TDObjectForm)),
            ],
        ),
        migrations.CreateModel(
            name='GameWeapon',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name_rus', models.TextField()),
                ('name_eng', models.TextField()),
                ('weight', models.IntegerField()),
                ('group_type', models.TextField()),
            ],
        ),
    ]
