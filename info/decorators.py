# from functools import wraps
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework import status
# import base64

# from .models import Tblusers

# def IsAuthenticated(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         # Check if the Authorization header is present
#         authorization_header = request.headers.get('Authorization', '')

#         if not authorization_header.startswith('Basic '):
#             # If the header is not present or not in the correct format, return an unauthorized response
#             return HttpResponse(401)

#         # Decode the base64-encoded credentials
#         encoded_credentials = authorization_header[6:]
#         decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')

#         # Extract the username and password
#         username, password = decoded_credentials.split(':', 1)

#         # Authenticate the user
#         user = Tblusers.objects.filter(
#                 username=username,
#                 userpassword__exact=password
#             ).first()
            
#         if not user:
#             # If authentication fails, return an unauthorized response
#             return HttpResponse(401)
#         print('user', user.username)
#         # Set the authenticated user on the request object
#         # request.user = user

#         # Call the original DRF view function
#         return view_func(request, *args, **kwargs)

#     return wrapper