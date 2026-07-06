from rest_framework import serializers
from .models import User


class CurrentUserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="get_full_name", read_only=True)
    is_manager = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "username",
            "email",
            "phone",
            "avatar",
            "is_manager",
        )

    def get_is_manager(self, obj):
        return bool(obj.is_superuser or hasattr(obj, 'managerprofile'))
