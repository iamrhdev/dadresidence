# Generated by Django 4.2.11 on 2024-03-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_extraservice_service_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y/%m'),
        ),
        migrations.AddField(
            model_name='about',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y/%m'),
        ),
    ]
