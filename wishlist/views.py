from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from collections import defaultdict

def group_by_brand(items):
    grouped = defaultdict(list)
    for item in items:
        grouped[item.brand].append(item)
    return dict(sorted(grouped.items()))  # alphabetize brands

def group_by_type(items):
    grouped = defaultdict(list)
    for item in items:
        grouped[item.type].append(item)
    return dict(sorted(grouped.items()))

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(preference__in=["favorite", "alternative"])
    giftcard_items = WishlistItem.objects.filter(preference="giftcard")

    wishlist = group_by_type(wishlist_items)
    giftcards = group_by_type(giftcard_items)

    return render(request, 'wishlist/view.html', {
        'wishlist': wishlist,
        'giftcards': giftcards,
    })

@login_required
def mark_purchased(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id)
    item.purchased = True
    item.save()
    return redirect('wishlist:view_wishlist')
