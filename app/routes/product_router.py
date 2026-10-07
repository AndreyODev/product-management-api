from fastapi import APIRouter
from schemas.product_schema import Product
from services.product_service import *

router = APIRouter()

# Criar produto
@router.post("/produto")
def create_produto(produto: Product):
    return create_produto_service(produto)

# Rota GET para listar todos os produtos
@router.get("/produto")
def pegar_produtos():
    return pegar_produtos_services()

# Buscar produto por ID
@router.get("/produto/{produto_id}")
def buscar_produto(produto_id: str):
    return buscar_produto_service(produto_id)

# Atualizar produto
@router.put("/produto/{produto_id}")
def atualizar_produto(produto_id, dados: Product):
    return atualizar_produto_services(produto_id, dados)

# Deletar produto
@router.delete("/produto/{produto_id}")
def deletar_produto(produto_id: str):
    return deletar_produto_services(produto_id)