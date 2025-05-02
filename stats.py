def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    words = text.split()
    char_count = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count


def sort_dict(d):
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict