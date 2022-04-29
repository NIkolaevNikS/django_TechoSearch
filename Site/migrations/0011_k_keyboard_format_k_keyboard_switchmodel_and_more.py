# Generated by Django 4.0.3 on 2022-03-19 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0010_alter_m_mouse_m_mouse_id_alter_m_mouse_m_mouse_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='K_Keyboard_Format',
            fields=[
                ('K_Keyboard_Format_id', models.AutoField(help_text='ID формата клавиатуры', primary_key=True, serialize=False, unique=True)),
                ('K_Keyboard_Format_name', models.CharField(help_text='Формат клавиатуры', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='K_Keyboard_SwitchModel',
            fields=[
                ('K_Keyboard_SwitchModel_id', models.AutoField(help_text='ID модели переключателей', primary_key=True, serialize=False, unique=True)),
                ('K_Keyboard_SwitchModel_name', models.CharField(help_text='Модель переключателя', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='K_Keyboard_Type',
            fields=[
                ('K_Keyboard_Type_id', models.AutoField(help_text='ID типа клавиатуры', primary_key=True, serialize=False, unique=True)),
                ('K_Keyboard_Type_name', models.CharField(help_text='Тип клавиатуры', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='K_Keyboard',
            fields=[
                ('K_Keyboard_id', models.AutoField(help_text='ID формата клавиатуры', primary_key=True, serialize=False, unique=True)),
                ('K_Keyboard_name', models.CharField(help_text='Формат клавиатуры', max_length=50, null=True)),
                ('K_Keyboard_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype')),
                ('K_Keyboard_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint')),
                ('K_Keyboard_Format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_format')),
                ('K_Keyboard_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer')),
                ('K_Keyboard_SwitchModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_switchmodel')),
                ('K_Keyboard_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_type')),
            ],
        ),
    ]
