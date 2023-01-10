from rest_framework import serializers
from .models import *



class FeedbackSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    R = serializers.FloatField(required=False)
    Y = serializers.FloatField(required=False)
    B = serializers.FloatField(required=False)
    U = serializers.FloatField(required=False)
    RC = serializers.FloatField(required=False)
    YC = serializers.FloatField(required=False)
    BC = serializers.FloatField(required=False)
    UC = serializers.FloatField(required=False)
    UB = serializers.FloatField(required=False)

    def create(self, validated_data):
      return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
      instance.R = validated_data.get("R", instance.R)
      instance.Y = validated_data.get("Y", instance.Y)
      instance.B = validated_data.get("B", instance.B)
      instance.U = validated_data.get("U", instance.U)
      instance.RC = validated_data.get("RC", instance.RC)
      instance.YC = validated_data.get("YC", instance.YC)
      instance.BC = validated_data.get("BC", instance.BC)
      instance.UC = validated_data.get("UC", instance.UC)
      instance.UB = validated_data.get("UB", instance.UB)
      
      instance.save()
      return instance

    class Meta:
        model = Feedback
        fields = ["__all__"]