# Generated by Django 5.1.3 on 2024-12-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='films/', verbose_name='Загрузите фото фильма')),
                ('title', models.CharField(max_length=100, verbose_name='укажите название фильма')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('price', models.FloatField(default=10, verbose_name='укажите цену на фильм')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия'), ('Приключения', 'Приключения')], default='Комедия', max_length=100)),
                ('time_watch', models.TimeField(blank=True, verbose_name='Укажите длительность фильма')),
                ('director', models.CharField(default='Иван Иванов', max_length=100, verbose_name='укажите режисера')),
            ],
        ),
    ]
