from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserRole(models.Model):
    User_role_id = models.AutoField(primary_key=True, help_text="ID роли", unique=True)
    User_role_name = models.CharField(max_length=15, help_text="Название роли")

    def __str__(self):
        return self.User_role_name


class UserReg(models.Model):
    User_id = models.AutoField(primary_key=True, help_text="ID пользователя", unique=True)
    User_role = models.ForeignKey('UserRole', on_delete=models.SET_NULL, null=True)
    First_name = models.CharField(max_length=50, help_text="Имя", null=True)
    Middle_name = models.CharField(max_length=50, help_text="Отчество")
    Last_name = models.CharField(max_length=50, help_text="Фамилия")
    Email = models.EmailField(max_length=50, help_text="Почта", unique=True)
    Username = models.CharField(max_length=50, help_text="Ник", unique=True)
    User_password = models.CharField(max_length=100, help_text="Пароль")
    Date_Registration = models.DateField(auto_now_add=True, auto_now=False, help_text="Дата регистрации")

    def __str__(self):
        return '%s %s %s' % (self.First_name, self.Last_name, self.Username)


class Manufacturer(models.Model):
    Manufacturer_id = models.AutoField(primary_key=True, help_text="ID производителя", unique=True)
    Manufacturer_name = models.CharField(max_length=50, help_text="Бренд", null=True)
    Manufacturer_image = models.ImageField(null=True, blank=True, verbose_name="Изображение бренда")

    def __str__(self):
        return self.Manufacturer_name


class ConnectType(models.Model):
    ConnectType_id = models.AutoField(primary_key=True, help_text="ID типа подключения", unique=True)
    ConnectType_name = models.CharField(max_length=50, help_text="Тип подключения", null=True)

    def __str__(self):
        return self.ConnectType_name


class ConnectionInt(models.Model):
    ConnectionInt_id = models.AutoField(primary_key=True, help_text="ID интерфейса подключения", unique=True)
    ConnectionInt_name = models.CharField(max_length=50, help_text="Интерфейс подключения", null=True)

    def __str__(self):
        return self.ConnectionInt_name


class M_Mouse_Frequency(models.Model):
    M_Mouse_Frequency_id = models.AutoField(primary_key=True, help_text="ID частоты", unique=True)
    M_Mouse_Frequency_name = models.CharField(max_length=50, help_text="Частота обновления", null=True)

    def __str__(self):
        return self.M_Mouse_Frequency_name


class M_Mouse_DPI(models.Model):
    M_Mouse_DPI_id = models.AutoField(primary_key=True, help_text="ID разрешение датчика", unique=True)
    M_Mouse_DPI_name = models.CharField(max_length=50, help_text="Максимальное разрешение датчика", null=True)

    def __str__(self):
        return self.M_Mouse_DPI_name


class M_Mouse_SenserModel(models.Model):
    M_Mouse_SenserModel_id = models.AutoField(primary_key=True, help_text="ID модели сенсора", unique=True)
    M_Mouse_SenserModel_name = models.CharField(max_length=50, help_text="Модель сенсора", null=True)

    def __str__(self):
        return self.M_Mouse_SenserModel_name


