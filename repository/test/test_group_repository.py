from model.model import User as UserModel
from model.db_config import DBConnectionHandler
from model.model import Group as GroupModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text
from entities.group import Group
class GroupRepository:
    '''def execute(self):
        if self.repository.find_by(self.email):
            raise 'Email already exists'
        user = self.factory_group()
        return self.repository.create(user)

    def factory_group(self) -> Group:
        instance = Group(self.groupname)
        return instance'''

    @classmethod
    def insert(cls, req: dict) -> Group:
        with DBConnectionHandler() as db_connection:
            try:
                new_group = GroupModel(
                    name=req["name"])
                db_connection.session.add(new_group)
                db_connection.session.commit()

                return Group(
                    id=new_group.id, name=new_group.name
                ).get_as_json()

            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_all(cls) -> List[Group]:
        with DBConnectionHandler() as db_connection:
            try:
                datas = (
                    db_connection.session.query(GroupModel).all()
                )
                json_datas = []
                for data in datas:
                    json_datas.append(
                        Group(data.id, data.name).get_as_json())

                return json_datas

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_by_id(cls, id: int) -> Group:

        with DBConnectionHandler() as db_connection:
            try:
                json_data = None

                if id:
                    # Select player by id
                    with DBConnectionHandler() as db_connection:
                        data = db_connection.session.query(
                            GroupModel).filter_by(id=id).one()
                        json_data = Group(
                            data.id, data.name).get_as_json()

                return json_data

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def select_by_name(cls, name) -> Group:

        with DBConnectionHandler() as db_connection:
            try:
                json_data = None

                if id:
                    # Select player by id
                    with DBConnectionHandler() as db_connection:
                        data = db_connection.session.query(
                            GroupModel).filter_by(name=name).one()
                        json_data = Group(
                            data.id, data.name).get_as_json()

                return json_data

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()
