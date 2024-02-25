# Generated by Django 5.0.2 on 2024-02-25 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.ImageField(upload_to='')),
                ('groumImage', models.ImageField(upload_to='')),
                ('groupAdmin', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messeges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messegeBody', models.TextField()),
                ('messegeDate', models.DateTimeField()),
                ('messegeReaded', models.BooleanField()),
                ('messegeReadedTime', models.DateTimeField()),
                ('messegeAutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('messegeGroupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messeges.group')),
            ],
            options={
                'ordering': ('-messegeDate',),
            },
        ),
    ]
