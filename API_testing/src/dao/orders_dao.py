from API_testing.src.utility.dbUtility import DbUtility
import random


class OrdersDAO:

    def __init__(self):

        self.db_helper = DbUtility()


    def get_order_by_id(self, id, qty=1):

        sql = f"SELECT * FROM site.wp_posts where post_type='shop_order' and ID={id}"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))