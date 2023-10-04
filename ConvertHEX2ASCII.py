# Открываем исходный файл для чтения и результирующий файл для записи
with open('hashcat.potfile', 'r') as input_file, open('output_raw.txt', 'w') as output_file:
    # Итерируемся по строкам в исходном файле
    for line in input_file:
        # Находим позицию символов "*" и ":"
        star_index = line.find('*')
        colon_index = line.find(':')
        
        # Если "*" и ":" найдены
        if star_index != -1 and colon_index != -1:
            # Получаем текст между "*" и ":"
            hex_string = line[star_index+1:colon_index]
            
            # Получаем текст после ":"
            text_after_colon = line[colon_index+1:]
            
            try:
                # Конвертируем строку из HEX в ASCII
                ascii_string = bytearray.fromhex(hex_string).decode('utf-8')
                
                # Записываем расшифрованный текст + текст после ":" в результирующий файл
                output_file.write('"' + ascii_string + '"' + ' wpa2 ' + text_after_colon)
            except ValueError:
                # Если не удается расшифровать строку, выводим предупреждение
                print(f"Невозможно расшифровать строку: {line.strip()}")
        else:
            # Если "*" и ":" не найдены, записываем строку без изменений
            #output_file.write(line)
            print(f"Строка без изменения: {line}")

# Выводим сообщение о завершении преобразования
print("Преобразование завершено.")

