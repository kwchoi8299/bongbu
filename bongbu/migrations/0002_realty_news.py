# Generated by Django 4.0.3 on 2023-05-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongbu', '0001_initial_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty_News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]
