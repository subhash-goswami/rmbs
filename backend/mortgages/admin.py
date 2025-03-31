from django.contrib import admin

from mortgages.models import Mortgage


@admin.register(Mortgage)
class MortgageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "credit_score",
        "loan_amount",
        "property_value",
        "annual_income",
        "loan_type",
        "property_type"
    )
    list_filter = ("loan_type", "property_type")
