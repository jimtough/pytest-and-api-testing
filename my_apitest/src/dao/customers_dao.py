from my_apitest.src.utilities.database_utils import DatabaseUtils


class CustomersDAO(object):

    def __init__(self):
        self.database_utils = DatabaseUtils()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM my_wordpress.wp_users WHERE user_email = '{email}'"
        rs_sql = self.database_utils.execute_select(sql)
        return rs_sql
