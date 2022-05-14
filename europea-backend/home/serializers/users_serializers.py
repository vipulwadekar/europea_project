from rest_framework import serializers
from home.models.users import Users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id","name", "email","password","created_at"]
        