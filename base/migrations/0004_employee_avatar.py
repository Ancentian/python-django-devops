# Generated by Django 4.2.3 on 2023-11-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(default='user.jpg', null=True, upload_to=''),
        ),
    ]