def count_letter_a(string):
    count = string.lower().count('a')
    return count

input_string = input("Informe uma string: ")
count = count_letter_a(input_string)
print(f"A letra 'a' aparece {count} vez(es) na string.")
