# Generated by Django 3.2.16 on 2022-11-02 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_about_d1_content_about_d1_name_about_d2_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page1',
            name='service1',
        ),
        migrations.RemoveField(
            model_name='page1',
            name='service2',
        ),
        migrations.RemoveField(
            model_name='page1',
            name='service3',
        ),
    ]
