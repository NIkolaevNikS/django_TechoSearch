from django.contrib import admin
from .models import Manufacturer, ConnectType, ConnectionInt, K_Keyboard_Format, \
    K_Keyboard_SwitchModel, K_Keyboard, K_Keyboard_Type, M_Mouse_SenserModel, M_Mouse, M_Mouse_DPI, M_Mouse_Frequency, \
    H_HeadSet_Scheme, H_HeadSet_Hz, H_HeadSet_Set, H_HeadSet, H_HeadSet_Sens

admin.site.register(Manufacturer)
admin.site.register(ConnectType)
admin.site.register(ConnectionInt)
admin.site.register(K_Keyboard_Format)
admin.site.register(K_Keyboard_SwitchModel)
# admin.site.register(K_Keyboard)
admin.site.register(K_Keyboard_Type)
admin.site.register(M_Mouse_SenserModel)
# admin.site.register(M_Mouse)
admin.site.register(M_Mouse_DPI)
admin.site.register(M_Mouse_Frequency)
admin.site.register(H_HeadSet_Scheme)
# admin.site.register(H_HeadSet_Hz)
admin.site.register(H_HeadSet_Set)
# admin.site.register(H_HeadSet)
admin.site.register(H_HeadSet_Sens)


# @admin.register(UserReg)
# class UserRegAdmin(admin.ModelAdmin):
# list_display = ('First_name', 'Last_name', 'Email', 'Username', 'Date_Registration')


@admin.register(K_Keyboard)
class K_KeyboardAdmin(admin.ModelAdmin):
    list_display = (
        'K_Keyboard_name', 'K_Keyboard_Manufacturer', 'K_Keyboard_Type', 'K_Keyboard_SwitchModel', 'K_Keyboard_Format',
        'K_Keyboard_ConnectType', 'K_Keyboard_ConnectionInt')
    list_filter = ('K_Keyboard_Manufacturer', 'K_Keyboard_Type', 'K_Keyboard_SwitchModel', 'K_Keyboard_Format',
                   'K_Keyboard_ConnectType', 'K_Keyboard_ConnectionInt')
    fields = ['K_Keyboard_name', 'K_Keyboard_Manufacturer', 'K_Keyboard_Type', 'K_Keyboard_SwitchModel',
              'K_Keyboard_Format',
              ('K_Keyboard_ConnectType', 'K_Keyboard_ConnectionInt'), 'K_Keyboard_Image']


@admin.register(M_Mouse)
class M_MouseAdmin(admin.ModelAdmin):
    list_display = (
        'M_Mouse_name', 'M_Mouse_Manufacturer', 'M_Mouse_SenserModel', 'M_Mouse_ConnectType', 'M_Mouse_Frequency',
        'M_Mouse_DPI', 'M_Mouse_ConnectionInt', 'M_Mouse_Price')
    list_filter = (
        'M_Mouse_Manufacturer', 'M_Mouse_SenserModel', 'M_Mouse_ConnectType', 'M_Mouse_Frequency', 'M_Mouse_DPI',
        'M_Mouse_ConnectionInt')
    fields = ['M_Mouse_name', 'M_Mouse_Manufacturer', 'M_Mouse_SenserModel',
              ('M_Mouse_DPI', 'M_Mouse_Frequency'),
              ('M_Mouse_ConnectType', 'M_Mouse_ConnectionInt'), 'M_Mouse_Image', 'M_Mouse_Price']


@admin.register(H_HeadSet)
class H_HeadSetAdmin(admin.ModelAdmin):
    list_display = ('H_HeadSet_name', 'H_HeadSet_Manufacturer', 'H_HeadSet_Scheme', 'H_HeadSet_Hz', 'H_HeadSet_Sens',
                    'H_HeadSet_ConnectType', 'H_HeadSet_ConnectionInt', 'H_HeadSet_Set')
    list_filter = (
        'H_HeadSet_Manufacturer', 'H_HeadSet_Scheme', 'H_HeadSet_Hz', 'H_HeadSet_Sens', 'H_HeadSet_ConnectType',
        'H_HeadSet_ConnectionInt', 'H_HeadSet_Set')
    fields = ['H_HeadSet_name', 'H_HeadSet_Manufacturer', 'H_HeadSet_Scheme',
              ('H_HeadSet_Sens', 'H_HeadSet_Hz'),
              ('H_HeadSet_ConnectType', 'H_HeadSet_ConnectionInt'), 'H_HeadSet_Set', 'H_HeadSet_Image']


@admin.register(H_HeadSet_Hz)
class H_HeadSet_HzAdmin(admin.ModelAdmin):
    list_display = ('H_HeadSet_Hz_Min_name', 'H_HeadSet_Hz_Max_name')
