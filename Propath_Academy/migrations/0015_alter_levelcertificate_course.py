# Generated by Django 4.2.11 on 2024-05-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0014_levelcertificate_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelcertificate',
            name='course',
            field=models.CharField(max_length=100),
        ),
    ]
