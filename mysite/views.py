from django.shortcuts import render
from .models import MainContent
def index(request):
    Index = MainContent.objects.order_by('-pub_date')
    context={'Index':Index}
    return render(request, 'mysite/Index.html',context)
