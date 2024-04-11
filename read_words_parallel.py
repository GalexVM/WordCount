from multiprocessing import Pool
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import time

def count_words_chunk(chunk):
  word_counts = {}
  words = text_to_word_sequence(chunk)
  for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
  return word_counts

def count_words(filename, part_size=1024**3//3):
  with open(filename, "r") as f:
    chunks = read_in_chunks(f,part_size)
    with Pool() as pool:
        word_counts_chunks = pool.map(count_words_chunk,chunks)
    word_counts = {}
    for word_counts_chunk in word_counts_chunks:
        for word, count in word_counts_chunk.items():
            word_counts[word] = word_counts.get(word,0)+count
    return word_counts


def read_in_chunks(f, size):
  while True:
    chunk = f.read(size)
    if not chunk:
      break
    yield chunk

if __name__ == '__main__':
    start = time.time()
    w = count_words("random_words_mini.txt")   
    end = time.time() 
    print("Time:", (end-start), "s")
    print("writing to file...")
    with open("output.txt","w") as file:
      for key, value in w.items():
        file.write(f"Palabra: {key}, Conteo: {value}\n")
  