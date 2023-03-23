from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, state_choices
# Create your views here.

def index (request):
    # return all listings
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings, 1)
    page = request.GET.get("page")
    paged_lisiting= paginator.get_page(page)
    
    page=request.GET.get("page")
    return render(request, "listings.html", {"listings": paged_lisiting})

def listing (request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "listing.html", {"listing": listing})
    
    

def search (request):
    queryset_list = Listing.objects.order_by("-list_date")
    # keywords 
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            
    # city
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            
    # state
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            
            
    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings": queryset_list,
        "values": request.GET,
    }
        
    return render(request, "search.html", context)   