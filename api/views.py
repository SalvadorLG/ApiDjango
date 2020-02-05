from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from api.models import Juegos
from api.serializers import JuegosSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwarsg):
        serializer = self.serializer_class(data=request.data, 
                                            context = {'resquest':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
        })

class JuegosList(generics.ListCreateAPIView):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer
