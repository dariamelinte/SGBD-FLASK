from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import cx_Oracle

from config.config import Config


class Roles(Resource):
    """
    Route for managing User Roles
    """

    def get(self):
      try:
        # create a connection to the Oracle Database
        with cx_Oracle.connect(user=Config.USERNAME, password=Config.PASSWORD, dsn=Config.DSN) as connection:
          # create a new cursor
          with connection.cursor() as cursor:
            roles = cursor.var()
            cursor.callproc('crud_roles_pkg.get_all', [])
            print(roles, roles.getvalue())

            return {
              "success": True,
              "data": roles.getvalue()
            }

      except cx_Oracle.Error as error:
        print(error)
        return {
          "success": False,
          "error": str(error)
        }