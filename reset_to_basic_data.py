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
            'nazwa': 'Spaghetti Bolognese',
            'skladniki': ['makaron', 'mielone mięso', 'cebula', 'czosnek', 'sos pomidorowy'],
            'opis_przygotowania': '1. Ugotuj makaron. 2. Usmaż mięso mielone i cebulę. 3. Dodaj czosnek i sos pomidorowy. 4. Gotuj na małym ogniu i podawaj na makaronie.',
            'czas_przygotowania': 30,
            'ilosc_porcji': 4,
            'kategoria': 'dania główne',
            'alergeny': ''
        },
        {
            'nazwa': 'Ciasteczka z kawałkami czekolady',
            'skladniki': ['mąka', 'masło', 'cukier', 'kawałki czekolady'],
            'opis_przygotowania': '1. Rozgrzej piekarnik. 2. Utłucz masło z cukrem. 3. Dodaj mąkę i kawałki czekolady. 4. Piecz ciasteczka.',
            'czas_przygotowania': 25,
            'ilosc_porcji': 20,
            'kategoria': 'desery',
            'alergeny': ''
        },
        {
            'nazwa': 'Kurczak Parmezan',
            'skladniki': ['pierś z kurczaka', 'bułka tarta', 'ser Parmezan', 'sos marinara', 'ser mozzarella'],
            'opis_przygotowania': '1. Rozgrzej piekarnik. 2. Panieruj kurczaka w bułce tartej i serze Parmezan. 3. Usmaż kurczaka na patelni. 4. Posmaruj sosem marinara i dodaj ser mozzarella. 5. Piecz, aż ser się roztopi i będzie puszysty.',
            'czas_przygotowania': 45,
            'ilosc_porcji': 6,
            'kategoria': 'dania główne',
            'alergeny': ''
        },
        {
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
        recipes_collection.add(recipe)

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
        user_id = str(user.pop("id"))  # Przekonwertuj id na string
        users_collection.document(user_id).set(user)  # Użyj id jako nazwy dokumentu

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
            'nazwa': 'dania główne'
        },
        {
            'nazwa': 'desery'
        },
        {
            'nazwa': 'sałatki'
        },
        {
            'nazwa': 'zupy'
        },
        {
            'nazwa': 'napoje'
        }
    ]

    for category in categories_data:
        categories_collection.add(category)

    print('Utworzono kolekcję Kategorie.')


def create_allergens():
    allergens_collection = db.collection('allergens')
    allergens_data = [
        {
            'nazwa': 'gluten'
        },
        {
            'nazwa': 'mleko'
        },
        {
            'nazwa': 'jajka'
        },
        {
            'nazwa': 'orzechy'
        },
        {
            'nazwa': 'soja'
        }
    ]

    for allergen in allergens_data:
        allergens_collection.add(allergen)

    print('Utworzono kolekcję Alergeny.')


def reset_to_defaults():
    delete_all_recipes()
    add_recipes()
    delete_all_users()
    add_users()
    create_categories()
    create_allergens()

    print("\nUtworzenie domyślnej struktury i uzupełnienie podstawowymi danymi zakończone\n")


reset_to_defaults()
