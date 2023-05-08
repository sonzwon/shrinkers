from django.contrib.auth.models import User
from shortener.models import Users, ShortenedUrls
from rest_framework import serializers
from shortener.utils import url_count_changer


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class UserSerializer(serializers.ModelSerializer):
    user = UserBaseSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ["id", "url_count", "organization", "user"]


class UrlListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = ShortenedUrls
        fields = "__all__"


class UrlCreateSerializer(serializers.ModelSerializer):
    nick_name = serializers.CharField(max_length=50)
    target_url = serializers.CharField(max_length=2000)
    category = serializers.IntegerField(required=False)

    def create(self, request, data, commit=True):
        inst = ShortenedUrls
        inst.creator_id = request.user.id
        inst.category = data.get("category", None)
        inst.target_url = data.get("target_url").strip()
        if commit:
            try:
                inst.save()
            except Exception as e:
                print(e)
            else:
                url_count_changer(request, True)
        print(inst)
        return inst
