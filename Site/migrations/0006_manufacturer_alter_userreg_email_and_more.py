# Generated by Django 4.0.3 on 2022-03-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_alter_userreg_user_id_alter_userrole_user_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('Manufacturer_id', models.AutoField(help_text='ID производителя', primary_key=True, serialize=False, unique=True)),
                ('Manufacturer_name', models.CharField(help_text='Бренд', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='userreg',
            name='Email',
            field=models.EmailField(help_text='Почта', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='User_id',
            field=models.AutoField(help_text='ID пользователя', primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='Username',
            field=models.CharField(help_text='Ник', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='User_role_id',
            field=models.AutoField(help_text='ID роли', primary_key=True, serialize=False, unique=True),
        ),
    ]