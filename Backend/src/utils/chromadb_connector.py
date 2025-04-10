"""
ChromaDB Connector - Funciones CRUD para la base de datos vectorial
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
