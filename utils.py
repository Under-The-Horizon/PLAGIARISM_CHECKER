from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Loaded once when the server starts — keeps subsequent requests fast
print("Loading Machine Learning Paraphrasing Model... (this may take a few seconds)")
_semantic_model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_similarity(documents: list) -> list:
    """
    Takes a list of document texts, converts them to semantic embeddings,
    and returns a cosine-similarity matrix (list of lists, values 0-1).
    """
    if not documents:
        return []

    embeddings        = _semantic_model.encode(documents)
    similarity_matrix = cosine_similarity(embeddings)
    return similarity_matrix