import stripe

from django.shortcuts import Http404

from rest_framework.views import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

from payments import models


@api_view(http_method_names=['GET'])
@renderer_classes([TemplateHTMLRenderer])
def get_success_page(request):
    message = "Your payment is succeed"
    return Response({"message": message}, template_name="payments/success.html",
                    status=200)


@api_view(http_method_names=['GET'])
@renderer_classes([TemplateHTMLRenderer])
def get_cancel_page(request):
    message = "Your payment was cancelled"
    return Response({"message": message},
                    template_name="payments/cancel.html", status=404)


@api_view(http_method_names=['GET'])
@renderer_classes([TemplateHTMLRenderer])
def get_item(request, id):
    try:
        item = models.Item.objects.get(id=id)
    except:
        raise Http404
    return Response({'item': item}, template_name='payments/payment.html', status=200)


@api_view(http_method_names=['GET'])
def get_session(request, id):
    try:
        item = models.Item.objects.get(id=id)
    except:
        raise Http404
    stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    session = stripe.checkout.Session.create(success_url="http://localhost:8000/success/",
                                             cancel_url="http://localhost:8000/cancel/",
                                             payment_method_types=["card"],
                                             line_items=[
                                                 {
                                                     "price_data": {
                                                         "currency": "usd",
                                                         "product_data": {
                                                             "name": item.name
                                                         },
                                                         "unit_amount_decimal": item.price * 100
                                                     },
                                                     "quantity": 1,
                                                 }
                                             ],
                                             mode="payment")
    if not session.id:
        return Response({"message": "There is some problems with getting session_id"}, status=404)
    return Response({'session': session}, status=200)
