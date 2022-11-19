from .stats import get_headline_stats
from .inference import infer_headline_stats
from .wordbank import tokenize
from .wordbank import calculate_wordbank_percentage

def analyze_headline(headline: str):
  """Analyze a headline."""

  tokens = tokenize(headline)
  stats = get_headline_stats(headline)
  inference = infer_headline_stats(stats.__dict__)
  percentage = calculate_wordbank_percentage(tokens)

  result = {
    'headline': headline,
    'tokens': tokens,
    'stats': stats.__dict__,
    'inference': inference,
    'percentage': percentage
  }

  return result