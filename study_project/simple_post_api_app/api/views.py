from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import NotFound, MethodNotAllowed, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from simple_post_api_app.api.serializers import SimplePostSerializer, SignUpSerializer
from simple_post_api_app.models import SimplePost


# =======================================
# Sign Up
# =======================================
@api_view(["POST"])
def sign_up_view(request):

    sign_up_ser = SignUpSerializer(data=request.data)

    if sign_up_ser.is_valid():

        user_obj = sign_up_ser.save()

        response_message = {"status": "OK"}

    else:
        return Response(sign_up_ser.errors)

    return Response(response_message)


# =======================================
# Simple Post List
# =======================================
@api_view(["GET", "POST"])
@authentication_classes((TokenAuthentication,)) #SessionAuthentication
@permission_classes((IsAuthenticated,))
def simple_post_list_view(request):

    # Retrieve a list
    if request.method == "GET":
        post_objs = SimplePost.objects.all()
        post_ser = SimplePostSerializer(post_objs, many=True)
        return Response(post_ser.data)

    # Create a simple post
    elif request.method == "POST":
        post_ser = SimplePostSerializer(data=request.data)
        if post_ser.is_valid():
            post_ser.save()
            return Response(post_ser.data, status=status.HTTP_201_CREATED)
        return Response(post_ser.errors, status=400)


# =======================================
# Simple Post Detail
# =======================================
@api_view(["GET", "PUT", "DELETE"])
@permission_classes((IsAuthenticated,))
def simple_post_detail_view(request, pk=None):

    def get_object(pk=None):
        try:
            obj = SimplePost.objects.get(pk=pk)
        except SimplePost.DoesNotExist:
            raise NotFound(detail="There is no such post", code="not_found")
        return obj

    if pk is None:
        raise ParseError(detail=None, code=None)

    # Get post details
    if request.method == "GET":

        post_obj = get_object(pk)
        post_ser = SimplePostSerializer(post_obj)

        return Response(post_ser.data)

    # Update a post
    elif request.method == "PUT":

        post_obj = get_object(pk)
        post_ser = SimplePostSerializer(data=request.data, instance=post_obj)

        if post_ser.is_valid():
            post_ser.save()
            return Response(status=status.HTTP_200_OK)

        return Response(post_ser.errors, status=status.HTTP_417_EXPECTATION_FAILED)

    # Delete a post
    elif request.method == "DELETE":
        get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    raise MethodNotAllowed(request.method, detail=None, code=None)


# =======================================
# Simple Post List With HTML
# =======================================
class SimplePostHTMLAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "simple_post_template.html"

    def get(self, request):
        queryset = SimplePost.objects.all()
        return Response({"simple_post_list": queryset})