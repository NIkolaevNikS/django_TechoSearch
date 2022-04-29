# Generated by Django 4.0.3 on 2022-03-23 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0030_alter_transaction_transaction_headset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='k_keyboard',
            name='K_Keyboard_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='Manufacturer_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Transaction_Keyboard',
            field=models.ForeignKey(blank=True, help_text='Заказанная клавиатура', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.k_keyboard', verbose_name='Клавиатура'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Transaction_Mouse',
            field=models.ForeignKey(blank=True, help_text='Заказанная компьютерная мышь', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse', verbose_name='Компьютерная мышь'),
        ),
    ]