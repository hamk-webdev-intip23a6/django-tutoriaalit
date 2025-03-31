# Generated by Django 5.1.7 on 2025-03-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
    ]
