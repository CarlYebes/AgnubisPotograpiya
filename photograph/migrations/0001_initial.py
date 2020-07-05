# Generated by Django 3.0.8 on 2020-07-05 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picture',
            fields=[
                ('title', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
