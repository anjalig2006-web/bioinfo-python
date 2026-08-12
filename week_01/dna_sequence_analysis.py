def main():

    # Take input of DNA seq from user and print the correct dna sequence
    while True:
        dna = input("Enter DNA sequence: ").upper().strip()
        
        try:
            validate_sequence(dna)
            break

        except ValueError:
            print("Invalid DNA sequence. Try again.")

    print ("Give DNA seq is: ",dna)

    # Print the length of the dna sequence
    l = length(dna)
    print("Length of the given DNA seq is: ",l)

    # Print the total number of A,T,G,C in sequence
    A, T, G, C = count (dna)
    print ("Number of adenine (A) in the given DNA seq are: ",A)
    print ("Number of thymine (T) in the given DNA seq are: ",T)
    print ("Number of guanine (G) in the given DNA seq are: ",G)
    print ("Number of cytosine (C) in the given DNA seq are: ",C)

    # Print the calculated GC, AT content 
    GC, AT = content (A,T,G,C,l)
    print ("Total GC content in the given DNA seq: ",GC,"%")
    print ("Total AT content in the given DNA seq: ",AT,"%")

    # Print occurence of motifs in the sequence
    m = motif_analysis (dna)
    print ("The number of motif seq in the DNA seq are: ",m)
    
# Check the user input and return correct dna seq else raise error
def validate_sequence (dna):
    for letter in dna:
        if letter not in "ATGC":
            raise ValueError("DNA sequence is incorrect")
    return dna

# Calculate the length of sequence
def length(dna):
    l = len(dna)
    return l

# Count A,T,G,C in the sequence
def count(dna):
    A_in_seq = dna.count ("A")
    T_in_seq = dna.count ("T")
    G_in_seq = dna.count ("G")
    C_in_seq = dna.count ("C")
    return A_in_seq, T_in_seq, G_in_seq, C_in_seq

# Calculate GC and AT content in the sequence
def content (A,T,G,C,l):
    GC_content = (G + C) / l * 100
    AT_content = (A + T) / l * 100
    return GC_content, AT_content

# Check if the given motif present in the sequence or not
def motif_analysis (dna):
    while True:
        motif = input("Enter the motif: ").upper().strip()

        try:
            validate_sequence(motif)
            break

        except ValueError:
            print("Invalid motif. Try again.")
    
    if motif in dna:
        m = dna.count(motif)
        return m
    else:
        return 0

if __name__ == "__main__":
    main()
