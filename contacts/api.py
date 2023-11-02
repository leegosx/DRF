from datetime import date

from django.http import Http404
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'all_contacts': '/contacts/',
        'get_contact_by_id': '/contacts/api-docs/list/?id=1/',
        'get_contact_by_first_name': '/contacts/api-docs/list/?first_name=John/',
        'get_contact_by_last_name': '/contacts/api-docs/list/?last_name=Doe/',
        'get_contact_by_email': '/contacts/api-docs/list/?email=<EMAIL>/',
        'get_contact_by_phone': '/contacts/api-docs/list/?phone=1234567890/',
        'create_contact': '/contacts/create/',
        'update_contact': '/contacts/<int:pk>/update/',
        'delete_contact': '/contacts/<int:pk>/delete/',
    }
    
    return Response(api_urls)

class ContactListApi(generics.ListAPIView):
    """
    ContactListApi provides a ListAPIView for retrieving Contacts.
    
    It filters the queryset based on query parameters for id, first_name, 
    last_name, email, and phone to allow searching.
    
    Raises 404 error if no matching contacts are found.
    """
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Contact.objects.all()
        query_params = self.request.query_params
        
        search_id = query_params.get('id', None)
        search_firstname = query_params.get('first_name', None)
        search_lastname = query_params.get('last_name', None)
        search_email = query_params.get('email', None)
        search_phone = query_params.get('phone', None)
        
        if search_id is not None:
            queryset = queryset.filter(id=search_id)
        elif search_firstname is not None:
            queryset = queryset.filter(first_name__icontains=search_firstname)
        elif search_lastname is not None:
            queryset = queryset.filter(last_name__icontains=search_lastname)
        elif search_email is not None:
            queryset = queryset.filter(email__icontains=search_email)
        elif search_phone is not None:
            queryset = queryset.filter(phone__icontains=search_phone)
            
        if not queryset.exists():
            raise Http404("Contacts not found")
        
        return queryset
    
class ContactCreateApi(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    
class ContactUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    
class ContactDeleteApi(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]