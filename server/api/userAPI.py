from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('users')


userAPI = Blueprint('userAPI', __name__)
    

# GET
# Pobierz dane o wszystkich użytkownikach 
@userAPI.route('/', methods=['GET'])
def get_all_users():
    try:
        all_users = [doc.to_dict() for doc in user_Ref.stream()]
        return jsonify(all_users), 200
    except Exception as e:
        return f"An Error Occured: {e}"


# GET
# Pobierz dane o jednym użytkowniku
@userAPI.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        doc_ref = user_Ref.document(user_id)
        doc = doc_ref.get()

        if doc.exists:
            user_data = doc.to_dict()
            user_data['id'] = user_id
            return jsonify(user_data), 200
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"


# POST
# Dodanie użytkownika gdzie id jest autoincrement
@userAPI.route('/', methods=['POST'])
def add_user():
    try:
        docs = user_Ref.stream()
        existing_ids = set()
        for doc in docs:
            user_id = int(doc.id)
            existing_ids.add(user_id)

        new_user_id = 1
        while new_user_id in existing_ids:
            new_user_id += 1

        user_data = request.json
        user_data['id'] = new_user_id
        user_Ref.document(str(new_user_id)).set(user_data)

        return jsonify({"success": True, "id": new_user_id}), 201

    except Exception as e:
        return f"An Error Occurred: {e}"



# PUT
# Edytuj użytkownika o podanym ID
@userAPI.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        doc_ref = user_Ref.document(user_id)
        doc = doc_ref.get()

        if doc.exists:
            user_data = request.json
            doc_ref.update(user_data)
            updated_doc = doc_ref.get()
            updated_user_data = updated_doc.to_dict()
            updated_user_data['id'] = user_id
            return jsonify(updated_user_data), 200
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"


# DELETE
# Usuń wszystkich użytkowników
@userAPI.route('/', methods=['DELETE'])
def delete_all_users():
    try:
        docs = user_Ref.stream()

        for doc in docs:
            doc.reference.delete()

        return jsonify({'message': 'Wszyscy użytkownicy zostali usunięci.'}), 200

    except Exception as e:
        return f"An Error Occurred: {e}"


# DELETE
# Usuń użytkownika o podanym ID
@userAPI.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        doc_ref = user_Ref.document(user_id)
        doc = doc_ref.get()

        if doc.exists:
            doc.reference.delete()
            return jsonify({'message': 'Użytkownik został usunięty.'}), 200
        else:
            return jsonify({'message': 'Użytkownik nie istnieje.'}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"
