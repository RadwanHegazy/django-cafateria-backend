from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User

class profile_view (APIView) : 
    permission_classes = [permissions.IsAuthenticated] 

    def get (self,request,**kwargs) : 
        user:User = request.user
        data = {
            'full_name' : user.full_name,
            'email' : user.email,
            'picture' : user.picture.url,
            'has_cafateria' : False
        }

        if user.cafateria :
            data['has_cafateria'] = True
            data['cafateria'] = {
                'name' : user.cafateria.name,
                'orders' : '', # get all order that not finished for that cafateria
            }

        return Response(data,status=status.HTTP_200_OK)
        