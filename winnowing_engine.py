import hashlib


def get_kgrams(text: str, k: int) -> list:
    """Step 1 & 2: Clean text and generate overlapping k-grams."""
    clean_text = ''.join(char for char in text if char.isalnum()).lower()
    return [clean_text[i:i+k] for i in range(len(clean_text) - k + 1)]


def hash_string(string: str) -> int:
    """Step 3: Convert a k-gram into an integer hash."""
    return int(hashlib.md5(string.encode('utf-8')).hexdigest()[:8], 16)


def generate_fingerprints(text: str, k: int = 10, w: int = 5) -> set:
    """
    Step 4: The Winnowing process.
    Slides a window of size W across the hash list and keeps
    the minimum hash in each window (the document fingerprint).
    """
    kgrams = get_kgrams(text, k)
    hashes = [hash_string(kg) for kg in kgrams]

    fingerprints = set()
    for i in range(len(hashes) - w + 1):
        window = hashes[i:i+w]
        fingerprints.add(min(window))

    return fingerprints