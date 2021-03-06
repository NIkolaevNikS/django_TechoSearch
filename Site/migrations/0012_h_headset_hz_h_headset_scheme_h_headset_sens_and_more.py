# Generated by Django 4.0.3 on 2022-03-19 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0011_k_keyboard_format_k_keyboard_switchmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='H_HeadSet_Hz',
            fields=[
                ('H_HeadSet_Hz_id', models.AutoField(help_text='ID частоты звука', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_Hz_Min_name', models.CharField(help_text='Минимальная воспроизводимая частота', max_length=50, null=True)),
                ('H_HeadSet_Hz_Max_name', models.CharField(help_text='Максимальная воспроизводимая частота ', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='H_HeadSet_Scheme',
            fields=[
                ('H_HeadSet_Scheme_id', models.AutoField(help_text='ID Схемы', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_Scheme_name', models.CharField(help_text='Схема звука', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='H_HeadSet_Sens',
            fields=[
                ('H_HeadSet_Sens_id', models.AutoField(help_text='ID чувствительности', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_Sens_name', models.CharField(help_text='Чувствительность', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='H_HeadSet_Set',
            fields=[
                ('H_HeadSet_Set_id', models.AutoField(help_text='ID комплекта', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_Set_name', models.CharField(help_text='Комплект', max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='k_keyboard',
            name='K_Keyboard_id',
            field=models.IntegerField(help_text='ID клавиатуры', unique=True),
        ),
        migrations.AlterField(
            model_name='k_keyboard',
            name='K_Keyboard_name',
            field=models.CharField(help_text='Название клавиатуры', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_id',
            field=models.IntegerField(help_text='ID компьютерной мыши', unique=True),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_name',
            field=models.CharField(help_text='Название компьютерной мыши', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='H_HeadSet',
            fields=[
                ('H_HeadSet_id', models.IntegerField(help_text='ID гарнитуры', unique=True)),
                ('H_HeadSet_name', models.CharField(help_text='Название гарнитуры', max_length=50, primary_key=True, serialize=False)),
                ('H_HeadSet_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype')),
                ('H_HeadSet_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint')),
                ('H_HeadSet_Hz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_hz')),
                ('H_HeadSet_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer')),
                ('H_HeadSet_Scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_scheme')),
                ('H_HeadSet_Sens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_sens')),
                ('H_HeadSet_Set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_set')),
            ],
        ),
    ]
