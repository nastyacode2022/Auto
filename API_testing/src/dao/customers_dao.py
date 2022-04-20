from API_testing.src.utility.dbUtility import DbUtility
import random


class CustomersDAO:

    def __init__(self):
        self.db_helper = DbUtility()


    def get_customer_by_email(self, email):

        sql = f"select * from site.wp_users where user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql


    def get_random_customer_from_db(self, qty=1):

        sql = "select * from site.wp_users order by rand() limit 1;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))
