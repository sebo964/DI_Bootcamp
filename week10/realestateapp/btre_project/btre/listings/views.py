from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    return render(request, "search.html")