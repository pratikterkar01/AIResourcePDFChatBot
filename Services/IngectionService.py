from Utils import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader,PyPDFDirectoryLoader,DirectoryLoader
from langchain_unstructured.document_loaders import UnstructuredLoader

logger = logger.get_logger(__name__)
class IngetionService:
    def __init__(self):
        pass

    def loadDocument(self,filePath:str,doc_type:str) -> list[Document]:
        logger.info(f"Inside the loadDocument function in IngetionService")
        try:
            if filePath.endswith(".pdf"):
                loader = PyPDFLoader(filePath)
            elif filePath.endswith(".txt"):
                loader = TextLoader(filePath)
            else:
                loader = CSVLoader(filePath)
            docs = loader.load()
            logger.info(f"File loaded successfully: {filePath}")
            return docs
        except Exception as e:
            logger.debug(f"Error occured while loading the file: {filePath}")
            logger.debug(e)

    ## This works for PDFs, DOCX, PPTX, HTML, TXT, MD, images, etc., since Unstructured detects file type internally. Needs
    def directoryLoad(self,folderPath:str) -> list[Document]:
        logger.info(f"Inside the directoryLoad function in IngetionService")
        try:
            logger.info(f"Folder path is : {folderPath}")
            loader = PyPDFDirectoryLoader(folderPath)
            docs = loader.load()
            if not docs:
                logger.warning(f"No documents were loaded from: {folderPath}")
            else:
                logger.info(f"Loaded {len(docs)} documents from: {folderPath}")

            return docs
        except Exception as e:
            logger.debug(f"Error occured while loading the folder: {folderPath}")
            logger.debug(e)

