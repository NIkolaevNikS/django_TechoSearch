import django_filters
from django import forms

from .models import M_Mouse, K_Keyboard, H_HeadSet


class KeyboardFilter(django_filters.FilterSet):

    class Meta:
        model = K_Keyboard
        fields = {
            'K_Keyboard_name': ['icontains'],
        }
