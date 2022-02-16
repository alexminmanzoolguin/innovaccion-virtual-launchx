print("texto original")
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest"""
print(text)
print("cortar texto")
text_parts=text.split('.')
print(text_parts)
print("palabras clave")
palabra=["average", "temperature","distance"]

print("para recorrer la cadena")
for sentence in text_parts:
    for palabra in palabra:
        if palabra in sentence:
            print(sentence)
            break
print("para cambiear de c a celsius")
for sentence in text_parts:
    for palabra in palabra:
        if palabra in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break