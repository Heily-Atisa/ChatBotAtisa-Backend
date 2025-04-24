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
    client = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromaDBConnector, cls).__new__(cls)
            # Inicialización lazy - la conexión se creará la primera vez que se use
            cls._instance.client = None
        return cls._instance
    
    def _get_client(self):
        """Inicializa el cliente si aún no existe"""
        if self.client is None:
            # Usa variables de entorno o valores por defecto para la configuración
            host = "localhost"
            port = 8000
            
            print(f"Conectando a ChromaDB en {host}:{port}")
            
            # Intenta conectarse a ChromaDB
            self.client = chromadb.HttpClient(
                host=host,
                port=port
            )
        return self.client
    
    def test_connection(self) -> bool:
        """Prueba la conexión a ChromaDB"""
        try:
            # Intenta una operación simple para verificar la conexión
            client = self._get_client()
            # Listar colecciones es una operación ligera para probar
            client.list_collections()
            return True
        except Exception as e:
            print(f"Error al conectar con ChromaDB: {str(e)}")
            return False