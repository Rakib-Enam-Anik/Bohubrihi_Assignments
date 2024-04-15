def count_words(filename, search_words):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = {word: text.count(word) for word in search_words}
            return word_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

filename = "C:\Developments\Projects\Bohubrihi\Bohubrihi_Assignments\Python Assignments\WordCount\input.text"
search_words = ["Python", "C", "OOP", "Hello", "Java"]
word_counts = count_words(filename, search_words)
print("Word Counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")