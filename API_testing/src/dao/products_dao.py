from API_testing.src.utility.dbUtility import DbUtility
import random


class ProductsDAO:

    def __init__(self):

        self.db_helper = DbUtility()


    def get_random_product_id_from_bd(self, qty=1):

        sql = f"SELECT id FROM site.wp_posts where post_type='product' order by rand() limit 5000"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))


    def get_product_by_id(self, id):

        sql = f"SELECT {id} FROM site.wp_posts limit 5000"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql


    def count_products_by_data(self, data):

        sql = f"SELECT count(*) FROM site.wp_posts where post_date>'{data}' and post_type='product'"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql