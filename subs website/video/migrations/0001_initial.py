# Generated by Django 4.0.5 on 2022-06-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]
