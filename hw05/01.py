# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text1 = input('Введите текст: ')
text2 = text1.replace('а', '').replace('б', '').replace('в', '')
print(text2)