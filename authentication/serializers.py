from rest_framework import serializers

from authentication.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username',"email","phone_number","password"]

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs["username"]).exists()
        email_exists=User.objects.filter(email=attrs["email"]).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Un Utilisateur avec ce nom existe déja")

        if email_exists:
            raise serializers.ValidationError(detail="Un Utilisateur avec cet email existe déja")

        return super().validate(attrs)