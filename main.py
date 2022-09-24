from src.headline_analyzer.analyze_headline import analyze_headline
from src.headline_analyzer.utils.pretty_print import pretty_print


headline = input('Enter a headline: ')


# test= 'Better emails mean bigger results'

# tokens = [('Better', 'persuasive'), ('emails', None), ( 'mean', None),  ('bigger', 'power'), ('results', None)]
result = analyze_headline(headline)

pretty_print(result)

