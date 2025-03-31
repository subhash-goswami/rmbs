from django.core.exceptions import ValidationError
from django.test import TestCase
from mortgages.models import Mortgage

class CreditRatingTest(TestCase):

    def test_credit_rating_aaa(self):
        """Credit rating should be AAA for low-risk borrowers"""
        mortgage = Mortgage(
            credit_score=800, loan_amount=100000, property_value=300000,
            annual_income=100000, debt_amount=10000, loan_type="fixed", property_type="single_family"
        )
        self.assertEqual(mortgage.calculate_credit_rating(), "AAA")

    def test_credit_rating_bbb(self):
        """Credit rating should be BBB for moderate-risk borrowers"""
        mortgage = Mortgage(
            credit_score=300, loan_amount=250000, property_value=40000,
            annual_income=70000, debt_amount=35000, loan_type="fixed", property_type="condo"
        )
        self.assertEqual(mortgage.calculate_credit_rating(), "BBB")

    def test_credit_rating_c(self):
        """Credit rating should be C for high-risk borrowers"""
        mortgage = Mortgage(
            credit_score=500, loan_amount=200000, property_value=200000,
            annual_income=50000, debt_amount=50000, loan_type="adjustable", property_type="condo"
        )
        self.assertEqual(mortgage.calculate_credit_rating(), "C")

    def test_invalid_credit_score(self):
        """Should raise ValidationError for an invalid credit score"""
        mortgage = Mortgage(
            credit_score=200, loan_amount=100000, property_value=200000,
            annual_income=50000, debt_amount=10000, loan_type="fixed", property_type="single_family"
        )
        with self.assertRaises(ValidationError):
            mortgage.full_clean()

    def test_negative_loan_amount(self):
        """Should raise ValidationError for negative loan amounts"""
        mortgage = Mortgage(
            credit_score=700, loan_amount=-50000, property_value=200000,
            annual_income=60000, debt_amount=10000, loan_type="fixed", property_type="single_family"
        )
        with self.assertRaises(ValidationError):
            mortgage.full_clean()

