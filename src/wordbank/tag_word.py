from .tag_from_wordbanks import tag_from_wordbanks

def tag_word(word: str) -> tuple[str, str]:
    return (word, tag_from_wordbanks(word))



