from django.urls import path
from inventory.api import views

app_name = "inventory"

urlpatterns = [
    path('category-list/', views.CategoryListAPIView.as_view(), name="categories"),
    path('product-list/', views.ProductsAPIView.as_view(), name="products"),
    path('product-create/', views.CreateProductAPIView.as_view(), name="create_product"),
    path('product-update/<int:pk>/', views.UpdateProductAPIView.as_view(), name="update_product"),

]