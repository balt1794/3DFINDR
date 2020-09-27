from django.shortcuts import render, redirect
from .forms import ListingForm, CustomerForm
from .models import Listing, Customer
from .filters import ListingFilter
from django.core.paginator import Paginator
from .decorators import unauthenticated_listings


# HOMEPAGE DONE
def index(request):
    # Listings Page
    return render(request, 'listings/index.html')


def careers(request):
    # Listings Page
    return render(request, 'listings/careers.html')


def faq(request):
    # Listings Page
    return render(request, 'listings/faq.html')


def new_index(request):
    # Listings Page
    return render(request, 'listings/new_index.html')
# ADD THE ID FOR EACH USER


@unauthenticated_listings
def my_listings(request):

    my_listings = request.user.listing_set.order_by('-list_date')
    context = {'my_listings': my_listings}
    return render(request, 'listings/my_listings.html', context)

# LISTINGS DONE


def all_listings(request):

    my_Filter = ListingFilter(
        request.GET, queryset=Listing.objects.order_by('-list_date'))
    # all_listings = Listing.objects.order_by('-list_date')

    # my_Filter = ListingFilter(request.GET, queryset=all_listings)
    # all_listings = my_Filter.qs

    # paginator = Paginator(all_listings, 3)
    # page = request.GET.get('page')
    # all_listings = paginator.get_page(page)

    # context = {'all_listings': all_listings,
    #          'my_Filter': my_Filter}
    paginated_filter = Paginator(my_Filter.qs, 3)

    page_number = request.GET.get('page')
    listing_page_obj = paginated_filter.get_page(page_number)

    context = {"my_Filter": my_Filter,
               "listing_page_obj": listing_page_obj}
    return render(request, 'listings/all_listings.html', context)


@unauthenticated_listings
def new_listing(request):
    if request.method != 'POST':
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = request.user
            instance.save()
            return redirect('listings:all_listings')

    context = {'form': form}
    return render(request, 'listings/new_listing.html', context)


def detail(request, detail_id):
    detail = Listing.objects.get(id=detail_id)
    context = {'detail': detail, 'all_listings': all_listings}
    return render(request, 'listings/detail.html', context)


@unauthenticated_listings
def edit_listing(request, detail_id):
    listing = Listing.objects.get(id=detail_id)

    if request.method != 'POST':
        form = ListingForm(instance=listing)
    else:
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings:my_listings')

    context = {'listing': listing, 'form': form}
    return render(request, 'listings/edit_listing.html', context)


@unauthenticated_listings
def delete_listing(request, detail_id):
    listing = Listing.objects.get(id=detail_id)

    if request.method == 'POST':
        listing.delete()
        return redirect('listings:my_listings')

    context = {'listing': listing}
    return render(request, 'listings/delete_listing.html', context)


@unauthenticated_listings
def profile(request):
    if request.method != 'POST':
        form = CustomerForm()
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('listings:my_profile')

    context = {'form': form}
    return render(request, 'listings/profile.html', context)

# SEE MY PROFILE DONE


@unauthenticated_listings
def my_profile(request):
    my_profile = request.user.customer
    usert = request.user
    # customer = request.user.customer

    context = {'my_profile': my_profile, 'usert': usert}
    return render(request, 'listings/my_profile.html', context)


@unauthenticated_listings
def edit_profile(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method != 'POST':
        form = CustomerForm(instance=customer)
    else:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('listings:my_profile')

    context = {'customer': customer, 'form': form}
    return render(request, 'listings/edit_profile.html', context)
