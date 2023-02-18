from app.dao.director import DirectorDAO


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, did):
        return self.director_dao.get_one(did)

    def get_all(self):
        return self.director_dao.get_all()

    def create(self, data):
        return self.director_dao.create(data)

    def update(self, data):
        did = data.get('id')
        director = self.get_one(did)

        director = self.get_one(did)
        director.name = data.get('name')

        self.director_dao.update(director)

        return director

    def delete(self, did):
        self.director_dao.delete(did)