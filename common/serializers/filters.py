from rest_framework import serializers


class FilterSerializer(serializers.Serializer):
    label = serializers.CharField()
    min_value = serializers.CharField(required=False)
    max_value = serializers.CharField(required=False)
