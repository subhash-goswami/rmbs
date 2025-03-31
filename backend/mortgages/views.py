from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from mortgages.models import Mortgage
from mortgages.serializers import MortgageSerializer


class MortgageListCreateView(generics.ListCreateAPIView):
    queryset = Mortgage.objects.all()
    serializer_class = MortgageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mortgage = serializer.save()
            return Response({
                'id': mortgage.id,
                'credit_rating': mortgage.calculate_credit_rating()
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MortgageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mortgage.objects.all()
    serializer_class = MortgageSerializer