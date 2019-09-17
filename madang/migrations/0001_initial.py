# Generated by Django 2.2.3 on 2019-09-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Madang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=1500)),
                ('price', models.CharField(max_length=100)),
                ('image1', models.ImageField(blank=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, upload_to='images/')),
                ('image6', models.ImageField(blank=True, upload_to='images/')),
                ('image7', models.ImageField(blank=True, upload_to='images/')),
                ('image8', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
