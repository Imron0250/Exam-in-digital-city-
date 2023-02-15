from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def login_view(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'success': True,
                'user': {
                    "id": user.id,
                    "username": user.username,
                    'token': token.key,
                }
            }
        else:
            data = {
                "success": False,
                "error": "Username or password error!"
            }

    except Exception as err:
        data = {
            "success": False,
            "error": f'{err}'
        }
    return Response(data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def clearcard(request):
    user = request.user
    Card.objects.filter(user=user).delete()
    return Response("Clear card passed very well")


@api_view(["GET"])
def get_slider(request):
    product = Product.objects.filter(in_slider=True).order_by('-id')[:3]
    ser = ProductSerializer(product, many=True).data
    return Response(ser)


@api_view(["GET"])
def get_category(request):
    category = Category.objects.all()
    ser = CategorySerializer(category, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_ad_product(request):
    product = Product.objects.filter(in_ad=True).last()
    ser = ProductSerializer(product)
    return Response(ser.data)

@api_view(["GET"])
def get_product(request):
    product = Product.objects.all()
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)

@api_view(["GET"])
def get_service(request):
    service = Service.objects.all()
    ser = ServiceSerializer(service, many = True)
    return Response(ser.data)

@api_view(['GET'])
def get_product_by_category(request, pk):
    product = Product.objects.filter(category_id=pk)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_blog(request):
    blog = Blog.objects.all().order_by('-id')[:3]
    ser = BlogSerializer(blog, many=True)
    return Response(ser.data)

k

@api_view(['GET'])
def get_single_product(request, pk):
    product = Product.objects.get(id=pk)
    ser = ProductSerializer(product)
    return Response(ser.data)


@api_view(['GET'])
def get_blog_details(request, pk):
    blog = Blog.objects.get(id=pk)
    ser = BlogSerializer(blog)
    return Response(ser.data)

@api_view(['GET'])
def get_team(request):
    team = Team.objects.all()
    ser = TeamSerializer(team, many=True)
    return Response(ser.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_message(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    Contact.objects.create(name=name)
    Contact.objects.create(email=email)
    Contact.objects.create(subject=subject)
    Contact.objects.create(message=message)
    return Response('Send contact passed very well')

@api_view(['GET'])
def get_client_say(request):
    say = ClientSays.objects.all()
    ser = ClientSaysSerializer(say, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_logo(request):
    logo = Partner.objects.all()
    ser = PartnerSerializer(logo, many=True)
    return Response(ser.data)

@api_view(['GET'])
def get_partner(request):
    part = Partner.objects.all()
    ser = PartnerSerializer(part, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_emails(request):
    email = request.POST.get('email')
    e = Emails.objects.create(email=email)
    ser = EmailsSerializer(e)
    return Response(ser.data)

@api_view(['GET'])
def get_info(request):
    info = Info.objects.last()
    ser = InfoSerializer(info)
    return Response(ser.data)


@api_view(['GET'])
def get_faq(request):
    about = Faq.objects.all()
    ser = FaqSerializer(about, many=True)
    return Response(ser.data)



@api_view(['GET'])
def get_product_by_price(request):
    minimum = request.GET.get('min')
    maximun = request.GET.get('max')
    product = Product.objects.filter(price__gte=minimum, price__lte=maximun)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def search_producy(request):
    q = request.GET.get('q')
    product = Product.objects.filter(name__icontains=q)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data) 


@api_view(['GET'])
def get_product_by_reating(request):
    reating = request.GET.get('reating')
    product = Product.objects.filter(rating__gte=reating, rating__lte=reating)
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)    


@api_view(['POST'])
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    if User.objects.filter(username=username).count() > 0:
        return Response('Bunday user mavjud')
    u = User.objects.create_user(username=username, email=email)
    u.set_password(password)
    ser = UserSerializer(u)
    return Response(ser.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_wishlist(request):
    user = request.user
    product = request.POST.get('product')
    w = Wishlist.objects.create(user=user, product_id=product)
    ser = WishlistSerializer(w)
    return Response(ser.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_card(request):
    user = request.user
    product = request.POST.get('product')
    w = Card.objects.create(user=user, product_id=product)
    ser = CardSerializer(w,)
    return Response(ser.data)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_delete(requset, pk):
    name = requset.POST.get("name")
    cat = Wishlist.objects.get(id=pk)
    cat.name = name
    cat.delete()
    return Response('Delete passed very welll')



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def card_delete(requset, pk):
    name = requset.POST.get("name")
    cat = Card.objects.get(id=pk)
    cat.name = name
    cat.delete()
    return Response('Delete passed very welll')

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def card_edit(requset, pk):
    name = requset.POST.get("name")
    cat = Card.objects.get(id=pk)
    cat.name = name
    cat.save() 
    return Response('Edit passed very well')

import datetime


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    order = Order.objects.create(user=user, date=datetime.now(), total_price =0)
    card = Card.objects.filter(user=user)
    for i in card:
        OrderItem.objects.filter(
            order = order,
            product = i.product,
            quantity = i.quantity,
            price = i.product.bonus if i.product.bonus > 0 else i.product.price
        )
        order.total_price += i.quantity * i.product.bonus if i.product.bonus > 0 else i.product.price
        order.save()

    card = Card.objects.filter(user=user).delete(
        
    )
    return Response({'success': True})



@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order(request):
    user = request.user
    order = Order.objects.filter(user=user)
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_order_items(request, pk):
    order = Order.objects.get(id=pk)
    if order.user == request.user:
        items = OrderItem.objects.filter(order=order)
        ser = OrderItemSerializer(items, many=True)
        return Response(ser.data)
    else:
        return Response({"seccess": False})

@api_view(['PUT'])
def edit_user_info(request):
    user = request.user
    email = request.POST.get('email')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get("last_name")
    user.last_name = last_name
    user.fist_name = first_name
    user.email = email
    user.set_password(password)
    user.save()
    return Response({"success": False})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_wishlist(request):
    user = request.user
    wish = Wishlist.objects.filter(user=user)
    ser = WishlistSerializer(wish, many=True)
    return Response(ser.data)