from .count_words import count_words
from .count_characters import count_characters
from .headline_stats import HeadlineStats

def get_headline_stats(headline: str) -> HeadlineStats:
  if(type(headline) != str):
    raise TypeError('headline must be a string')

  result = HeadlineStats(
    character_count = count_characters(headline), 
    word_count = count_words(headline))

  return result

