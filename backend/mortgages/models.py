from django.core.exceptions import ValidationError
from django.db import models


class Mortgage(models.Model):
    LOAN_TYPE_CHOICES = [
        ('fixed', 'Fixed'),
        ('adjustable', 'Adjustable')
    ]
    PROPERTY_TYPE_CHOICES = [
        ('single_family', 'Single Family'),
        ('condo', 'Condo')
    ]

    credit_score = models.IntegerField()
    loan_amount = models.FloatField()
    property_value = models.FloatField()
    annual_income = models.FloatField()
    debt_amount = models.FloatField()
    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_credit_rating(self):
        risk_score = 0

        # Loan-to-Value (LTV) Ratio
        ltv = self.loan_amount / self.property_value
        if ltv > 0.9:
            risk_score += 2
        elif ltv > 0.8:
            risk_score += 1

        # Debt-to-Income (DTI) Ratio
        dti = self.debt_amount / self.annual_income
        if dti > 0.5:
            risk_score += 2
        elif dti > 0.4:
            risk_score += 1

        # Credit Score Impact
        if self.credit_score >= 750:
            risk_score -= 2
        elif self.credit_score >= 700:
            risk_score -= 1
        elif self.credit_score < 650:
            risk_score += 1
        elif self.credit_score < 600:
            risk_score += 2

        # Loan Type
        if self.loan_type == 'fixed':
            risk_score -= 1
        else:
            risk_score += 1

        # Property Type
        if self.property_type == 'condo':
            risk_score += 1

        # Assign Credit Rating
        if risk_score <= 2:
            return 'AAA'
        elif 3 <= risk_score <= 5:
            return 'BBB'
        else:
            return 'C'

    def clean(self):
        if self.credit_score < 300 or self.credit_score > 850:
            raise ValidationError("Credit score must be between 300 and 850.")
        if self.loan_amount <= 0:
            raise ValidationError("Loan amount must be positive.")