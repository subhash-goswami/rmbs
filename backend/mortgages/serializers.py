from rest_framework import serializers, generics

from mortgages.models import Mortgage


class MortgageSerializer(serializers.ModelSerializer):
    credit_rating = serializers.SerializerMethodField()

    class Meta:
        model = Mortgage
        fields = '__all__'

    def get_credit_rating(self, obj):
        return obj.calculate_credit_rating()