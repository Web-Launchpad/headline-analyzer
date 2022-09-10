from .stats import get_headline_stats
from .inference import infer_headline_stats
from .wordbank import tokenize

def analyze_headline(headline: str):
  """Analyze a headline."""

  tokens = tokenize(headline)
  stats = get_headline_stats(headline)
  inference = infer_headline_stats(stats)

  result = {
    'headline': headline,
    'tokens': tokens,
    'stats': stats,
    'inference': inference
  }

  return result