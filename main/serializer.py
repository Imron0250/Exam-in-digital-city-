from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Product
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class EmailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emails
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"


class ClientSaysSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientSays
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = "__all__"

class OurStoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurStories
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = "__all__"

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_active']


class WishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"



class ProductPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPhoto
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInfo
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"    


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"    

    




