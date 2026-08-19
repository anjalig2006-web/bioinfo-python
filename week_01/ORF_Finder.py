def main():

# Take input from the user and print actual DNA seuence
    dna = input("Enter the DNA sequence: ").upper().strip()
    print("DNA sequence:", dna)

# Print the position of start and stop codon
    start_codon, stop_codon = orf(dna)
    print ("Start codon position in the given DNA sequence is: ", start_codon + 1)
    print ("Stop codon position in the given DNA sequence is: ", stop_codon + 1)

# Print the orf sequence
    orf_sequence = get_orf(dna, start_codon, stop_codon)
    print ("ORF sequence is: ", orf_sequence)

# Find the start codon in the given dna sequence
def orf(dna):
    start_codon = ""
    for i in range (len(dna)):
        if dna [i : i+3] == "ATG":
            start_codon = i
            start = i
            break

# Find the stop codon in the given dna sequence
    stop_codon = ""
    for i in range (start, len(dna), 3):
        codon = dna[i: i+3]
        if codon == "TAA" or codon == "TAG" or codon == "TGA":
            stop_codon = i
            break

    return start_codon, stop_codon

# Return the orf sequence from start codon to the complete stop codon
def get_orf (dna,start_codon ,stop_codon):
    orf_sequence = dna [start_codon:stop_codon + 3]
    return orf_sequence

# Call main
if __name__ == "__main__":
    main()
