from rest_framework import serializers
from account.models import Account


class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our user profile objects."""
    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""
        user = Account(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
