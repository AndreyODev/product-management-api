from bson import ObjectId
from database.database import *

def create_produto_repositorio(produto_dict):
    return collection.insert_one(produto_dict)

def pegar_produtos_repositorio():
    return collection.find()

def buscar_produto_repositorio(produto_id):
    return collection.find_one({"_id": ObjectId(produto_id)})

def atualizar_produto_repositorio(produto_id, dados_dict): 
    return collection.update_one(
            {"_id": ObjectId(produto_id)},
            {"$set": dados_dict}
    )
    
def deletar_produto_repositorio(produto_id):
    return collection.delete_one({"_id": ObjectId(produto_id)})