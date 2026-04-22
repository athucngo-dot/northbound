def normalize_name(name: str) -> str:
    # Normalize names by stripping whitespace and capitalizing each word
    return " ".join(
        word.capitalize()
        for word in name.strip().split()
    )