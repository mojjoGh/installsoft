# Generated by Django 2.1.5 on 2019-09-19 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20190919_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='catergory',
            new_name='category',
        ),
    ]