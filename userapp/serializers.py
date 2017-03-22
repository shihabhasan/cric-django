from cricapp.serializers import DynamicFieldsModelSerializer
from userapp.models import Cricketer


class CricketerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Cricketer
        fields = '__all__'