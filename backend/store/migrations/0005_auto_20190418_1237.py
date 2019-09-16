# Generated by Django 2.2 on 2019-04-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variable_hit_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='word',
        ),
        migrations.AddField(
            model_name='variable',
            name='words',
            field=models.ManyToManyField(related_name='variables', to='store.Word'),
        ),
    ]