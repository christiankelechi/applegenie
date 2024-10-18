#!/usr/bin/env python3
from core_app_root.security.settings_and_privacy.models import MatchPreferenceModel, CausesModel, QualitiesValueModel, SettingPrivacyModel
from rest_framework import serializers


class MatchPreferenceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchPreferenceModel
        fields = '__all__'
        
class CausesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CausesModel
        fields = '__all__'

class QualitiesValueModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = QualitiesValueModel
        fields = '__all__'        

class SettingPrivacyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SettingPrivacyModel
        fields = '__all__'