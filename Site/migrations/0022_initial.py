# Generated by Django 4.0.3 on 2022-03-21 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Site', '0021_remove_h_headset_h_headset_connecttype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionInt',
            fields=[
                ('ConnectionInt_id', models.AutoField(help_text='ID интерфейса подключения', primary_key=True, serialize=False, unique=True)),
                ('ConnectionInt_name', models.CharField(help_text='Интерфейс подключения', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectType',
            fields=[
                ('ConnectType_id', models.AutoField(help_text='ID типа подключения', primary_key=True, serialize=False, unique=True)),
                ('ConnectType_name', models.CharField(help_text='Тип подключения', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='H_HeadSet_Hz',
            fields=[
                ('H_HeadSet_Hz_id', models.AutoField(help_text='ID частоты звука', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_Hz_Min_name', models.CharField(help_text='Минимальная воспроизводимая частота', max_length=50, null=True, verbose_name='Минимальная воспроизводимая частота')),
                ('H_HeadSet_Hz_Max_name', models.CharField(help_text='Максимальная воспроизводимая частота', max_length=50, null=True, verbose_name='Максимальная воспроизводимая частота')),
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
            name='M_Mouse_DPI',
            fields=[
                ('M_Mouse_DPI_id', models.AutoField(help_text='ID разрешение датчика', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_DPI_name', models.CharField(help_text='Максимальное разрешение датчика', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse_Frequency',
            fields=[
                ('M_Mouse_Frequency_id', models.AutoField(help_text='ID частоты', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_Frequency_name', models.CharField(help_text='Частота обновления', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse_SenserModel',
            fields=[
                ('M_Mouse_SenserModel_id', models.AutoField(help_text='ID модели сенсора', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_SenserModel_name', models.CharField(help_text='Модель сенсора', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('Manufacturer_id', models.AutoField(help_text='ID производителя', primary_key=True, serialize=False, unique=True)),
                ('Manufacturer_name', models.CharField(help_text='Бренд', max_length=50, null=True)),
                ('Manufacturer_image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('User_role_id', models.AutoField(help_text='ID роли', primary_key=True, serialize=False, unique=True)),
                ('User_role_name', models.CharField(help_text='Название роли', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('User_id', models.AutoField(help_text='ID пользователя', primary_key=True, serialize=False, unique=True)),
                ('First_name', models.CharField(help_text='Имя', max_length=50, null=True)),
                ('Middle_name', models.CharField(help_text='Отчество', max_length=50)),
                ('Last_name', models.CharField(help_text='Фамилия', max_length=50)),
                ('Email', models.EmailField(help_text='Почта', max_length=50, unique=True)),
                ('Username', models.CharField(help_text='Ник', max_length=50, unique=True)),
                ('User_password', models.CharField(help_text='Пароль', max_length=100)),
                ('Date_Registration', models.DateField(auto_now_add=True, help_text='Дата регистрации')),
                ('User_role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.userrole')),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse',
            fields=[
                ('M_Mouse_id', models.IntegerField(help_text='ID компьютерной мыши', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_name', models.CharField(help_text='Название компьютерной мыши', max_length=50, verbose_name='Название компьютерной мыши')),
                ('M_Mouse_Image', models.ImageField(null=True, upload_to='')),
                ('M_Mouse_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype', verbose_name='Тип подключения')),
                ('M_Mouse_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint', verbose_name='Интерфейс подключения')),
                ('M_Mouse_DPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_dpi', verbose_name='Максимальное разрешение датчика')),
                ('M_Mouse_Frequency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_frequency', verbose_name='Частота обращения')),
                ('M_Mouse_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer', verbose_name='Бренд')),
                ('M_Mouse_SenserModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_sensermodel', verbose_name='Модель сенсора')),
            ],
        ),
        migrations.CreateModel(
            name='K_Keyboard',
            fields=[
                ('K_Keyboard_id', models.IntegerField(help_text='ID клавиатуры', primary_key=True, serialize=False, unique=True)),
                ('K_Keyboard_name', models.CharField(help_text='Название клавиатуры', max_length=50, verbose_name='Название клавиатуры')),
                ('K_Keyboard_Image', models.ImageField(null=True, upload_to='')),
                ('K_Keyboard_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype', verbose_name='Тип подключения')),
                ('K_Keyboard_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint', verbose_name='Интерфейс подключения')),
                ('K_Keyboard_Format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_format', verbose_name='Формат клавиатуры')),
                ('K_Keyboard_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer', verbose_name='Бренд')),
                ('K_Keyboard_SwitchModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_switchmodel', verbose_name='Модель переключателя')),
                ('K_Keyboard_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard_type', verbose_name='Тип клавиатуры')),
            ],
        ),
        migrations.CreateModel(
            name='H_HeadSet',
            fields=[
                ('H_HeadSet_id', models.IntegerField(help_text='ID гарнитуры', primary_key=True, serialize=False, unique=True)),
                ('H_HeadSet_name', models.CharField(help_text='Название гарнитуры', max_length=50, verbose_name='Название гарнитуры')),
                ('H_HeadSet_Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('H_HeadSet_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype', verbose_name='Тип подключения')),
                ('H_HeadSet_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint', verbose_name='Интерфейс подключения')),
                ('H_HeadSet_Hz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_hz', verbose_name='Воспроизводимая частота')),
                ('H_HeadSet_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer', verbose_name='Бренд')),
                ('H_HeadSet_Scheme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_scheme', verbose_name='Схема звука')),
                ('H_HeadSet_Sens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_sens', verbose_name='Чувствительность')),
                ('H_HeadSet_Set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.h_headset_set', verbose_name='Комплект')),
            ],
        ),
    ]
