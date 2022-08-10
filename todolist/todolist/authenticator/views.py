from django.http import JsonResponse

from rest_framework import generics,permissions


from .serializers import LoginSerializer, UserSerializer
from .models import User
import bcrypt

# Create your views here.

class UserAuthenticator(generics.GenericAPIView):
  authentication_classes=[]
  serializer_class = LoginSerializer
  def post(self,request):
      email = request.data.get("email")
      password = request.data.get("password")
      if password:
        obj = User.objects.get(email = email)
        if obj and bcrypt.checkpw(password.encode(), obj.password.encode()):
            serializer = self.serializer_class(obj)
            return JsonResponse(serializer.data)
        else:
          return JsonResponse({"status": "Inválid Password or Username"},status=402)
      return JsonResponse({})
      
user_auth_view = UserAuthenticator.as_view()

class UserCreateView(generics.CreateAPIView):
  authentication_classes=[]

  serializer_class = UserSerializer

  def perform_create(self, serializer):
    password = serializer.validated_data.get('password')
    
    if password:
      hashed = bcrypt.hashpw(password.encode('utf8'),bcrypt.gensalt())
      serializer.save(password = hashed.decode('utf8'))
      
create_user_view = UserCreateView.as_view()
  
class UserDetailView(generics.GenericAPIView):
  permission_classes=(permissions.IsAuthenticated,)
  
  def get(self,request):
    user = request.user
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)
  
detail_user_view = UserDetailView.as_view()  

class UserActivateView(generics.UpdateAPIView): 
  authentication_classes=[]
  serializer_class = UserSerializer
  queryset = User.objects.all()
  def perform_update(self, serializer):
    params = self.request.data
    
    user_id = params.user_id
    confirmation_token = params.confirmation_token
    
    try:
      user = self.get_queryset().get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
      user = None
    
    if not user:
       return JsonResponse('User not found',status = 400)
    if not default_token_generator.check_token(user, confirmation_token):
      return JsonResponse('Token is invalid or expired',status = 400)
  
    serializer.save(is_active = True)
    return JsonResponse({'status': 'Email successfully confirmed'},status = 200)
    #serializer.save(validated = True)
    
activate_user_view = UserActivateView.as_view()

