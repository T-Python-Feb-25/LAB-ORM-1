# Generated by Django 5.1.6 on 2025-03-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/'),
        ),
    ]