class M_Mouse(models.Model):
    M_Mouse_id = models.AutoField(primary_key=True, help_text="ID компьютерной мыши", unique=True)
    M_Mouse_name = models.CharField(max_length=50, unique=True,
                                    verbose_name="Название компьютерной мыши")
    M_Mouse_Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True,
                                             verbose_name="Бренд")
    M_Mouse_SenserModel = models.ForeignKey('M_Mouse_SenserModel', on_delete=models.SET_NULL, null=True,
                                            verbose_name="Модель сенсора")
    M_Mouse_ConnectType = models.ForeignKey('ConnectType', on_delete=models.SET_NULL, null=True,
                                            verbose_name="Тип подключения")
    M_Mouse_Frequency = models.ForeignKey('M_Mouse_Frequency', on_delete=models.SET_NULL, null=True,
                                          verbose_name="Частота обращения")
    M_Mouse_DPI = models.ForeignKey('M_Mouse_DPI', on_delete=models.SET_NULL, null=True,
                                    verbose_name="Максимальное разрешение датчика")
    M_Mouse_ConnectionInt = models.ForeignKey('ConnectionInt', on_delete=models.SET_NULL, null=True,
                                              verbose_name="Интерфейс подключения")
    M_Mouse_Image = models.ImageField(null=True, blank=True, upload_to='uploads/', verbose_name="Изображение модели")
    M_Mouse_Price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Цена компьютерной мышки",
                                        null=True, blank=True)

    def mouse_image_set(self):
        return 'img class=card-img-top src=/uploads/%s' % self.M_Mouse_Image

    mouse_image_set.allow_tags = True
    mouse_image_set.short_description = 'Image'

    def mouse_image_set1(self):
        return 'img class=img-fluid src=/uploads/%s alt=Компьютерная мышь' % self.M_Mouse_Image

    mouse_image_set.allow_tags = True
    mouse_image_set.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('mouse-detail', args=[str(self.M_Mouse_id)])

    def __str__(self):
        return self.M_Mouse_name


class K_Keyboard_Type(models.Model):
    K_Keyboard_Type_id = models.AutoField(primary_key=True, help_text="ID типа клавиатуры", unique=True)
    K_Keyboard_Type_name = models.CharField(max_length=50, help_text="Тип клавиатуры", null=True)

    def __str__(self):
        return self.K_Keyboard_Type_name


class K_Keyboard_SwitchModel(models.Model):
    K_Keyboard_SwitchModel_id = models.AutoField(primary_key=True, help_text="ID модели переключателей", unique=True)
    K_Keyboard_SwitchModel_name = models.CharField(max_length=50, help_text="Модель переключателя", null=True)

    def __str__(self):
        return self.K_Keyboard_SwitchModel_name


class K_Keyboard_Format(models.Model):
    K_Keyboard_Format_id = models.AutoField(primary_key=True, help_text="ID формата клавиатуры", unique=True)
    K_Keyboard_Format_name = models.CharField(max_length=50, help_text="Формат клавиатуры", null=True)

    def __str__(self):
        return self.K_Keyboard_Format_name


class K_Keyboard(models.Model):
    K_Keyboard_id = models.AutoField(primary_key=True, help_text="ID клавиатуры", unique=True)
    K_Keyboard_name = models.CharField(max_length=50,
                                       verbose_name="Название клавиатуры", unique=True)
    K_Keyboard_Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True,
                                                verbose_name="Бренд")
    K_Keyboard_Type = models.ForeignKey('K_Keyboard_Type', on_delete=models.SET_NULL, null=True,
                                        verbose_name="Тип клавиатуры")
    K_Keyboard_SwitchModel = models.ForeignKey('K_Keyboard_SwitchModel', on_delete=models.SET_NULL, null=True,
                                               verbose_name="Модель переключателя")
    K_Keyboard_Format = models.ForeignKey('K_Keyboard_Format', on_delete=models.SET_NULL, null=True,
                                          verbose_name="Формат клавиатуры")
    K_Keyboard_ConnectType = models.ForeignKey('ConnectType', on_delete=models.SET_NULL, null=True,
                                               verbose_name="Тип подключения")
    K_Keyboard_ConnectionInt = models.ForeignKey('ConnectionInt', on_delete=models.SET_NULL, null=True,
                                                 verbose_name="Интерфейс подключения")
    K_Keyboard_Image = models.ImageField(null=True, blank=True, verbose_name="Изображение модели")
    K_Keyboard_Price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Цена клавиатуры", null=True,
                                           blank=True)

    def get_absolute_url(self):
        return reverse('keyboard-detail', args=[str(self.K_Keyboard_id)])

    def keyboard_image_set(self):
        return 'img class=card-img-top src=/uploads/%s' % self.K_Keyboard_Image

    keyboard_image_set.allow_tags = True
    keyboard_image_set.short_description = 'Image'

    def keyboard_image_set1(self):
        return 'img class=img-fluid src=/uploads/%s alt=Клавиатура' % self.K_Keyboard_Image

    keyboard_image_set1.allow_tags = True
    keyboard_image_set1.short_description = 'Image'

    def __str__(self):
        return self.K_Keyboard_name


