# Generated by Django 4.1.2 on 2022-11-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourApp', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='book_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]