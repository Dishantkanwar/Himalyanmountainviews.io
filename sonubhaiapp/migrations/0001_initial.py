# Generated by Django 4.0.2 on 2022-03-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourname', models.CharField(max_length=200)),
                ('youremail', models.CharField(max_length=200)),
                ('yourphone', models.CharField(max_length=200)),
                ('yourproblem', models.CharField(max_length=200)),
            ],
        ),
    ]
