with open('hashcat.potfile', 'r') as input_file, open('output_raw.txt', 'w') as output_file:
    for line in input_file:
        star_index = line.find('*')
        colon_index = line.find(':')
        if star_index != -1 and colon_index != -1:
            hex_string = line[star_index+1:colon_index]
            text_after_colon = line[colon_index+1:]
            try:
                ascii_string = bytearray.fromhex(hex_string).decode('utf-8')
                output_file.write('"' + ascii_string + '"' + ' wpa2 ' + text_after_colon)
            except ValueError:
                print(f"Невозможно расшифровать строку: {line.strip()}")
        else:
            print(f"Строка без изменения: {line}")
print("Преобразование завершено.")

