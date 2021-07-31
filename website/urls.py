from django.urls import path
from website.views import (
    index,
    get_products,
    get_product,
    )

urlpatterns = [
    path('', index, name='index'),
    path('buy/', get_products, name='buy'),
    path('buy/<int:product_id>', get_product, name='product'),
]
