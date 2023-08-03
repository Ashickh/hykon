import re
import os
from collections import defaultdict
from pprint import pprint

import mysql.connector
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Restore a MySQL database dump directly in a given order'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='MySQL dump file path')
        parser.add_argument('--order', type=str, help='Comma separated list of tables in the order to restore')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        # table_order = kwargs.get('order', None)
        db_config = settings.DATABASES['default']
        connection = mysql.connector.connect(
            user=db_config['USER'],
            password=db_config['PASSWORD'],
            host=db_config['HOST'],
            port=db_config['PORT'],
            database=db_config['NAME']
        )
        ORDER_OF_EXEC = """states
                            districts
                            city
                            city_pincodes
                            users
                            address
                            categories
                            groups
                            media_types
                            media_library
                            media_settings
                            brands
                            products
                            group_products
                            product_cateory_attributes
                            product_cateory_attribute_values
                            product_attributes
                            product_cateory_attribute_groups
                            product_images_tb
                            product_variants
                            product_inventory_by_vendor
                            product_price_history
                            product_reviews
                            product_stock_history
                            product_variant_images
                            product_views
                            waranty
                            vendors
                            pages
                            blocks
                            extended_warranties
                            sliders
                            slider_photos
                            search
                            search_history
                            settings
                            specifications
                            wishlist
                            offers
                            offer_categories
                            offer_combo_free_products
                            offer_combo_products
                            offer_groups
                            offer_price_products
                            coupons
                            orders
                            order_details
                            order_status_labels_master
                            order_tracking
                            cart
                            cancel_order_reasons
                            banners
                            banner_photos
                            bans
                            brach_data
                            branch_landmarks
                            branches
                            frontend_pages
                            home_page_settings
                            menus
                            menu_items
                            newsletter_subscriptions
                            password_resets
                            activities
                            admin_pages"""
        cursor = connection.cursor()
        cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
        cursor.execute('ALTER TABLE users MODIFY is_superuser BOOLEAN DEFAULT false;')
        cursor.execute('ALTER TABLE users MODIFY is_staff BOOLEAN DEFAULT true;')
        cursor.execute('ALTER TABLE users MODIFY is_active BOOLEAN DEFAULT true;')
        cursor.execute('ALTER TABLE users MODIFY date_joined datetime(6) DEFAULT NULL;')
        cursor.execute('ALTER TABLE users MODIFY email varchar(254) DEFAULT NULL;')
        cursor.execute('ALTER TABLE users MODIFY first_name varchar(150) DEFAULT NULL;')
        cursor.execute('ALTER TABLE users MODIFY last_name varchar(150) DEFAULT NULL;')
        cursor.execute('ALTER TABLE users MODIFY username varchar(150) DEFAULT NULL;')
        sql_set = None
        with open(filename, 'r') as f:
            sql_set = f.readlines()
        sql_map = defaultdict(list)
        prompt = True
        for table in ORDER_OF_EXEC.split():
            for sql in sql_set:
                if sql.startswith(f'INSERT INTO `{table}`'):
                    sql_map[table.strip()].append(sql)
        self.stdout.write(self.style.WARNING('#############################################'))
        tables = ORDER_OF_EXEC.split()
        for table in tables:
            print('Processing : ', table)
            table = table.strip()
            cursor.execute(f'LOCK TABLES `{table}` WRITE;')
            counter = {'processed': 0, 'skipped': 0, 'crashed': 0}
            sql_data = None
            try:
                self.stdout.write(self.style.SUCCESS(f'Inserting data {table}.'))
                for sql in sql_map[table]:
                    if table in sql:
                        cursor.execute(sql)
                        counter['processed'] += 1
                        # self.stdout.write(self.style.SUCCESS('.'), ending='')
                    else:
                        counter['skipped'] += 1
            except Exception as e:
                counter['crashed'] += 1
                self.stdout.write(self.style.WARNING(e))
                print(sql_data)
                break
            else:
                self.stdout.write(self.style.SUCCESS(f'Table -{table}-  restore complete.'))
            finally:
                print(counter)
                cursor.execute(f'UNLOCK TABLES;')
        cursor.execute(
            "SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_SCHEMA = 'yourdatabase' AND REFERENCED_TABLE_NAME IS NOT NULL;")

        foreign_keys = cursor.fetchall()

        # Loop through each foreign key constraint
        for foreign_key in foreign_keys:
            table_name = foreign_key[0]
            column_name = foreign_key[1]
            constraint_name = foreign_key[2]
            referenced_table_name = foreign_key[3]
            referenced_column_name = foreign_key[4]

            # Check for foreign key constraints with invalid IDs
            cursor.execute(
                f"SELECT {column_name} FROM {table_name} WHERE {column_name} NOT IN (SELECT {referenced_column_name} FROM {referenced_table_name});")

            invalid_fks = cursor.fetchall()

            # Null the foreign key relation for each invalid ID
            for invalid_fk in invalid_fks:
                cursor.execute(f"UPDATE {table_name} SET {column_name} = NULL WHERE {column_name} = {invalid_fk[0]};")
        cursor.execute('SET FOREIGN_KEY_CHECKS=1;')
