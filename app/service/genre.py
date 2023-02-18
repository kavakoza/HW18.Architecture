from app.dao.genre import GenreDAO


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_one(self, gid):
        return self.genre_dao.get_one(gid)

    def get_all(self):
        return self.genre_dao.get_all()

    def create(self, data):
        return self.genre_dao.create(data)

    def update(self, data):
        gid = data.get('id')
        genre = self.get_one(gid)

        genre = self.get_one(gid)
        genre.name = data.get('name')

        self.genre_dao.update(genre)

        return genre

    def delete(self, gid):
        self.genre_dao.delete(gid)