from flask_app.models import base_model
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Config(base_model.Base):
    table_name = "config"
    attributes = ['max_daily_orders', 'announcement']
    required_attributes = []
    def __init__(self, data):
        super().__init__(data)

        # TODO: create attributes
        self.max_daily_orders = data['max_daily_orders']
        self.announcement = data['announcement']

    @classmethod
    def get_one(cls):
        query = "SELECT * FROM config LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        return cls(results[0])