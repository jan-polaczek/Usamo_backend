from datetime import date

from account.models import DefaultAccount, Address
from account.serializers import AddressSerializer
from rest_framework import serializers

from .models import *


class JobOfferCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOfferCategory
        fields = ['name']


class JobOfferTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOfferType
        fields = ['name']


class JobOfferSerializer(serializers.ModelSerializer):
    voivodeship = serializers.ChoiceField(choices=Voivodeships.choices)
    company_address = AddressSerializer()
    category = serializers.CharField(source='category.name')
    type = serializers.CharField(source='offer_type.name')

    def validate_expiration_date(self, value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError("Date is in past")
        return value

    class Meta:
        model = JobOffer
        fields = ['id', 'offer_name', 'category', 'type', 'company_name', 'company_address', 'voivodeship', 'expiration_date',
                  'description']

    def create(self, validated_data):
        validated_data['category'] = JobOfferCategory.objects.get(**validated_data['category'])
        validated_data['offer_type'] = JobOfferType.objects.get(**validated_data['offer_type'])
        company_address = Address.objects.create(**validated_data['company_address'])
        validated_data['company_address'] = company_address
        return JobOffer(**validated_data)


class JobOfferEditSerializer(serializers.Serializer):
    offer_name = serializers.CharField(max_length=50, required=False)
    category = serializers.CharField(max_length=30, required=False)
    type = serializers.CharField(max_length=30, required=False)
    company_name = serializers.CharField(max_length=120, required=False)
    company_address = AddressSerializer(required=False)
    voivodeship = serializers.CharField(max_length=30, required=False)
    expiration_date = serializers.DateField(required=False)
    description = serializers.CharField(max_length=1000, required=False)

    def create(self, validated_data):
        if 'category' in validated_data:
            validated_data['category'] = JobOfferCategory.objects.get(name=validated_data.pop('category'))
        if 'type' in validated_data:
            validated_data['offer_type'] = JobOfferType.objects.get(name=validated_data.pop('type'))
        return JobOfferEdit(**validated_data)

    def update(self, instance, validated_data):
        try:
            instance.category = JobOfferCategory.objects.get(name=validated_data.get('category', None))
        except JobOfferCategory.DoesNotExist:
            pass

        try:
            instance.offer_type = JobOfferType.objects.get(name=validated_data.get('type', None))
        except JobOfferType.DoesNotExist:
            pass

        instance.offer_name = validated_data.get('offer_name', instance.offer_name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        new_address_data = validated_data.get('company_address')
        if new_address_data:
            new_address = Address.objects.create(**new_address_data)
            instance.company_address.delete()
            instance.company_address = new_address
        instance.voivodeship = validated_data.get('voivodeship', instance.voivodeship)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
        instance.description = validated_data.get('description', instance.description)
        return instance


class JobOfferFiltersSerializer(serializers.Serializer):
    voivodeship = serializers.CharField(max_length=30, required=False)
    min_expiration_date = serializers.DateField(required=False)
    categories = serializers.ListField(child=serializers.CharField(max_length=30), required=False)
    types = serializers.ListField(child=serializers.CharField(max_length=30), required=False)

    def create(self, validated_data):
        return JobOfferFilters(**validated_data)

    def update(self, instance, validated_data):
        instance.voivodeship = validated_data.get('voivodeship', instance.voivodeship)
        instance.min_expiration_date = validated_data.get('min_expiration_date', instance.min_expiration_date)
        instance.categories = validated_data.get('categories', instance.categories)
        instance.types = validated_data.get('types', instance.types)
        return instance


class JobOfferApplicationSerializer(serializers.ModelSerializer):
    cv_url = serializers.CharField(source='cv.document.url', read_only=True)
    user_id = serializers.UUIDField(source='cv.cv_user.user.id', read_only=True)
    first_name = serializers.CharField(source='cv.cv_user.user.first_name', read_only=True)
    last_name = serializers.CharField(source='cv.cv_user.user.last_name', read_only=True)
    email = serializers.CharField(source='cv.cv_user.user.email', read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = JobOfferApplication
        fields = ['cv', 'job_offer', 'cv_url', 'user_id', 'first_name', 'last_name', 'email', 'date_posted']
        extra_kwargs = {
            'cv': {'write_only': True}
        }