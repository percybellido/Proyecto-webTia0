from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (CreateView, ListView)
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Resenas

# Create your views here.
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class ResenasCreateView(CreateView):
    template_name="reviews/reviews.html"
    model=Resenas
    fields=['name','email','message']
    success_url=reverse_lazy('reviews_app:reviews')
    
    
    
class ResenasListView(ListView):
    template_name="reviews/listar_resenas.html"
    model=Resenas
    context_object_name='lista'