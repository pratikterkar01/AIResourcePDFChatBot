from tensorflow.python.ops.initializers_ns import global_variables
from langchain_huggingface import HuggingFaceEmbeddings
from Utils import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader,PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from Utils import Config
from langchain_chroma import Chroma
logger = logger.get_logger(__name__)
global_variables = Config.get_settings()

class IngetionService:
    def __init__(self):
        pass

    def load_document(self,filePath:str) -> list[Document]:
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
            message = f"Error occured while loading the file: {filePath}"
            logger.debug(f"Error occured while loading the file: {filePath}")
            logger.debug(e)
            raise RuntimeError(message) from e
    ## This works for PDFs, since Unstructured detects file type internally. Needs
    def directory_load(self,folderPath:str) -> list[Document]:
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
            raise RuntimeError(e)
    ## convert into chunks
    def text_to_chunk_converter(self,fileContentText:str):
        logger.info(f"Inside the textToChunkConverter function in IngetionService")
        try:
            chunkSize = global_variables.ChunkSize
            chunkOverlap = global_variables.ChunkOverlap
            splitter = RecursiveCharacterTextSplitter(chunk_size=chunkSize, chunk_overlap=chunkOverlap)
            chunk = splitter.create_documents([fileContentText])
            logger.info(f"Chunk created successfully:")
            return chunk
        except Exception as e:
            logger.debug(f"Error occured while converting file to chunks")
            logger.debug(e)
            raise RuntimeError(e)
    def embedingConverter(self,chunkList:list[Document]):
        logger.info(f"Inside the embedingConverter function in IngetionService")
        message = ""
        try:
            logger.info(f"The len chunk list for the embeding is: {len(chunkList)} ")
            embedding = HuggingFaceEmbeddings(model_name=global_variables.HuggingfaceEmbedingModelName)
            vector_store = Chroma.from_documents(documents=chunkList,embedding=embedding,
                                  persist_directory=global_variables.VetorDBPath,
                                  collection_name="sample"
                                  )

            logger.info(f"Document embedding created and vector Store saved successfully in path: {global_variables.VetorDBPath}:")
            message = f"Document embedding created and vector Store saved successfully in path: {global_variables.VetorDBPath}:"
            return message
        except Exception as e:
            message = "Failed to convert into embeding the saved in the vector Store"
            logger.error(f"Error occured while converting file to embeddings")
            logger.error(e)
            raise RuntimeError(e)
    def pdf_document_to_text_convertor(self,documentList:list[Document]):
        logger.info(f"Inside the pdfDocumentToTextConvertor function in IngetionService")
        try:
            textExtraction = " ".join((doc.page_content) for doc in documentList)
            logger.info(f"Document extracted successfully:  with length: {len(textExtraction)}")
            return textExtraction
        except Exception as e:
            logger.error(f"Error occured while converting file to text")
            logger.error(e)
    def vectorization_pipline(self,folderPath:str):
        logger.info(f"Inside the vectorizationPipline function in IngetionService")
        try:
            ## loade the files from the directory (In this case we only have pdf's)
            pdfLoader = self.directoryLoad(folderPath)
            ## Extract only page content from the document class and convert it into chunks
            textLoader = self.pdfDocumentToTextConvertor(pdfLoader)
            chunkCreation = self.textToChunkConverter(textLoader)
            ## Convert into the chunks and save in the vector db
            vectorStore = self.embedingConverter(chunkCreation)
            return vectorStore

        except Exception as e:
            logger.error(f"Error occured while converting file to vector")
            logger.error(e)
            raise RuntimeError(e)

