from flask import Flask, request, jsonify, abort
import mysql.connector
from mysql.connector import errors
import logging

app = Flask(__name__)

def handle_db_error(e):
    if isinstance(e, errors.InterfaceError):
        if "Unknown MySQL server host" in str(e):
            app.logger.error(f"Database connection failed: {e}")
            return jsonify({"error": "Database connection failed", "message": "Unknown MySQL server host"}), 500
        else:
            app.logger.error(f"Database connection failed: {e}")
            return jsonify({"error": "Database connection failed", "message": str(e)}), 500
    elif isinstance(e, errors.DatabaseError):
        app.logger.error(f"Database error: {e}")
        return jsonify({"error": "Database error", "message": str(e)}), 500
    else:
        app.logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/api-dev', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_dev():
    if request.environ['SERVER_PORT'] == '5000':
        try:
            if request.method == 'GET':
                # Existing code for GET
                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                cursor.close()
                conx.close()
                return jsonify(users)

            elif request.method == 'POST':
                # Existing code for POST
                user_data = request.json
                name = user_data.get('name')
                age = user_data.get('age')

                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()
                cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
                conx.commit()
                cursor.close()
                conx.close()
                return jsonify({"message": "User added successfully"}), 201

            elif request.method == 'PUT':
                # New code for PUT
                user_data = request.json
                user_uid = user_data.get('uid')
                name = user_data.get('name')
                age = user_data.get('age')

                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()

                # Update query
                cursor.execute("UPDATE users SET name = %s, age = %s WHERE uid = %s", (name, age, user_uid))
                conx.commit()

                # Check if any row was updated
                if cursor.rowcount == 0:
                    return jsonify({"error": "User not found or no changes made"}), 404

                cursor.close()
                conx.close()
                return jsonify({"message": "User updated successfully"}), 200

            elif request.method == 'DELETE':
                # Existing code for DELETE
                user_data = request.json
                user_uid = user_data.get('uid')

                conx = mysql.connector.connect(user='root', password='db4dev$', host='db-dev', database='users')
                cursor = conx.cursor()

                cursor.execute("DELETE FROM users WHERE uid = %s", (user_uid,))
                conx.commit()

                if cursor.rowcount == 0:
                    return jsonify({"error": "User not found"}), 404

                cursor.close()
                conx.close()
                return jsonify({"message": "User deleted successfully"}), 200

            else:
                return abort(403)  # Forbuidden access

        except Exception as e:
            return handle_db_error(e)

@app.route('/api-test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_test():
    if request.environ['SERVER_PORT'] == '5000':
        try:
            if request.method == 'GET':
                # Existing code for GET
                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()
                cursor.close()
                conx.close()
                return jsonify(users)

            elif request.method == 'POST':
                # Existing code for POST
                user_data = request.json
                name = user_data.get('name')
                age = user_data.get('age')

                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()
                cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
                conx.commit()
                cursor.close()
                conx.close()
                return jsonify({"message": "User added successfully"}), 201

            elif request.method == 'PUT':
                # New code for PUT
                user_data = request.json
                user_uid = user_data.get('uid')
                name = user_data.get('name')
                age = user_data.get('age')

                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()

                # Update query
                cursor.execute("UPDATE users SET name = %s, age = %s WHERE uid = %s", (name, age, user_uid))
                conx.commit()

                if cursor.rowcount == 0:
                    return jsonify({"error": "User not found or no changes made"}), 404

                cursor.close()
                conx.close()
                return jsonify({"message": "User updated successfully"}), 200

            elif request.method == 'DELETE':
                # Existing code for DELETE
                user_data = request.json
                user_uid = user_data.get('uid')

                conx = mysql.connector.connect(user='root', password='db4test$', host='db-test', database='users')
                cursor = conx.cursor()

                cursor.execute("DELETE FROM users WHERE uid = %s", (user_uid,))
                conx.commit()

                if cursor.rowcount == 0:
                    return jsonify({"error": "User not found"}), 404

                cursor.close()
                conx.close()
                return jsonify({"message": "User deleted successfully"}), 200

            else:
                return abort(403)  # Forbuidden access

        except Exception as e:
            return handle_db_error(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)