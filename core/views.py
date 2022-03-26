from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")
def about(request):
    return render(request,"core/about.html")

def request_a_quote(request):
    return render(request,"core/Request_a_quote.html")
def deals(request):
    return render(request,"core/deals.html")


