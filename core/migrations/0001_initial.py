# Generated by Django 2.2.5 on 2019-10-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]