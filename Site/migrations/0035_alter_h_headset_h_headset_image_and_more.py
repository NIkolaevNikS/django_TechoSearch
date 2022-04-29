# Generated by Django 4.0.3 on 2022-03-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0034_alter_transaction_transaction_headset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h_headset',
            name='H_HeadSet_Image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение модели'),
        ),
        migrations.AlterField(
            model_name='k_keyboard',
            name='K_Keyboard_Image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение модели'),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_Image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение модели'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='Manufacturer_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение бренда'),
        ),
    ]
