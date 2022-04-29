# Generated by Django 4.0.3 on 2022-03-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0031_alter_k_keyboard_k_keyboard_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='h_headset',
            name='H_HeadSet_Price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, verbose_name='Цена клавиатуры'),
        ),
        migrations.AddField(
            model_name='k_keyboard',
            name='K_Keyboard_Price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, verbose_name='Цена клавиатуры'),
        ),
        migrations.AddField(
            model_name='m_mouse',
            name='M_Mouse_Price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True, verbose_name='Цена компьютерной мышки'),
        ),
    ]