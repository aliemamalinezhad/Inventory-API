from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ProductSerializer, CategorySerializer
)
from inventory.models.product import Product as ProductModel
from inventory.models.category import Category as CategoryModel

class CategoryListAPIView(generics.ListCreateAPIView):
    """ Return list of all categories"""
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'



class ProductsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            search_fields = ['name']
            filter_backends = (filters.SearchFilter,)
            products = ProductModel.objects.all()
            srz_data = ProductSerializer(instance=products, many=True).data
            return Response(srz_data, status = status.HTTP_200_OK)
        except:
            return Response({'status': 'Internal Server Error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )


class CreateProductAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = ProductSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
		
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateProductAPIView(APIView):
    def put(self, request,pk, *args, **kwargs):
        product = ProductModel.objects.get(pk=pk)
        srz_data = ProductSerializer(instance=product, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)

        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePeoductAPIView(APIView):
    def delete(self, request, pk):
        try:
            product = ProductModel.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'status': 'Internal Server Error'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )