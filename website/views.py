import re
from django.shortcuts import redirect, render
from django.http import Http404
import requests

from r3_factory.settings import ODOO_BASE_URL

def index(request):
    return redirect(('buy'))

def get_products(request):
    context = {}
    url = ODOO_BASE_URL + '/api/products'
    response = requests.get(url=url).json()
    context['products'] = response
    return render(request, 'index.html', context)

def get_product(request, product_id):
    context = {}
    if not isinstance(product_id, int):
        raise Http404
    url = ODOO_BASE_URL + f'/api/products/{product_id}'
    response = requests.get(url=url).json()
    # response['images'] = [str(ODOO_BASE_URL + image_url) for image_url in response["image_url"]]
    images = list()
    for i in response['images']:
        images.append(ODOO_BASE_URL+i)
    response['images'] = images
    context['product'] = response
    return render(request, 'index.html', context)