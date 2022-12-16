from rest_framework import serializers
from .models import League, Team, Driver

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = League
        fields = ('id', 'name', 'teams')


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name = 'team_detail',
        read_only=True
    )

    class Meta:
        model = Driver
        fields = ('id', 'name', 'position', 'age', 'years_of_experience', 'teams')
        
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    drivers = DriverSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'division', 'win', 'loss', 'drivers')



