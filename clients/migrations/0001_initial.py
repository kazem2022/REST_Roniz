# Generated by Django 4.2.7 on 2024-04-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('description', models.TextField()),
            ],
        ),
    ]
