from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    match_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name}"

    def get_match_status(self):
        if self.status == 'مستقبل':
            return f"{self.match_time.strftime('%Y-%m-%d %H:%M')}"
        elif self.status == 'قيد التنفيذ':
            return "المباراة جارية"
        else:
            return f"{self.home_score} - {self.away_score}"
