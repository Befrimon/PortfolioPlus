# Generated by Django 4.2.6 on 2023-10-14 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerace',
            name='img_path',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]