from theater_lab.models import Play

class PlayRepository:
    def get_all(self):
        return Play.objects.all()

    def get_by_id(self, play_id):
        return Play.objects.get(id=play_id)

    def create(self, title, genre, duration, premiere_date, director=None):
        play = Play(title=title, genre=genre, duration=duration, premiere_date=premiere_date, director=director)
        play.save()
        return play