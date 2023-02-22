from rest_framework import mixins, generics
from .serializers import PortfolioSerializer
from .models import Portfolio, Dividend
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PortfolioListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PortfolioSerializer

    def get_permission_class(self):
        if self.request.method == 'POST':
            return [IsAuthenticated]
        return 

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Portfolio.objects.filter(member_id = pk).order_by('-id')

    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

