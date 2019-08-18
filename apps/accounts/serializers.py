from rest_framework import serializers
from apps.accounts.models import User, UserProfile
from apps.news.serializers import NewsSerializer


class UserNewsSerializer(serializers.ModelSerializer):
    newses = NewsSerializer(many=True)

    class Meta:
        model =User
        fields=('pk','username','email','newses')



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("address", "dob")


class CreateUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()


    class Meta:
        model= User
        fields= ('pk','username','email','password','first_name','last_name','role','profile')
        extra_kwargs= {"password":{"write_only":True}}



    def create(self, validate_data):
        profile_data = validate_data.pop("profile")
        raw_password = validate_data.pop("password")
        user = User(**validate_data)
        user.set_password(raw_password)
        user.save()

        UserProfile.objects.create(**profile_data, user=user)
        return user

class UpdateUserSerailizer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model= User
        exclude= ('username', 'email')
        extra_kwargs= {"password":{"write_only":True}}
    
    def update(self, instance, validate_data):
        profile= instance.profile
        profile_data= validate_data.pop('profile')
        profile.dob=validate_data.get('dob', profile.dob)
        profile.address=profile_data.get('address', profile.address)
        profile.save()

        instance.first_name= validate_data.get('first_name', instance.first_name)
        instance.last_name= validate_data.get('last_name', instance.last_name)
        instance.role= validate_data.get('role', instance.role)
        if validate_data.get('password'):
            instance.set_password(validate_data.get('password'))
        instance.save()
        return instance


