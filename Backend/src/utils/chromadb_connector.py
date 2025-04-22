"""
ChromaDB Connector - Funciones CRUD para la base de datos vectorial

No se crea a partir del crud_base.py porque:

En SQLAlchemy (crud_base.py):

Trabaja con modelos de bases de datos relacionales
Usa sesiones SQL para las transacciones
Maneja entidades que tienen relaciones entre sí
Opera sobre registros con estructura fija (tablas)

En ChromaDB (chromadb_connector.py):

Trabaja con embeddings vectoriales para búsqueda semántica
Opera con "colecciones" de vectores en lugar de tablas
Está optimizado para búsqueda por similitud
No tiene un esquema rígido como SQL

En crud_base.py usas: create(), get(), update(), remove()
En chromadb_connector.py usamos: add_document(), search_similar_documents(), update_document(), delete_document()

"""
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
import uuid
from typing import List, Dict, Any, Optional
import logging


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
