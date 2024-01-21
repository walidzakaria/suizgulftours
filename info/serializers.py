from rest_framework import serializers
from .models import Tblguestinfo, Tblhotel, Tblnationality

class HotelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblhotel
        fields = ('hotelid', 'hotel', )


class NationalitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblnationality
        fields = ('nationalityid', 'nationality', )


class GuestInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tblguestinfo
        fields = ('guestinfoid', 'arrivaldate', 'departuredate', 'guestname', 'viawhatsapp',
                  'genderfemale', 'mailaddress', 'cityresidence', 'country', 'whatsappphone',
                  'phoneegypt', 'dateofbirth', 'hotelname', 'adult', 'child', 'inf', )
