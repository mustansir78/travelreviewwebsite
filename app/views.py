from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Item, Review
from .forms import ReviewForm


def home(request):
    return redirect(reverse_lazy("hotels"))


class ItemListFilterByHotelView(ListView):
    model = Item
    reviews = Review
    template_name = "app/list.html"
    queryset = Item.objects.filter(type='HOTEL')


class ItemListFilterByTouristAttractionView(ListView):
    model = Item
    template_name = "app/list.html"
    queryset = Item.objects.filter(type='TOURIST_ATTRACTION')


class ItemListFilterByConcertView(ListView):
    model = Item
    template_name = "app/list.html"
    queryset = Item.objects.filter(type='CONCERT')


class ItemListFilterByAmusementParkView(ListView):
    model = Item
    template_name = "app/list.html"
    queryset = Item.objects.filter(type='AMUSEMENT_PARK')


class ItemView(DetailView):
    model = Item
    template_name = "app/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]

        form = ReviewForm()
        item = get_object_or_404(Item, pk=pk)
        reviews = item.review_set.all()

        context["item"] = item
        context["reviews"] = reviews
        context["form"] = form

        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        item = Item.objects.filter(id=self.kwargs["pk"])[0]
        reviews = item.review_set.all()

        context["item"] = item
        context["reviews"] = reviews
        context["form"] = form

        if form.is_valid():
            reviewed_by = form.cleaned_data["reviewed_by"]
            reviewed_by_email = form.cleaned_data["reviewed_by_email"]
            review_body = form.cleaned_data["review"]

            review = Review.objects.create(
                reviewed_by=reviewed_by, reviewed_by_email=reviewed_by_email, review=review_body,
                reviewed_on=datetime.now(), item=item
            )

            form = ReviewForm()
            context["form"] = form

            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


# class AddReviewView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = "app/add_review.html"
#     # fields = "__all__"  # ["item", "reviewed_by", "reviewed_by_email", "review", "reviewed_on"]
#
#     def form_valid(self, form):
#         form.instance.item_id = self.kwargs['pk']
#         form.instance.reviewed_on = datetime.now()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy("item_detail", kwargs={'pk': self.kwargs['pk'], "item": self.model.item_detail})

