# Generated by Django 3.1.7 on 2021-03-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_slider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('about', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(help_text='width: 1600px & height: 575px', upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
