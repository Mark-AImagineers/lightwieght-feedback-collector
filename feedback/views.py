from django.shortcuts import render, redirect
from .models import Business
from .forms import BusinessForm
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

def events_view(request):
    template = "pages/home/events.html"
    context = {}
    return render(request, template, context)

def qrcodes_view(request):
    template = "pages/home/qrcodes.html"
    context = {}
    return render(request, template, context)
