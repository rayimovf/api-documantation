from rest_framework import serializers
from .models import Info, Services, About, Portfolio, Testimonials, Clients, Contact


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

