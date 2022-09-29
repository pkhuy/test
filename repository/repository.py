from entities.user import User
from model.db_config import DBConnectionHandler
from model.model import User as UserModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound

class UserRepository:
    @classmethod
    def insert_user(cls, email: str, password: str) -> UserModel:
        """
        Insert data in user entity
        :param  - email: user email
                - password: user password
        :return - tuple with new user inserted informations
        """

        # Creating a Return Tuple With Informations

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(name="huy", email=email, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return User(
                    id=new_user.id, email=new_user.email, password=new_user.password
                )

            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

        return None
    @classmethod
    def select_all_user(cls) -> List[UserModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(UserModel).all()
                )

                return data

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_user(cls, email: str, password: str = None) -> List[UserModel]:
        
        with DBConnectionHandler() as db_connection:
            try:
                query_data = None

                if email and password:
                    # Select user by id
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(UserModel)
                            .filter_by(email=email, password=password)
                            .one()
                        )
                        query_data = [data]

                return query_data

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def loaded_user(cls, id: int) -> UserModel:
        """
        Select data in user entity by id and/or name
        :param  - id: user ID
        :return - User who queried
        """
        with DBConnectionHandler() as db_connection:
            try:
                data = None

                if id:
                    # Select user by id
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(UserModel)
                            .filter_by(id=id)
                            .one()
                        )

                return data

            except NoResultFound:
                return data
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

        return None

    #Not done yet
    @classmethod
    def get_permission(cls, entity: str) -> UserModel:
        """
        Select data in user entity by id and/or name
        :param  - id: Id of the registry
                - name: User name in model
        :return - List with UsersModel selected
        """
        with DBConnectionHandler() as db_connection:
            try:
                data = None

                if id:
                    # Select user by id
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(UserModel)
                            .filter_by(id=id)
                            .one()
                        )

                return data

            except NoResultFound:
                return data
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()