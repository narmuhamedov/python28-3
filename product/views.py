from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import DetailView, ListView


class ProductListView(ListView):
    queryset = models.Product.objects.filter().order_by("-id")
    # queryset = models.Product.objects.filter(tag__name='Игры')
    template_name = "product/product_list.html"

    def get_queryset(self):
        return models.Product.objects.filter().order_by("-id")
        # return  models.Product.objects.filter(tag__name='Игры')


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.Product, id=product_id)
