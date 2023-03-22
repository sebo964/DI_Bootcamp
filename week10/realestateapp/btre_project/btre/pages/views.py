from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
        
        listings = Listing.objects.order_by("-list_date").filter(is_published=True)
        paginator = Paginator(listings, 4)
        page = request.GET.get("page")
        paged_lisiting= paginator.get_page(page)
        return render(request, "home.html", {"listings": paged_lisiting})


def about(request):
    realtors_db = Realtor.objects.order_by("-hire_date")
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = { "realtors": realtors_db, "mvp_realtors": mvp_realtors}
    return render(request, "about.html", context)
