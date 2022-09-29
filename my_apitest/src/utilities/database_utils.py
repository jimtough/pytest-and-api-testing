import pymysql
import logging as logger
from my_apitest.src.utilities.credentials_utils import CredentialsUtils


class DatabaseUtils(object):

    def __init__(self):
        credentials_utils = CredentialsUtils()
        self.credentials = credentials_utils.get_database_credentials()
        self.database_host = "localhost"
        self.database_port = "8889"

    def create_connection(self):
        connection = pymysql.connect(
            host=self.database_host,
            user=self.credentials['db_username'],
            password=self.credentials['db_password'],
            port=int(self.database_port)
        )
        return connection

    def execute_select(self, sql):
        connection = self.create_connection()
        try:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            logger.debug("executing SQL SELECT | [%s]", sql)
            cursor.execute(sql)
            rs_dict = cursor.fetchall()
            cursor.close()
            return rs_dict
        except Exception as e:
            raise Exception(f"Failed to execute SQL | err msg: [{str(e)}] | SQL: [{sql}]")
        finally:
            connection.close()

    def execute_update(self, sql):
        pass
