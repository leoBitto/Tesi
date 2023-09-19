# Apre il file txt
with open('output_regressione.txt', 'r') as file:
    lines = file.readlines()

# Rimuove gli spazi multipli e aggiunge un tab alla fine di ogni riga
cleaned_lines = [' '.join(line.split()) + '\t\n' for line in lines]

# Salva il file con gli spazi corretti
with open('output_regressione_pulito.txt', 'w') as file:
    file.writelines(cleaned_lines)
