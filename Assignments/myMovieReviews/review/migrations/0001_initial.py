# Generated by Django 5.1.4 on 2025-01-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('release', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('stars', models.FloatField()),
            ],
        ),
    ]
