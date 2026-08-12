def main():

    # Take dna seq input from the user and print it
    dna = input ("Enter the DNA sequence: ").upper().strip()
    print ("Entered DNA seq: ",dna)

    # Take motif input from user, verify it and print
    while True:
        motif = input ("Enter the motif: ").upper().strip()
        try:
            validate_motif(motif)
            break
        except ValueError:
            print ("Invalid motif. Try Again.")
    print ("Entered motif sequence:", motif)

    # Print the position of motif found after analysis
    p = motif_analysis(dna, motif)
    print ("The position of motif in the given dna sequence is :", p)

# Check motif entered by the user
def validate_motif(motif):
    for letter in motif:
        if letter not in "ATGC":
            raise ValueError("Invalid motif")

# Analyse the position of motif
def motif_analysis(dna, motif):
    position = []
    for i in range (len(dna)):
        if dna [i:i+ len(motif)] == motif:
            position.append(i+1)
    return position

if __name__ == "__main__":
    main()
