from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
recipe_Ref = db.collection('recipes')


recipeAPI = Blueprint('recipeAPI', __name__)


# GET
# Pobierz dane o wszystkich przepisach 
@recipeAPI.route('/', methods=['GET'])
def get_all_recipes():
    try:
        all_recipes = [doc.to_dict() for doc in recipe_Ref.stream()]
        return jsonify(all_recipes), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
    
# GET
# Pobierz dane o jednym przepisie
@recipeAPI.route('/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    try:
        doc_ref = recipe_Ref.document(recipe_id)
        doc = doc_ref.get()

        if doc.exists:
            recipe_data = doc.to_dict()
            recipe_data['id'] = recipe_id
            return jsonify(recipe_data), 200
        else:
            return jsonify({"message": "Recipe not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"
    
    
# POST
# Dodanie przepisu gdzie id jest autoincrement
@recipeAPI.route('/', methods=['POST'])
def add_recipe():
    try:
        docs = recipe_Ref.stream()
        existing_ids = set()
        for doc in docs:
            recipe_id = int(doc.id)
            existing_ids.add(recipe_id)

        new_recipe_id = 1
        while new_recipe_id in existing_ids:
            new_recipe_id += 1

        recipe_data = request.json
        recipe_data['id'] = new_recipe_id
        recipe_Ref.document(str(new_recipe_id)).set(recipe_data)

        return jsonify({"success": True, "id": new_recipe_id}), 201

    except Exception as e:
        return f"An Error Occurred: {e}"
    
    
# PUT
# Edytuj przepis o podanym ID
@recipeAPI.route('/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    try:
        doc_ref = recipe_Ref.document(recipe_id)
        doc = doc_ref.get()

        if doc.exists:
            recipe_data = request.json
            doc_ref.update(recipe_data)
            updated_doc = doc_ref.get()
            updated_recipe_data = updated_doc.to_dict()
            updated_recipe_data['id'] = recipe_id
            return jsonify(updated_recipe_data), 200
        else:
            return jsonify({"message": "Recipe not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"
    
# DELETE
# Usuń wszystkie przepisy
@recipeAPI.route('/', methods=['DELETE'])
def delete_all_recipes():
    try:
        docs = recipe_Ref.stream()

        for doc in docs:
            doc.reference.delete()

        return jsonify({'message': 'Wszystkie przepisy zostały usunięte.'}), 200

    except Exception as e:
        return f"An Error Occurred: {e}"


# DELETE
# Usuń przepis o podanym ID
@recipeAPI.route('/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    try:
        doc_ref = recipe_Ref.document(recipe_id)
        doc = doc_ref.get()

        if doc.exists:
            doc.reference.delete()
            return jsonify({'message': 'Przepis został usunięty.'}), 200
        else:
            return jsonify({'message': 'Przepis nie istnieje.'}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"
