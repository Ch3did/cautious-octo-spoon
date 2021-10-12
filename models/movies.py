from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


class Movies:
    def __init__(self, id, title, year, image, rating):
        self.id = id
        self.title = title
        self.year = year
        self.image_id = image["id"]
        self.image_url = image["url"]
        self.rating = rating

    def create(self):
        with engine.connect() as conn:
            conn.execute(
                text(
                    """
                    insert into movies (title, year, image_id, image_url)
                    values (:title, :year, :image_id, :image_url)
                """
                ),
                title=self.title,
                year=self.year,
                image_id=self.self.image_id,
                image_url=self.image_url,
            )
