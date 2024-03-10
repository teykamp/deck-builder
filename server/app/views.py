from django.http import HttpResponse
from . import models

def index(request):
    return HttpResponse('hello world. yippee!')

def hellodb(request):
    hello_item = models.HelloModel()
    hello_item.id = 0
    hello_item.content = 'hello from the database'
    hello_item.save()

    get_hello_item = models.HelloModel.objects.all()
    first_item = get_hello_item[0]

    return HttpResponse(f'{first_item}')

