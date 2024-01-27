from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Info, Services, About, Portfolio, Testimonials, Clients, Contact
from .serializer import InfoSerializer, ServicesSerializer, AboutSerializer, PortfolioSerializer, TestimonialsSerializer, ClientsSerializer, ContactSerializer


@api_view(['GET'])
def get_info_view(request):
    if request.method == 'GET':
        return Response(InfoSerializer(Info.objects.last()).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_services_view(request):
    if request.method == 'GET':
        return Response(ServicesSerializer(Services.objects.all(), many=True).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_about_view(request):
    if request.method == 'GET':
        return Response(AboutSerializer(About.objects.last()).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_portfolio_view(request):
    if request.method == 'GET':
        return Response(PortfolioSerializer(Portfolio.objects.all(), many=True).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_testimonials_view(request):
    if request.method == 'GET':
        return Response(TestimonialsSerializer(Testimonials.objects.all(), many=True).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_clients_view(request):
    if request.method == 'GET':
        return Response(ClientsSerializer(Clients.objects.all(), many=True).data)
    else:
        return Response({"message": "Error"})


@api_view(['GET'])
def get_contact_view(request):
    if request.method == 'GET':
        return Response(ContactSerializer(Contact.objects.all(), many=True).data)
    else:
        return Response({"message": "Error"})


@api_view(['POST'])
def post_contact_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)
        return Response({"message": "saved"})
    else:
        return Response({"message": "Error"})









