# Generated by Django 3.0.8 on 2020-07-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recpie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]