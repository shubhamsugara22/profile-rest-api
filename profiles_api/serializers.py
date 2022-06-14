from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our views"""
    name = serializers.CharField(max_length=10)
