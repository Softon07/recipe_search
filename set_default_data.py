import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('server/api/key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def add_recipes():
    recipes_collection = db.collection('recipes')
    recipe_data = [
        {
            'id': 1,
            'nazwa': 'Spaghetti Bolognese',
            'skladniki': ['makaron', 'mielone mięso', 'cebula', 'czosnek', 'sos pomidorowy'],
            'opis_przygotowania': '1. Ugotuj makaron. 2. Usmaż mięso mielone i cebulę. 3. Dodaj czosnek i sos pomidorowy. 4. Gotuj na małym ogniu i podawaj na makaronie.',
            'czas_przygotowania': 30,
            'ilosc_porcji': 4,
            'kategoria': 'dania główne',
            'alergeny': ''
        },
        {
            'id': 2,
            'nazwa': 'Ciasteczka z kawałkami czekolady',
            'skladniki': ['mąka', 'masło', 'cukier', 'kawałki czekolady'],
            'opis_przygotowania': '1. Rozgrzej piekarnik. 2. Utłucz masło z cukrem. 3. Dodaj mąkę i kawałki czekolady. 4. Piecz ciasteczka.',
            'czas_przygotowania': 25,
            'ilosc_porcji': 20,
            'kategoria': 'desery',
            'alergeny': ''
        },
        {
            'id': 3,
            'nazwa': 'Kurczak Parmezan',
            'skladniki': ['pierś z kurczaka', 'bułka tarta', 'ser Parmezan', 'sos marinara', 'ser mozzarella'],
            'opis_przygotowania': '1. Rozgrzej piekarnik. 2. Panieruj kurczaka w bułce tartej i serze Parmezan. 3. Usmaż kurczaka na patelni. 4. Posmaruj sosem marinara i dodaj ser mozzarella. 5. Piecz, aż ser się roztopi i będzie puszysty.',
            'czas_przygotowania': 45,
            'ilosc_porcji': 6,
            'kategoria': 'dania główne',
            'alergeny': ''
        },
        {
            'id': 4,
            'nazwa': 'Sałatka Cezar',
            'skladniki': ['sałata rzymska', 'grzanki', 'ser Parmezan', 'sos Cezar'],
            'opis_przygotowania': '1. Umyj i pokrój sałatę. 2. Dodaj grzanki, ser Parmezan i sos Cezar. 3. Podawaj schłodzone.',
            'czas_przygotowania': 15,
            'ilosc_porcji': 2,
            'kategoria': 'sałatki',
            'alergeny': ''
        }
    ]
    
    for recipe in recipe_data:
        recipe_id = str(recipe.pop("id"))
        recipes_collection.document(recipe_id).set(recipe) 

    print('Dodano przepisy.')


def delete_all_recipes():
    recipes_collection = db.collection('recipes')
    recipes = recipes_collection.stream()

    for recipe in recipes:
        recipe.reference.delete()

    print('Usunięto wszystkie przepisy.')


def add_users():
    users_collection = db.collection('users')
    user_data = [
        {
            "id": 1,
            'imie': 'Marcel',
            'nazwisko': 'Nędza',
            'email': 'marcelnedza2000@gmail.com',
        },
        {
            "id": 2,
            'imie': 'Jan',
            'nazwisko': 'Kowalski',
            'email': 'jan.kowalski@gmail.com',
        }
    ]

    for user in user_data:
        user_id = str(user.pop("id"))
        users_collection.document(user_id).set(user) 

    print('Dodano użytkowników.')


def delete_all_users():
    users_collection = db.collection('users')
    users = users_collection.stream()

    for user in users:
        user.reference.delete()

    print('Usunięto wszystkich użytkowników.')
    
    
def create_categories():
    categories_collection = db.collection('categories')
    categories_data = [
        {
            'id': 1,
            'nazwa': 'dania główne'
        },
        {
            'id': 2,
            'nazwa': 'desery'
        },
        {
            'id': 3,
            'nazwa': 'sałatki'
        },
        {
            'id': 4,
            'nazwa': 'zupy'
        },
        {
            'id': 5,
            'nazwa': 'napoje'
        }
    ]

    for category in categories_data:
        category_id = str(category.pop("id"))
        categories_collection.document(category_id).set(category) 

    print('Utworzono kolekcję Kategorie.')
    
def delete_all_categories():
    categories_collection = db.collection('categories')
    categories = categories_collection.stream()

    for category in categories:
        category.reference.delete()

    print('Usunięto wszystkie kategorie.')


def create_allergens():
    allergens_collection = db.collection('allergens')
    allergens_data = [
        {
            'id': 1,
            'nazwa': 'gluten'
        },
        {
            'id': 2,
            'nazwa': 'mleko'
        },
        {
            'id': 3,
            'nazwa': 'jajka'
        },
        {
            'id': 4,
            'nazwa': 'orzechy'
        },
        {
            'id': 5,
            'nazwa': 'soja'
        }
    ]

    for allergen in allergens_data:
        allergen_id = str(allergen.pop("id"))
        allergens_collection.document(allergen_id).set(allergen) 

    print('Utworzono kolekcję Alergeny.')
    
def delete_all_allergens():
    allergens_collection = db.collection('allergens')
    allergens = allergens_collection.stream()

    for allergen in allergens:
        allergen.reference.delete()

    print('Usunięto wszystkie allergeny.')


def reset_to_defaults():
    delete_all_recipes()
    add_recipes()
    delete_all_users()
    add_users()
    delete_all_categories()
    create_categories()
    delete_all_allergens()
    create_allergens()

    print("\nUtworzenie domyślnej struktury i uzupełnienie podstawowymi danymi zakończone\n")


reset_to_defaults()
