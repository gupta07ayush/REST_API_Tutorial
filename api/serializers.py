from rest_framework import serializers
from api.models import Company, Employee


# create serializers here

# serializer for company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"

# serializer for Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
