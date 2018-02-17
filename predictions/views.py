from django.shortcuts import render
from .models import Predictions


# Create your views here.
def pred_list(request):
    preds = Predictions.objects.all().order_by('NAME_T')
    return render(request, 'pred_list_n.html', {'preds': preds})
