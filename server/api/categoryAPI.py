from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
category_Ref = db.collection('categories')


categoryAPI = Blueprint('categoryAPI', __name__)


# GET
# Pobierz dane o wszystkich kategoriach
@categoryAPI.route('/', methods=['GET'])
def get_all_categories():
    try:
        all_categories = [doc.to_dict() for doc in category_Ref.stream()]
        return jsonify(all_categories), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
    
# GET
# Pobierz dane o jednej kategorii
@categoryAPI.route('/<category_id>', methods=['GET'])
def get_category(category_id):
    try:
        doc_ref = category_Ref.document(category_id)
        doc = doc_ref.get()

        if doc.exists:
            category_data = doc.to_dict()
            category_data['id'] = category_id
            return jsonify(category_data), 200
        else:
            return jsonify({"message": "Category not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"