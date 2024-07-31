import string

def build_markov_chain(text):
  # Remove punctuation and split into words
  
  changes = str.maketrans('', '', string.punctuation)
  words = text.translate(changes).split(' ')

  # Initialize Markov chain dictionary
  markov_chain = {}

  # Iterate through word pairs
  for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    # Update Markov chain dictionary
    if current_word in markov_chain:
      next_words = markov_chain[current_word]
      if next_word in next_words:
        next_words[next_word] += 1
      else:
        next_words[next_word] = 1
    else:
      markov_chain[current_word] = {next_word: 1}

  # Calculate transition probabilities
  for current_word, next_words in markov_chain.items():
    total_transitions = sum(next_words.values())
    for next_word, count in next_words.items():
      next_words[next_word] = count / total_transitions

  return markov_chain

# Example usage
text = '''Half a bee, philosophically,
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. D’you see?

But can a bee be said to be
Or not to be an entire bee
When half the bee is not a bee
Due to some ancient injury?'''

markov_chain = build_markov_chain(text)

