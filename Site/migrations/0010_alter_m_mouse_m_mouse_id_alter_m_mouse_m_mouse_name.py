# Generated by Django 4.0.3 on 2022-03-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0009_m_mouse_dpi_m_mouse_frequency_m_mouse_sensermodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_id',
            field=models.IntegerField(help_text='ID интерфейса подключения', unique=True),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_name',
            field=models.CharField(help_text='Интерфейс подключения', max_length=50, primary_key=True, serialize=False),
        ),
    ]
