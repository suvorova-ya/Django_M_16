# Generated by Django 4.0.6 on 2022-09-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_post_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='send_messages',
        ),
        migrations.AddField(
            model_name='author',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
