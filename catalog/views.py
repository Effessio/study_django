from django.shortcuts import render_to_response
from django.http import Http404

from catalog.models import Producer, Product


def producers(request):
    context = {
        'producers_list': Producer.objects.all(),
    }
    return render_to_response('catalog/producers.html', context)


def producer(request, producer_id):
    try:
        producer = Producer.objects.get(id=producer_id)
    except Producer.DoesNotExist:
        raise Http404

    context = {
        'producer': producer,
        'products_list': producer.product_set.all(),

    }

    return render_to_response('catalog/producer.html', context)