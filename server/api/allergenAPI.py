from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
allergen_Ref = db.collection('allergens')


allergenAPI = Blueprint('allergenAPI', __name__)


# GET
# Pobierz dane o wszystkich alergenach
@allergenAPI.route('/', methods=['GET'])
def get_all_allergens():
    try:
        all_allergens = [doc.to_dict() for doc in allergen_Ref.stream()]
        return jsonify(all_allergens), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
    
# GET
# Pobierz dane o jednym allergenie
@allergenAPI.route('/<allergen_id>', methods=['GET'])
def get_allergen(allergen_id):
    try:
        doc_ref = allergen_Ref.document(allergen_id)
        doc = doc_ref.get()

        if doc.exists:
            allergen_data = doc.to_dict()
            allergen_data['id'] = allergen_id
            return jsonify(allergen_data), 200
        else:
            return jsonify({"message": "Allergen not found"}), 404

    except Exception as e:
        return f"An Error Occurred: {e}"