from flask import Flask, request, jsonify, abort
import mysql.connector
from mysql.connector import errors
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return "Hi World"

@app.route('/api-dev', methods=['GET', 'POST'])
def users_dev():
    if request.environ['SERVER_PORT'] == '5000':
        if request.method == 'GET':
            try:
                # Connect to MySQL database
                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                cursor.close()
                conx.close()
                return jsonify(users)
            except errors.InterfaceError as e:
                app.logger.error(f"Database connection failed: {e}")
                return jsonify({"error": "Database connection failed", "message": str(e)}), 500
            except errors.DatabaseError as e:
                app.logger.error(f"Database error: {e}")
                return jsonify({"error": "Database error", "message": str(e)}), 500
            except Exception as e:
                app.logger.error(f"An unexpected error occurred: {e}")
                return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
        elif request.method == 'POST':
            try:
                # Get data from request
                user_data = request.json
                name = user_data.get('name')
                age = user_data.get('age')

                # Connect to MySQL database
                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()
                cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
                conx.commit()
                cursor.close()
                conx.close()
                return jsonify({"message": "User added successfully"}), 201
            except errors.InterfaceError as e:
                app.logger.error(f"Database connection failed: {e}")
                return jsonify({"error": "Database connection failed", "message": str(e)}), 500
            except errors.DatabaseError as e:
                app.logger.error(f"Database error: {e}")
                return jsonify({"error": "Database error", "message": str(e)}), 500
            except Exception as e:
                app.logger.error(f"An unexpected error occurred: {e}")
                return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
    else:
        return abort(403)  # Forbidden access

@app.route('/api-test', methods=['GET', 'POST'])
def users_test():
    if request.environ['SERVER_PORT'] == '5000':
        if request.method == 'GET':
            try:
                # Connect to MySQL database
                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                cursor.close()
                conx.close()
                return jsonify(users)
            except errors.InterfaceError as e:
                app.logger.error(f"Database connection failed: {e}")
                return jsonify({"error": "Database connection failed", "message": str(e)}), 500
            except errors.DatabaseError as e:
                app.logger.error(f"Database error: {e}")
                return jsonify({"error": "Database error", "message": str(e)}), 500
            except Exception as e:
                app.logger.error(f"An unexpected error occurred: {e}")
                return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
        elif request.method == 'POST':
            try:
                # Get data from request
                user_data = request.json
                name = user_data.get('name')
                age = user_data.get('age')

                # Connect to MySQL database
                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()
                cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
                conx.commit()
                cursor.close()
                conx.close()
                return jsonify({"message": "User added successfully"}), 201
            except errors.InterfaceError as e:
                app.logger.error(f"Database connection failed: {e}")
                return jsonify({"error": "Database connection failed", "message": str(e)}), 500
            except errors.DatabaseError as e:
                app.logger.error(f"Database error: {e}")
                return jsonify({"error": "Database error", "message": str(e)}), 500
            except Exception as e:
                app.logger.error(f"An unexpected error occurred: {e}")
                return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500
    else:
        return abort(403)  # Forbidden access

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
