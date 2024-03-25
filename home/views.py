
from django.shortcuts import render, HttpResponse

# Create your views here.
# ab humay pata chal gaya eik page se dusray ki taraf kasay jatay hai 
# http://127.0.0.1:8000/services jo page dekhna hai services ki jaga likh do 
def index(request):  
    context = {
        "variable1": "obaid you are to hottttt",
        "variable2": "jamil you are to hottttt"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')






