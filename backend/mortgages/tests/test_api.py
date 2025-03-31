from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from mortgages.models import Mortgage

class MortgageAPITest(TestCase):

    def setUp(self):
        """Setup test client and sample data"""
        self.client = APIClient()
        self.valid_mortgage = {
            "credit_score": 720,
            "loan_amount": 150000,
            "property_value": 300000,
            "annual_income": 80000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family",
        }
        self.invalid_mortgage = {
            "credit_score": 250,
            "loan_amount": -50000,
            "property_value": 300000,
            "annual_income": 80000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family",
        }

    def test_create_mortgage_valid(self):
        """Should create a mortgage successfully"""
        response = self.client.post("/api/mortgages/", self.valid_mortgage, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_mortgage_invalid(self):
        """Should return 400 Bad Request for invalid mortgage"""
        response = self.client.post("/api/mortgages/", self.invalid_mortgage, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_mortgages_list(self):
        """Should retrieve the mortgage list"""
        Mortgage.objects.create(**self.valid_mortgage)
        response = self.client.get("/api/mortgages/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_mortgage(self):
        """Should delete a mortgage"""
        mortgage = Mortgage.objects.create(**self.valid_mortgage)
        response = self.client.delete(f"/api/mortgages/{mortgage.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mortgage.objects.count(), 0)
