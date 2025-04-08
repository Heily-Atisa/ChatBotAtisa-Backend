# Importar FastAPI desde fastapi directamente
from fastapi import FastAPI

# Importar modelos específicos según los necesites
from src.models.schemas.user import UserCreate, UserResponse
from src.models.schemas.document import DocumentBase, DocumentResponse
from src.models.schemas.chat import ChatMessage

# Crear la aplicación
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Ejecutar la app con uvicorn,se mantiene porque asi podemos iniciarla de ambas formas sin afectar el flujo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=2690, reload=True)