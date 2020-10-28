# Generated by Django 3.1.2 on 2020-10-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('author', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('language', models.CharField(max_length=15)),
                ('genre', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('num_pages', models.IntegerField()),
                ('num_sold', models.IntegerField()),
                ('recommended_age', models.IntegerField()),
                ('thumbnail', models.CharField(max_length=30)),
            ],
        ),
    ]
