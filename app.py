# importando a biblioteca do pymongo
from pymongo import MongoClient

# definindo a conexão com o BD Mongodb
client = MongoClient("mongodb://localhost:27017")

# criando objeto que definirá o DB
database = client["veiculos"]

# criando coleção no DB criado
collection = database["carros"]

# inserindo dados no BD
#new_car = {"Marca": "Fiat", "Modelo": "Toro", "Ano": 1995}
#collection.insert_one(new_car)

# Buscar com Find na tabela e mostrar na tela
print(collection.find_one())

# Atualizar com Update na collection
#collection.update_one({"Marca": "Fiat"}, {"$set": {"ano": 1992}})

new_car2 = {"Marca": "Fiat", "Modelo": "Toro", "Ano": 2022}
collection.insert_one(new_car2)

collection.delete_many({"Modelo": "Toro"})

print(collection.find_one())