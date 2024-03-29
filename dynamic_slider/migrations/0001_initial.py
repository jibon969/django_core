# Generated by Django 3.1.7 on 2021-03-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='slider title is mandatory', max_length=120, null=True)),
                ('extraLargeDevices', models.ImageField(blank=True, help_text='1920x597', null=True, upload_to='slider/')),
                ('largeDevices', models.ImageField(blank=True, help_text='1400x400', null=True, upload_to='slider/')),
                ('mediumDevices', models.ImageField(blank=True, help_text='800X400', null=True, upload_to='slider/')),
                ('smallDevices', models.ImageField(blank=True, help_text='600x400', null=True, upload_to='slider/')),
                ('url_field', models.URLField(blank=True, max_length=120, null=True)),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Slider Position')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
