from django.db import models

class Game(models.Model):
    game_title = models.CharField(max_length=50)
    game_description = models.CharField(max_length=200)
    image_url = models.URLField()
    game_url = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # __unicode__ on Python 2
        return "game title : " + self.game_title + ", url : " + str(self.game_url)
