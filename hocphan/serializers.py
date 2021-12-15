from rest_framework import serializers
from .models import Majors
from .models import Subjects
from .models import Docs
class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Majors
        fields = ('major_id','major_name')

