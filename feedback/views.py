from django.shortcuts import render, redirect
from .models import Business, Event
from .forms import BusinessForm, EventForm
from django.contrib.auth.decorators import login_required

@login_required
def businesses_view(request):
    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = request.user
            business.save()
            return redirect("businesses")
    else:
        form = BusinessForm()

    user_businesses = Business.objects.filter(owner=request.user)
    template = "pages/home/businesses.html"
    context = {
        "form": form,
        "businesses": user_businesses,
    }

    return render(request, template, context)

@login_required
def events_view(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect("events")
        
    else:
        form = EventForm()

    user_events = Event.objects.filter(owner=request.user)

    template = "pages/home/events.html"
    context = {
        "form": form,
        "events": user_events,
    }
    return render(request, template, context)

def qrcodes_view(request):
    template = "pages/home/qrcodes.html"
    context = {}
    return render(request, template, context)
