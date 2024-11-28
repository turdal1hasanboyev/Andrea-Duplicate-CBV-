# Generated by Django 5.1.3 on 2024-11-28 13:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
