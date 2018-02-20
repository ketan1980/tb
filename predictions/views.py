from django.shortcuts import render
from .models import Predictions


# Create your views here.
def pred_list(request):
    preds = Predictions.objects.all().order_by('NAME_T')
    return render(request, 'pred_list_n.html', {'preds': preds})


def spider_chart(request, pk):
    stats = Predictions.objects.get(id=pk)
    return render(request, 'spider_ajax.html', {'stats': stats})
