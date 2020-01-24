from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank
)
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.offerings.models import Offerings
from api.webpages.models import Webpage
from api.authentication.serializers import UserSerializer
from api.authentication.models import User
from api.permissions import IsOwnerOrReadOnly

class SearchAPIView(APIView):
    """Full-text Search functionality for webpages"""
    def get(self, request, format=None):
        query_search_vector = SearchVector('title', 'description')
        location_search_vector = SearchVector('address', 'city', 'state', 'country')
        query_search_query = SearchQuery(request.query_params.get('query'))
        location_search_query = SearchQuery(request.query_params.get('location'))
        search_rank = SearchRank(query_search_vector, query_search_query)

        offering_search_result = Offerings.objects.annotate(
            rank=search_rank,
            search=query_search_vector
        ).filter(
            search=query_search_query
        ).order_by(
            '-rank'
        ).values(
            'id',
            'title',
            'description',
            'image',
            'price',
            'associated_webpage',
            'created_at',
        ).distinct()

        location_search_result = Webpage.objects.annotate(
            search=location_search_vector
        ).filter(
            search=location_search_query
        ).values(
            'id',
            'title',
            'description',
            'sub_domain_name',
            'state',
            'city',
            'address',
            'country',
            'is_active',
            'verified_business',
            'featured_images',
            'colour'
        ).distinct()

        search_result = []
        for offering in offering_search_result:
            for webpage in location_search_result:
                if offering['associated_webpage'] == webpage['id']:
                    offering['business_name'] = webpage['title']
                    offering['sub_domain_name'] = webpage['sub_domain_name']
                    offering['business_tagline'] = webpage['description']
                    offering['country'] = webpage['country']
                    offering['state'] = webpage['state']
                    offering['city'] = webpage['city']
                    offering['address'] = webpage['address']
                    offering['is_active'] = webpage['is_active']
                    offering['verified_business'] =  webpage['verified_business']
                    offering['colour'] = webpage['colour']
                    search_result.append(offering)

        return Response(search_result)

LOOKUP_FIELD='username'
class RetrieveUpdateUserAPIView(generics.RetrieveUpdateAPIView):
    """View for updating and getting a user's profile"""
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = LOOKUP_FIELD

    def perform_update(self, serializer):
        """Update a user profile"""
        serializer.save(user=self.request.user)
