
# Generated by Django 4.1.2 on 2022-10-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_page1_about_alter_page1_innovation1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('header', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),


            ],
        ),
    ]
