print("Enter your Paragraph: ")
paragraph = input()
words = paragraph.split()
palindromes = []
for word in words:
    clean=word.lower().strip('.,!?;"()[]{}')
    if clean==clean[::-1] and len(clean)>1:
        palindromes.append(clean)
print("Palindromic words:", palindromes)            
