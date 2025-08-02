from django.shortcuts import render

def businesses_view(request):
    template = "pages/home/businesses.html"
    context = {}
    return render(request, template, context)

def events_view(request):
    template = "pages/home/events.html"
    context = {}
    return render(request, template, context)

def qrcodes_view(request):
    template = "pages/home/qrcodes.html"
    context = {}
    return render(request, template, context)
