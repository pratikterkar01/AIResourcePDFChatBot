from fastapi import APIRouter, HTTPException
from Services.IngectionService import IngetionService

router = APIRouter()

@router.get("/IngectionSerivice/{directoryPath}")
def ingectionDocument(directoryPath: str):
    ingection = IngetionService()
    loadedDoc = ingection.directoryLoad(directoryPath)
    return loadedDoc

@router.get("/hello")
def helloWord():
    return "App is working"



