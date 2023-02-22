from rest_framework import mixins, generics
from .serializers import PortfolioSerializer, PortfolioDetailSerializer
from .models import Portfolio, Dividend
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PortfolioListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = PortfolioSerializer

    def get_queryset(self):
        portfolios = Portfolio.objects.all().order_by('-id')
        return portfolios

    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class PortfolioDetailView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = PortfolioDetailSerializer

    def get_queryset(self):
        # member_id = self.kwargs.get('member_id')
        
        if self.request.user.id:
            return Portfolio.objects.filter(member_id=self.request.user.id) \
                .select_related('member') \
                .order_by('-id')
        return Portfolio.objects.none()
    
    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
