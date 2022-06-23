import os


class Environment:
    DEV = 'dev'

    URLS = {
        DEV: 'https://developers.themoviedb.org/3/movies/get-top-rated-movies',
        PROD: 'https://developers.themoviedb.org/3/movies/get-top-rated-movies'
    }

    def __init__(self):
        self.name = self._get_environment_variable()

    @classmethod
    def _get_environment_variable(cls) -> str:
        try:
            return os.environ['ENVIRONMENT']
        except KeyError:
            return cls.DEV

    def base_url(self) -> str:
        return self.URLS[self.name]


ENV = Environment()
