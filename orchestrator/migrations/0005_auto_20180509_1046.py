# Generated by Django 2.0.5 on 2018-05-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0004_auto_20180509_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrequest',
            name='description',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
