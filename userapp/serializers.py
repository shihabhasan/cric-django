from cricapp.serializers import DynamicFieldsModelSerializer, serializers
from userapp.models import Cricketer


class CricketerSerializer(DynamicFieldsModelSerializer):
    runs = serializers.SerializerMethodField()

    class Meta:
        model = Cricketer
        fields = '__all__'

    def get_runs(self, obj):
        return obj.get_runs()