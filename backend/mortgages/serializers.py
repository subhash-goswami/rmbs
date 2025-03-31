from rest_framework import serializers, generics

from mortgages.models import Mortgage


class MortgageSerializer(serializers.ModelSerializer):
    credit_rating = serializers.SerializerMethodField()

    class Meta:
        model = Mortgage
        fields = '__all__'

    def get_credit_rating(self, obj):
        return obj.calculate_credit_rating()

    def validate_credit_score(self, value):
        if value < 300 or value > 850:
            raise serializers.ValidationError("Credit score must be between 300 and 850.")
        return value

    def validate_loan_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be positive.")
        return value