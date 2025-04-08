# Importaciones comunes para ser reutilizadas
"""
Importaciones comunes para ser reutilizadas:

- `FastAPI`: Framework principal para construir aplicaciones web y APIs.
- `Body`: Utilizado para extraer datos del cuerpo de las solicitudes HTTP.
- `Depends`: Permite la inyección de dependencias en rutas y funciones.
- `HTTPException`: Clase para manejar excepciones HTTP personalizadas.
- `status`: Proporciona códigos de estado HTTP estándar.

- `BaseModel`: Clase base de Pydantic para definir modelos de datos.
- `Field`: Permite agregar metadatos y validaciones a los campos de los modelos.
- `validator`: Decorador para agregar validaciones personalizadas en los modelos.
- `EmailStr`: Tipo de dato para validar direcciones de correo electrónico.

- `List`: Tipo genérico para listas.
- `Optional`: Indica que un campo puede ser opcional (puede ser `None`).
- `Dict`: Tipo genérico para diccionarios.
- `Union`: Permite definir campos que aceptan múltiples tipos de datos.
- `Any`: Tipo genérico que acepta cualquier valor.
"""
from fastapi import FastAPI, Body, Depends, HTTPException, status
from pydantic import BaseModel, Field, validator, EmailStr
from typing import List, Optional, Dict, Union, Any