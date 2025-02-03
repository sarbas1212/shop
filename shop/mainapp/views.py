from django.shortcuts import render
from .models import product
# to load template file
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def homeview(request):
    #querying the DB and getting a colletcionn of product class object from the records
    products=product.objects.all() #select * from products;

    context = {
        'product_list' : products
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context,request))

    