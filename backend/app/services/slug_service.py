def make_unique_slug(slug: str, exists_fn) -> str:
    base = slug
    counter = 1

    while exists_fn(slug):
        slug = f"{base}-{counter}"
        counter += 1

    return slug