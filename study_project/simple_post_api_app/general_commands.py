"""
http://www.django-rest-framework.org/tutorial/1-serialization/
"""

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from simple_post_api_app.api.serializers import SimplePostSerializer
from simple_post_api_app.models import SimplePost

SimplePost.objects.create(header="my post 1", content="content of my post 1", location="Moscow")
obj = SimplePost.objects.create(header="my post 2", content="content of my post 2", location="Moscow")

# Serialization
obj_ser = SimplePostSerializer(obj)
data_json = JSONRenderer().render(obj_ser.data)

# Deserialization
stream = BytesIO(data_json)
data = JSONParser().parse(stream)

serializer = SimplePostSerializer(data=data)
serializer.is_valid()

serializer.save()


# SUPER USER =========================
from django.contrib.auth.models import User
# create
user=User.objects.create_superuser(username="admin", password="admin", email="p@p.p")
# delete
User.objects.get(username="admin", is_superuser=True).delete()
# ====================================

# TOKEN MODEL
from rest_framework.authtoken.models import Token

# Create
for user_obj in User.objects.all():
    token = Token.objects.create(user=user_obj)

user = User.objects.create_user(username="test", password="test", email="p@p.p")
user.delete()

Token.objects.get(user=user)

User.objects.get(username="test").delete()