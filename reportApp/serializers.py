from rest_framework import serializers
from .models import Report
import json
from .page_speed_api import get_data
import re

from users.models import CustomUser
from rest_framework.authtoken.models import Token

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(default=0)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_at = serializers.ReadOnlyField()
    report_data = serializers.ReadOnlyField()
    class Meta:
        model = Report
        fields = ('user', 'url', 'id', 'report_id', 'updated_at', 'report_data')

    def create(self, validated_data):
        search_url = validated_data.get('report_id')
        string = re.match('(?i)(url:|origin:)?http(s)?://.*', search_url)

        if not string:
            err_msg = "urls must match the following example http(s)://example.com/"
            raise serializers.ValidationError({"error": err_msg})

        user = self.context['request'].user
        report_obj = user.report.filter(report_id=search_url).first()
        if report_obj:
            return report_obj

        data = get_data(search_url)
        if data["error"]:
            err_msg = "Unable to get the data for " + search_url
            raise serializers.ValidationError({"error": err_msg})

        str_report_data = json.dumps(data)
        report_obj = user.report.create(user=user, report_id=data["id"], report_data=str_report_data)
        report_obj.save()
        return report_obj


    def update(self, instance, validated_data):
        search_url = validated_data.get('report_id', instance.report_id)
        string = re.match('(?i)(url:|origin:)?http(s)?://.*', search_url)

        if not string:
            err_msg = "urls must match the following example http(s)://example.com/"
            raise serializers.ValidationError({"error": err_msg})

        user = self.context['request'].user
        report_obj = user.report.filter(report_id=search_url).exclude(id=instance.id).first()
        if report_obj:
            err_msg = "A report with this URL already exists"
            raise serializers.ValidationError({"error": err_msg})

        data = get_data(search_url)
        if data["error"]:
            err_msg = "Unable to get the data for " + search_url
            raise serializers.ValidationError({"error": err_msg})

        str_report_data = json.dumps(data)
        instance.report_id = search_url
        instance.report_data = str_report_data
        instance.save()
        return instance

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

