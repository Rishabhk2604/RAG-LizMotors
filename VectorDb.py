from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load data from CSV
loader = CSVLoader(file_path='about_data.csv', csv_args={
    'delimiter': ',',
    'fieldnames': ['Source', 'About Us', 'About Wiki','Industries','key market size','Growth rate and trends','key players','competitors','canoos financial peformance']
})
data = loader.load()

# Split text into chunks (if needed)
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
docs = text_splitter.split_documents(data)

# Create embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Load documents into Chroma
db = Chroma.from_documents(docs, embedding_function)

# Query Chroma
query = "Gather information on Canoo's financial performance, including its revenue, profit margins, return on investment, and expense structure. "
results = db.similarity_search(query)

# Initialize PDF canvas
pdf_file_path = "search_results2.pdf"
c = canvas.Canvas(pdf_file_path, pagesize=letter)

# Initialize text file
text_file_path = "results.txt"

# Print results to PDF and text file
if results:
    for i, doc in enumerate(results, start=1):
        result_text = f"Document {i}: {doc.page_content}"
        c.drawString(10, 800 - i * 20, result_text)
        with open(text_file_path, "a") as file:
            file.write(result_text + "\n")
else:
    c.drawString(10, 800, "No similar documents found.")
    with open(text_file_path, "w") as file:
        file.write("No similar documents found.")

# Save PDF file
c.save()
