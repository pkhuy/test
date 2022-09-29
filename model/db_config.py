from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """SQLAlchemy model connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///database.db"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :param - None
        :return - engine connection to model
        """

        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member

    def execute(self, exe_data):
        with self:
            try:
                return self.get_engine().execute(exe_data)

            except Exception as ex:
                self.session.rollback()
                print(ex)
                raise
            finally:
                self.session.close()

