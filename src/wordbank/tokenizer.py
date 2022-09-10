from .tag_word import tag_word

def tokenize(headline: str) -> list[tuple[str, str]]:
  """Tokenize a headline into a list of tuples."""
  words = headline.split()

  tokens = [tag_word(word) for word in words]
  return tokens

