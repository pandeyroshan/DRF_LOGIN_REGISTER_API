from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAutheticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes((IsAutheticated,))
def login(request):
    params=request.data
    username = params["username"]
    password = params["password"]
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    params=request.data
    username = params["username"]
    email = params["email"]
    password = params["password"]
    try:
        user = User.objects.create_user(username, email, password)
        print(user)
        return Response({'message':'success'},status=HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"message":"Error"}, status=HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)