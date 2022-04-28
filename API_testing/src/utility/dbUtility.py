import pymysql
from pymysql import cursors
from API_testing.src.utility.credentialUtility import CredentialsUtility
from API_testing.src.config.hosts_config import DB_HOST
import os

class DbUtility:

    def __init__(self):

        self.creds = CredentialsUtility().get_db_credentials()
        self.host = DB_HOST['machine1']['test']['host']
        self.port = DB_HOST['machine1']['test']['port']

    def create_connection(self):

        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=self.port)
        return connection

    def execute_select(self, sql):

        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql} \n Error: {str(e)}")
        finally:
            conn.close()
        return rs_dict

    def execute_sql(self, sql):
        pass
