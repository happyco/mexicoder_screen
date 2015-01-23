from django.db import models


class League(models.Model):
    league_name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.league_name


class Team(models.Model):
    league_team = models.ForeignKey(League)
    team_name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.team_name


class Person(models.Model):
    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )
    
    country = models.CharField(
        max_length=255,
    )
    
    team_name = models.ForeignKey(Team)

    coach = models.BooleanField()

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])
