from API_testing.src.utility.dbUtility import DbUtility
import random


class ProductsDAO:

    def __init__(self):

        self.db_helper = DbUtility()


    def get_random_product_id_from_bd(self, qty=1):

        sql = f"SELECT id FROM site.wp_posts where id>10 order by rand() limit 5000"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))