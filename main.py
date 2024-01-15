import heapq
from collections import defaultdict
import time

# Program untuk kompresi teks menggunakan metode Run-Length Encoding (RLE) dan Huffman Coding.

# Fungsi untuk melakukan kompresi menggunakan RLE (Run-Length Encoding).
def compress_rle(text):
    compressed_text = ""
    count = 1

    # Iterasi melalui teks dan melakukan kompresi RLE.
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed_text += text[i - 1] + str(count)
            count = 1

    compressed_text += text[-1] + str(count)

    return compressed_text

# Fungsi untuk membangun pohon Huffman berdasarkan frekuensi karakter.
def build_huffman_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0][1:]

# Fungsi untuk melakukan kompresi menggunakan Huffman Coding.
def huffman_compress(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1

    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = {char: code for char, code in huffman_tree}
    compressed_text = ''.join(huffman_codes[char] for char in text)

    return compressed_text, huffman_codes

# Fungsi untuk mengukur waktu dan ukuran data sebelum dan setelah kompresi.
def measure_time_and_size(text, compressed_text):
    original_size = len(text)
    compressed_size = len(compressed_text)
    compression_ratio = original_size / compressed_size

    return original_size, compressed_size, compression_ratio

# Fungsi utama program.
def main():
    # Membaca teks dari file text.txt
    try:
        with open('text.txt', 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return

    # Kompresi menggunakan RLE
    start_time = time.time()
    compressed_rle = compress_rle(input_text)
    rle_time = time.time() - start_time
    rle_original_size, rle_compressed_size, rle_ratio = measure_time_and_size(input_text, compressed_rle)

    print("\n=== Kompresi RLE ===")
    print("Teks Asli:", input_text)
    print("Teks Terkompresi (RLE):", compressed_rle)
    print(f"Ukuran Data Sebelum Kompresi: {rle_original_size} byte")
    print(f"Ukuran Data Setelah Kompresi: {rle_compressed_size} byte")
    print(f"Rasio Kompresi: {rle_ratio:.2f}")
    print(f"Waktu Pengiriman: {rle_time:.6f}\n")

    # Kompresi menggunakan Huffman
    start_time = time.time()
    compressed_huffman, huffman_codes = huffman_compress(input_text)
    huffman_time = time.time() - start_time
    huffman_original_size, huffman_compressed_size, huffman_ratio = measure_time_and_size(input_text, compressed_huffman)

    print("=== Kompresi Huffman ===")
    print("Teks Asli:", input_text)
    print("Teks Terkompresi (Huffman):", compressed_huffman)
    print("Tabel Kode Huffman:", huffman_codes)
    print(f"Ukuran Data Sebelum Kompresi: {huffman_original_size} byte")
    print(f"Ukuran Data Setelah Kompresi: {huffman_compressed_size} byte")
    print(f"Rasio Kompresi: {huffman_ratio:.2f}")
    print(f"Waktu Pengiriman: {huffman_time:.6f}")

# Memastikan bahwa program dijalankan hanya jika ini adalah file utama.
if __name__ == "__main__":
    main()
