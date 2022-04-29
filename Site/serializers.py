from rest_framework.serializers import ModelSerializer

from .models import M_Mouse


class MouseSerializer(ModelSerializer):
    class Meta:
        model = M_Mouse
        fields = '__all__'
