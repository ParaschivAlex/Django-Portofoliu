# Generated by Django 2.2.24 on 2021-09-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_job_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
