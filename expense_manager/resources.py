# core django
from django.contrib.auth.models import User

# project
from .models import Expense, Budget

# third party
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class BudgetResource(ModelResource):

    # filter obj for logged in user
    def get_object_list(self, request):
        return super(BudgetResource, self).get_object_list(request).filter(user=request.user)

    # store obj based on logged in
    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle
    # get detail obj direct

    def render_detail(self, request, pk):
        resp = self.get_detail(request, pk=pk)
        return resp.content
    # get list direct

    def render_list(self, request):
        resp = self.get_list(request)
        return resp.content

    class Meta:
        queryset = Budget.objects.all()
        resource_name = 'budget'
        authorization = DjangoAuthorization()
        filtering = {
            'budget': ALL,
            'month': ALL,
        }
        ordering = ['month']
        excludes = ('created', 'modified',)


class ExpenseResource(ModelResource):

    # filter obj for logged in user
    def get_object_list(self, request):
        if request.GET.get('photos') == "-1":
            return super(ExpenseResource, self).get_object_list(request).filter(user=request.user).exclude(photo__exact='')
        return super(ExpenseResource, self).get_object_list(request).filter(user=request.user)

    # store obj based on logged in
    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle
    # get detail obj direct

    def render_detail(self, request, pk):
        resp = self.get_detail(request, pk=pk)
        return resp.content
    # get list direct

    def render_list(self, request):
        resp = self.get_list(request)
        return resp.content
    
    

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        authorization = DjangoAuthorization()
        filtering = {
            'name': ALL,
            'price': ALL,
            'photo': ALL,
            'created': ['exact', 'range', 'gte']
        }
        ordering = ['name','price']
        excludes = ('modified')
