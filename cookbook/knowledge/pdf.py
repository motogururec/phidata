from phi.agent import Agent
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector2

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Create a knowledge base with the PDFs from the data/pdfs directory
knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=PgVector2(
        collection="pdf_documents",
        # Can inspect database via psql e.g. "psql -h localhost -p 5432 -U ai -d ai"
        db_url=db_url,
    ),
    reader=PDFReader(chunk=True),
)
# Load the knowledge base
knowledge_base.load(recreate=False)

# Create an agent with the knowledge base
agent = Agent(
    knowledge_base=knowledge_base,
    add_references_to_prompt=True,
)

# Ask the agent about the knowledge base
agent.print_response("Ask me about something from the knowledge base", markdown=True)
