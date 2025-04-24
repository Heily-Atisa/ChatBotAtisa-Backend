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


(lazy initialization)

Técnica donde los objetos se crean solo cuando son realmente necesarios, no antes. Esto ahorra recursos al retrasar la creación hasta el momento de uso.

"""
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os
import uuid
from typing import List, Dict, Any, Optional
import logging


def load_env_file():
    """Lee el archivo .env manualmente"""
    env_vars = {}
    try:
        with open('.env', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
        return env_vars
    except FileNotFoundError:
        return {}

class ChromaDBConnector:
    _instance = None
    _client = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromaDBConnector, cls).__new__(cls)
            # Inicialización lazy - el cliente se creará la primera vez que se use
            cls._instance._client = None
        return cls._instance
    
    def get_client(self):
        """Inicializa el cliente persistente si aún no existe"""
        if self._client is None:
            # Crea el directorio si no existe
            os.makedirs("./chromadb_data", exist_ok=True)
            
            print(f"Inicializando cliente persistente de ChromaDB en ./chromadb_data")
            
            # Inicializa el cliente persistente - esto maneja todo internamente
            self._client = chromadb.PersistentClient(path="./chromadb_data")
            
        return self._client
    
    def test_connection(self) -> bool:
        """Prueba la conexión/funcionalidad de ChromaDB"""
        try:
            # Intenta una operación simple para verificar la funcionalidad
            client = self.get_client()
            # Listar colecciones es una operación ligera para probar
            client.list_collections()
            return True
        except Exception as e:
            print(f"Error con ChromaDB: {str(e)}")
            return False
            
    def create_collection(self, collection_name, metadata=None):
        """Crea una colección si no existe"""
        client = self.get_client()
        try:
            # Intenta obtener la colección primero
            return client.get_collection(name=collection_name, embedding_function=None)
        except:
            # Si no existe, créala
            return client.create_collection(
                name=collection_name,
                metadata=metadata or {},
                embedding_function=None
            )