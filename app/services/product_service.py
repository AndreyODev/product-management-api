from bson import ObjectId
from repositories.product_repository import *

def create_produto_service(produto):
    create_produto_repositorio(produto.model_dump())
    return {"Message": "Product created"}

def formatar_id(produto):
    produto["_id"] = str(produto["_id"])
    return produto
    
def pegar_produtos_services():
    produtos = pegar_produtos_repositorio()
    lista = []
    
    for produto in produtos:
        lista.append(formatar_id(produto))
        
    return lista

def buscar_produto_service(produto_id):
    produto = buscar_produto_repositorio(produto_id)

    try:
        if produto:
            produto["_id"] = str(produto["_id"])
            return produto
        else:
            return {"erro": "Produto não encontrado"}
    except:
        return {"erro": "ID inválido"}
    
def atualizar_produto_services(produto_id, dados):
    result = atualizar_produto_repositorio(produto_id, dados.model_dump())
    
    try:
        if result.matched_count == 0:
            return {"erro": "Produto não encontrado"}
        return {"mensagem": "Produto atualizado"}
    except:
        return {"erro": "ID inválido"}
    
def deletar_produto_services(produto_id):
    result = deletar_produto_repositorio(produto_id)
    
    try:
        if result.deleted_count == 0:
            return {"erro": "Produto não encontrado"}
        return {"mensagem": "Produto deletado"}
    except:
        return {"erro": "ID inválido"}
