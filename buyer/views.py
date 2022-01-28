from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from sawo import createTemplate, getContext, verifyToken
import json
import os
from django.template import loader
from django.db.models import Q, Sum

from seller.models import Product


load = ''
loaded = 0


def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

createTemplate("templates/partials")

def index(request):

    return render(request,"buyer.html")

def login(request):
    setLoaded()
    setPayload(load if loaded<2 else '')
    # print(config('api_key'))
    configuration = {
                "auth_key": os.environ.get("BUYER_API_KEY"),
                "identifier": "email",
                "to": "buyer/receive"
    }
    context = {"sawo":configuration,"load":load,"title":"Home"}

    return render(request,"login.html", context)

def receive(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setLoaded(True)
        setPayload(payload)
        print(payload)

        return redirect('/buyer/products')
        # return HttpResponse(json.dumps(response_data), content_type="application/json")


def products(request):

    template=loader.get_template('buyer/products.html')

    list_of_products=Product.objects.order_by('?')

    query=request.GET.get('q')

    if query:
        product_list=list_of_products.filter(Q(product_name__icontains=query) |
                                            Q(description__icontains=query)).distinct()

    else:
        product_list=list_of_products

    sort=request.GET.get('sort')
    if sort:
        if sort=='Descending':
            product_list=product_list.order_by('-product_name')
        elif sort=='Ascending':
            product_list=product_list.order_by('product_name')

    query_count=product_list.count()

    number_of_products=product_list.count()
    paginator=Paginator(product_list, 30)
    page=request.GET.get('page')
    product_list=paginator.get_page(page)

    context={
        'number_of_products': number_of_products,
        'query_count': query_count,
        'product_list': product_list,
    }

    return HttpResponse(template.render(context, request))
