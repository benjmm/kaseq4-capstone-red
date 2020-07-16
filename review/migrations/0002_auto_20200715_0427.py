# Generated by Django 3.0.8 on 2020-07-15 04:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('author', 'recipe')},
        ),
    ]