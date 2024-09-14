# Credit by Zidan IDz
# Open Source untuk Tujuan Pembelajaran

import time
import marshal
import base64

def main():
    time.sleep(0.5)
    icon("Compile Marshall")
    print('1. Marshal')
    print('2. Marshal (base64)')
    print('3. Keluar')
    index = input('\nPilih Opsi >> ')
    if index == '1':
        first()
    elif index == '2':
        second()
    elif index == '3':
        exit()
    else:
        print("\nPilihan tidak valid. Silakan coba lagi.")
        time.sleep(1)
        main()

def first():
    file = input('\nFile >> ')
    echo = int(input('\nEcho (Max 300) >> '))

    if echo <= 300:
        output = file.replace('.py', '') + '_enc.py'
        try:
            with open(file, 'r') as f:
                source = f.read()

            codec = compile(source, '<Haze>', 'exec')
            codem = marshal.dumps(codec)

            mark(output, codem)
            repeat(output, echo)
        except FileNotFoundError:
            print(f'\nFile {file} tidak ditemukan!')
            main()
    else:
        print('\nJumlah Echo terlalu besar!')
        main()

def second():
    file = input('\nFile >> ')
    echo = int(input('\nEcho (Max 300) >> '))

    if echo <= 300:
        output = file.replace('.py', '') + '_enc.py'
        try:
            with open(file, 'r') as f:
                source = f.read()

            codec = compile(source, '<Haze>', 'exec')
            codem = marshal.dumps(codec)

            mark(output, codem)
            repeat(output, echo)

            with open(output, 'r') as f:
                compiled = f.read()
            encoded = base64.b64encode(compiled.encode())

            with open(output, 'w') as encoded_file:
                encoded_file.write(f"#Credit by Zidan IDz\nimport base64\nexec(base64.b64decode('{encoded.decode()}'))\n")

            print(f"\nFile berhasil disimpan: {output}")
        except FileNotFoundError:
            print(f'\nFile {file} tidak ditemukan!')
            main()
    else:
        print('\nJumlah Echo terlalu besar!')
        main()

def mark(output, codem):
    with open(output, 'w') as credit:
        credit.write(f"#Credit by Zidan IDz\nimport marshal\nexec(marshal.loads({repr(codem)}))")

def repeat(output, echo):
    zero = 0
    while zero < echo:
        try:
            with open(output, 'r') as f:
                source = f.read()
            codec = compile(source, '<Haze>', 'exec')
            codem = marshal.dumps(codec)

            mark(output, codem)
            zero += 1
        except FileNotFoundError:
            print(f'\nFile {output} tidak ditemukan!')
            break

    print(f"\nFile berhasil disimpan: {output}")

def icon(title):
    border = "─" * 55
    print(f"""
{border}
    ══════════════ {title} ══════════════
{border}
""")



if __name__ == "__main__":
    main()
  
