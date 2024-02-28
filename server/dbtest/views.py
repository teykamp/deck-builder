from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .models import Text


def index(request):
    text_list = list(Text.objects.all().values_list('text', flat=True))
    return HttpResponse("No items added." if len(text_list) == 0 else text_list)


@csrf_exempt
def submit(request):
    if request.method == 'POST':
        Text.objects.create(text=request.POST)
    return render(request, "dbtest/index.html")
