
import matplotlib.pyplot as plt
# Example word frequency dictionary
word_freq = {
    'the': 5242,
    'and': 4897,
    'to': 4293,
    'of': 4132,
    'a': 3191,
    'in': 3144,
    'it': 2529,
    'is': 2483,
    'that': 2400,
    'was': 2364
}

# Extract frequencies
frequencies = list(word_freq.values())

# Plot histogram
print(frequencies)
plt.hist(frequencies, bins=10, edgecolor='black')
plt.title('Histogram of Word Frequencies')
plt.xlabel('Frequency')
plt.ylabel('Number of Words')
plt.show()
