from app.dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_all(self, filters):
        return self.movie_dao.get_all(filters)

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.get_one(mid)

        movie = self.get_one(mid)
        movie.name = data.get('name')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.movie_dao.update(movie)

        return movie

    def delete(self, mid):
        self.movie_dao.delete(mid)