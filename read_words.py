from tensorflow.keras.preprocessing.text import text_to_word_sequence
import time


def count_words(filename, part_size=1024**3//4):
  with open(filename, "r") as f:
    word_counts = {}
    for part in read_in_chunks(f, part_size):
      words = text_to_word_sequence(part)
      for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def read_in_chunks(f, size):
  while True:
    chunk = f.read(size)
    if not chunk:
      break
    yield chunk


start = time.time()
w = count_words("random_words.txt")

  
end = time.time()
print("Time:", (end-start), "s")

print("writing to file...")
with open("output.txt","w") as file:
  for key, value in w.items():
    file.write(f"Palabra: {key}, Conteo: {value}\n")