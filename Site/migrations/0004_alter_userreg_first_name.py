# Generated by Django 4.0.3 on 2022-03-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_alter_userreg_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='First_name',
            field=models.CharField(help_text='Имя', max_length=50, null=True),
        ),
    ]
