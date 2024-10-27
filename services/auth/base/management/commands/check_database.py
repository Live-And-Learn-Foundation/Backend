import os

import MySQLdb
from django.core.management.base import BaseCommand, CommandError
from django.db import connections


class Command(BaseCommand):
    help = "Check if the databases exist, and create them if not."

    def handle(self, *args, **options):
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT', 3306)

        try:
            conn = connections['default']
            conn.ensure_connection()
            self.stdout.write(self.style.SUCCESS(
                f"Database '{db_name}' exists."))
        except Exception:
            self.stdout.write(self.style.WARNING(f"Checking databases..."))

            try:
                connection = MySQLdb.connect(
                    host=db_host,
                    user=db_user,
                    passwd=db_password,
                    port=int(db_port)
                )
                connection.autocommit(True)
                cursor = connection.cursor()

                for db_name in [db_name]:
                    cursor.execute(
                        f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
                    self.stdout.write(self.style.SUCCESS(
                        f"Database '{db_name}' created successfully."))

                cursor.close()
            except MySQLdb.Error as err:
                raise CommandError(f"Error creating database: {err}")
            finally:
                if 'connection' in locals():
                    connection.close()
