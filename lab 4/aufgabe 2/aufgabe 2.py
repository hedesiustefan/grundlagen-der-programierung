def replace_words_in_file(aufgabe2, replacements):
    try:
        with open(aufgabe2, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    replaced_count = 0
    for word, replacement in replacements.items():
        content, count = content.replace(word, replacement), content.count(word)
        replaced_count += count

    if replaced_count > 0:
        with open(aufgabe2, 'w') as file:
            file.write(content)
        print(f"Replacements made: {replaced_count}")
    else:
        print("No replacements were made.")


# Example usage:
aufgabe2 = 'aufgabe2.txt'  # Replace 'input.txt' with the path to your text file
replacements = {
    'plumb': 'fier',
    # Add more word replacements as needed
}

replace_words_in_file(aufgabe2, replacements)
