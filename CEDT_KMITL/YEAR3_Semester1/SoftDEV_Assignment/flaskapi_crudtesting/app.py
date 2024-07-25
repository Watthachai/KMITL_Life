from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"uid": 121, "name": "Alice", "age": 18},
    {"uid": 122, "name": "Bob", "age": 17},
    {"uid": 123, "name": "Cindy", "age": 25},
    {"uid": 124, "name": "Dan", "age": 21}
]

@app.route('/user', methods=['GET'])
def user():
    return jsonify(users), 200

@app.route('/user/new', methods=['POST'])
def add_user():
    user = request.get_json()
    new_id = max(u['uid'] for u in users) + 1
    user['uid'] = new_id
    users.append(user)
    return jsonify({"uid": new_id}), 201

@app.route('/user/<int:uid>', methods=['GET'])
def get_user(uid):
    for user in users:
        if user['uid'] == uid:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/user/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    for user in users:
        if user['uid'] == uid:
            users.remove(user)
            return jsonify({"uid": uid, "message": "Deleted Successfully!"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)