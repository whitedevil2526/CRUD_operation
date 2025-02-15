# Generated by Django 5.1.6 on 2025-02-08 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('prize', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
