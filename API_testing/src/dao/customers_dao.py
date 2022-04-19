from API_testing.src.utility.dbUtility import DbUtility


class CustomersDAO:

    def __init__(self):
        self.db_helper = DbUtility()

    def get_customer_by_email(self, email):

        sql = f"select * from site.wp_users where user_email='{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
