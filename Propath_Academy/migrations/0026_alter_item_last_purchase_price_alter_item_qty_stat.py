# Generated by Django 4.2.11 on 2024-06-04 16:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0006_appusermodel_app_objects'),
        ('dynamic_models', '0025_alter_competitionstudent_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='last_purchase_price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='qty',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('object_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('franchises', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='appauth.appusermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
