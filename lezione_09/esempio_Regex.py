import re

text:str = "I have 20 cats and 3 dogs"
numbers:list[str] = re.findall(r"\d+", text)
print(numbers)
print("-"*30)

text:str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group())
print("-"*30)

for m in re.finditer(r"\d+", "a1b2"):
    print(m.group())
print("-"*30)

result1 = re.sub(r"\d", "#", "a1b2")
print(result1)
print("-"*30)

result2 = re.split(r"\d+", "a1b2c3")
print(result2)
print("-"*30)

pattern = re.compile(r"\d+")
result3 = pattern.findall("a1b2")
print(result3)
print("-"*30)

text:str = "Il codice è: 123-ABC"
match = re.search(r"(\d+)-([A-Z]+)", text)
if match:
   print("Intera corrispondenza:", match.group(0))
   print("Gruppo 1 (numeri):", match.group(1))
   print("Gruppo 2 (lettere):", match.group(2))

print("-"*30)

text:str = "123-ABC"
new_text:str = re.sub(r"(\d+)-([A-Z]+)", r"\2-\1", text)
print(new_text)
print("-"*30)

text:str = "abcabcabc"
print("Cattura:", re.findall(r"(abc)+", text)) 
print("Non cattura:", re.findall(r"(?:abc)+", text))

