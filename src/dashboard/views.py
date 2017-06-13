from django.views.generic import View
from django.shortcuts import render

# Create your views here.
from products.models import Product, CuratedProducts

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        tag_views = None
        products = None
        top_tags = None
        curated = CuratedProducts.objects.filter(active=True)
        try:
            tag_views = request.user.tagview_set.all().order_by("-count")[:5]
        except:
            pass

        owned = None
        try:
            owned = request.user.myproducts.products.all()
        except:
            pass

        if tag_views:
            top_tags = [x.tag for x in tag_views]
            products = Product.objects.filter(tag__in=top_tags)

        context = {
            "products": products,
            "top_tags": top_tags,
            "curated": curated,
        }
        return render(request, "dashboard/view.html", context)
