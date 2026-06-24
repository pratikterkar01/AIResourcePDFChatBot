from fastapi import APIRouter, HTTPException
from Services.IngectionService import IngetionService

router = APIRouter()

@router.get("/IngectionPipelineInitiate/{directoryPath}")
def ingectionDocument(directoryPath: str):
    ingection = IngetionService()
    loadedDoc = ingection.vectorization_pipline(directoryPath)
    return loadedDoc

@router.get("/hello")
def helloWord():
    return "App is working"



