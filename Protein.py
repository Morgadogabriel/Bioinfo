# Dictionary for codon to amino acid translation
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

# mRNA sequence to translate
mRNA_seq = "AUGGCGUGUUGAUUGAGUUCGCGUUUGCGAGUCCAGCCUCCGACUCCGAAUCAAGUUUUGUCGAAUGGGGAGGUCAUCCACAUACCGCGCGCGUAA"

# Define a function to translate the mRNA sequence to protein sequence
def translate(mRNA_seq):
    codons = [mRNA_seq[i:i+3] for i in range(0, len(mRNA_seq), 3)] # Split mRNA sequence into codons
    protein_seq = ""
    for codon in codons:
        if codon in codon_table:
            protein_seq += codon_table[codon]
        else:
            protein_seq += "X" # Use "X" for unknown codons
    return protein_seq

# Translate the mRNA sequence
protein_seq = translate(mRNA_seq)

# Print the protein sequence
print(protein_seq)

def translate_to_protein(mrna_sequence):
    """
    Translates an mRNA sequence into a protein sequence in 3 open reading frames.
    """
    start_codon = "AUG"
    stop_codons = ["UAA", "UAG", "UGA"]
    protein_sequences = []

    for frame in range(3):
        protein_sequence = ""
        codon_index = frame

        while codon_index < len(mrna_sequence) - 2:
            codon = mrna_sequence[codon_index:codon_index + 3]
            if codon == start_codon:
                protein_sequence += "M"
                codon_index += 3
                while codon_index < len(mrna_sequence) - 2:
                    codon = mrna_sequence[codon_index:codon_index + 3]
                    if codon in stop_codons:
                        break
                    amino_acid = codon_table[codon]
                    protein_sequence += amino_acid
                    codon_index += 3
            else:
                codon_index += 3

        protein_sequences.append(protein_sequence)
        print(protein_sequence)

    return protein_sequences