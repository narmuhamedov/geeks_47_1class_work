# Generated by Django 5.1.3 on 2024-12-12 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_blog', '0003_alter_filmmodel_options_review'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='film_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy_film', to='films_blog.filmmodel'),
        ),
    ]