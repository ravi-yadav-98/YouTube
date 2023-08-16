
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
import pinecone
from PIL import Image 
import streamlit as st
import os
openai_key = os.environ.get('OPENAI_API_KEY')
print(openai_key)
pinecone_key = 'pine cone api key'
pinecone_env = 'gcp-starter'


#Start Building Application 

#title
st.title("AI PDF Retriever")
st.subheader("Chat with multiple pdfs")

#upload files
uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)

#input prompt
prompt = st.text_input("Ask a question about the PDF content")

#prompt template
script_template = PromptTemplate(
    input_variables=['question', 'context'],
    template='write an answer for this: {question}\n{context}\n Answer:'
)

#LLMs
model_name  = 'gpt-3.5-turbo'
llm = ChatOpenAI(temperature=0.2, model_name= model_name)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key = 'question')

#process file

@st.cache_resource
def process_file(uploaded_file):

    byte_data = uploaded_file.read()
    st.write("filename: ", uploaded_file.name)
    _, file_extention = os.path.splitext(uploaded_file.name)

    #write tje uploaded file to the disk 
    with open(uploaded_file.name,  'wb') as f:

        f.write(byte_data)
    
    document = None 

    if file_extention.lower() == '.pdf':
        loader = PyPDFLoader(uploaded_file.name)
        document = loader.load()
    
    elif file_extention.lower() == '.txt':
        loader = TextLoader(uploaded_file.name, encoding='utf8')
        document = loader.load()
    else:
        raise ValueError(f"unsupported file type: {file_extention}")

    return document


#Function to split docs

def split_docs(documents, chunk_size=1000, chunk_overlap =20):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


#embeddings
embeddings = OpenAIEmbeddings()

docs_chunks = []

if len(uploaded_files)>0:
    for uploaded_file in uploaded_files:
       documents = process_file(uploaded_file=uploaded_file)
       docs_chunks.extend(split_docs(documents))

#start pinecone

pinecone.init(
    api_key=pinecone_key,
    environment=pinecone_env
)

@st.cache_resource
def get_index_name():
    index_name = 'chat-pdf'
    return index_name

@st.cache_resource
def load_pinecone_index():
    index_name = get_index_name()
    index = Pinecone.from_documents(docs_chunks, embeddings, index_name=index_name )
    return index

index = load_pinecone_index()

#find similar documents
#k = top k similar docs 

def get_similar_docs(query, k=2, score = False):
    if score:
        similar_docs = index.similarity_search_with_score(query, k = k)
    else:
        similar_docs = index.similarity_search(query=query, k=k)
    
    return similar_docs

#question answering

chain = load_qa_chain(llm=llm, chain_type='stuff', verbose=True)

def get_answer(query):
    #get similar docs
    similar_docs = get_similar_docs(query=query)

    #generate answer using script chain
    answer = chain.run(input_documents = similar_docs, question = query)
    return answer

if st.button("Ask"):
    question = prompt
    answer = get_answer(question)
    st.write(answer)
    
    