import io


def process_line(file_line):
    newline = file_line.replace(' ', '').replace('\t', '|')
    while newline.find('||') != -1:
        newline = newline.replace('||', '|NaN|')
    return newline


datos_tsv = io.open('datos_data_engineer.tsv', 'r', encoding='utf-16-le')
datos_csv = io.open('datos_data_engineer.csv', 'w', encoding='utf-8')

line = datos_tsv.readline()
while line != "":
    nextLine = datos_tsv.readline()
    if nextLine != "" and not nextLine[0].isdigit():
        line = line.replace('\n', '') + nextLine
    else:
        line = process_line(line)
        datos_csv.write(line)
        line = nextLine

datos_csv.close()
datos_tsv.close()