class H_HeadSet_Scheme(models.Model):
    H_HeadSet_Scheme_id = models.AutoField(primary_key=True, help_text="ID Схемы", unique=True)
    H_HeadSet_Scheme_name = models.CharField(max_length=50, help_text="Схема звука", null=True)

    def __str__(self):
        return self.H_HeadSet_Scheme_name


class H_HeadSet_Hz(models.Model):
    H_HeadSet_Hz_id = models.AutoField(primary_key=True, help_text="ID частоты звука", unique=True)
    H_HeadSet_Hz_Min_name = models.CharField(max_length=50, help_text="Минимальная воспроизводимая частота", null=True,
                                             verbose_name="Минимальная воспроизводимая частота")
    H_HeadSet_Hz_Max_name = models.CharField(max_length=50, help_text="Максимальная воспроизводимая частота", null=True,
                                             verbose_name="Максимальная воспроизводимая частота")

    def __str__(self):
        return '%s %s' % (self.H_HeadSet_Hz_Min_name, self.H_HeadSet_Hz_Max_name)


class H_HeadSet_Sens(models.Model):
    H_HeadSet_Sens_id = models.AutoField(primary_key=True, help_text="ID чувствительности", unique=True)
    H_HeadSet_Sens_name = models.CharField(max_length=50, help_text="Чувствительность", null=True)

    def __str__(self):
        return self.H_HeadSet_Sens_name


class H_HeadSet_Set(models.Model):
    H_HeadSet_Set_id = models.AutoField(primary_key=True, help_text="ID комплекта", unique=True)
    H_HeadSet_Set_name = models.CharField(max_length=50, help_text="Комплект", null=True)

    def __str__(self):
        return self.H_HeadSet_Set_name


class H_HeadSet(models.Model):
    H_HeadSet_id = models.AutoField(primary_key=True, help_text="ID гарнитуры", unique=True)
    H_HeadSet_name = models.CharField(max_length=50,
                                      verbose_name="Название гарнитуры", unique=True)
    H_HeadSet_Manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True,
                                               verbose_name="Бренд")
    H_HeadSet_Scheme = models.ForeignKey('H_HeadSet_Scheme', on_delete=models.SET_NULL, null=True,
                                         verbose_name="Схема звука")
    H_HeadSet_Hz = models.ForeignKey('H_HeadSet_Hz', on_delete=models.SET_NULL, null=True,
                                     verbose_name="Воспроизводимая частота")
    H_HeadSet_Sens = models.ForeignKey('H_HeadSet_Sens', on_delete=models.SET_NULL, null=True,
                                       verbose_name="Чувствительность")
    H_HeadSet_ConnectType = models.ForeignKey('ConnectType', on_delete=models.SET_NULL, null=True,
                                              verbose_name="Тип подключения")
    H_HeadSet_ConnectionInt = models.ForeignKey('ConnectionInt', on_delete=models.SET_NULL, null=True,
                                                verbose_name="Интерфейс подключения")
    H_HeadSet_Set = models.ForeignKey('H_HeadSet_Set', on_delete=models.SET_NULL, null=True,
                                      verbose_name="Комплект")
    H_HeadSet_Image = models.ImageField(null=True, blank=True, verbose_name="Изображение модели")
    H_HeadSet_Price = models.DecimalField(max_digits=19, decimal_places=2, verbose_name="Цена клавиатуры", null=True,
                                          blank=True)

    def get_absolute_url(self):
        return reverse('headset-detail', args=[str(self.H_HeadSet_id)])

    def headset_image_set(self):
        return 'img class=card-img-top src=/uploads/%s' % self.H_HeadSet_Image

    headset_image_set.allow_tags = True
    headset_image_set.short_description = 'Image'

    def headset_image_set1(self):
        return 'img class=img-fluid src=/uploads/%s alt=Наушники' % self.H_HeadSet_Image

    headset_image_set1.allow_tags = True
    headset_image_set1.short_description = 'Image'

    def __str__(self):
        return self.H_HeadSet_name
