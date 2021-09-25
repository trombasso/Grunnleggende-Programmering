def check_if_gene(genome):
    genome_start = 0
    genome_end = len(genome)
    genome_length = len(genome)
    sequenze = []
    positive_pos = 10000

    while "ATG" in genome[genome_start:genome_length]:
        genome_start += genome[genome_start:genome_length].find("ATG") + 3

        x = genome[genome_start:genome_length]
        if x.find("ATG") != -1:
            ATG_pos = x.find("ATG") + genome_start + 1
        else:
            ATG_pos = positive_pos

        if x.find("TAG") != -1:
            TAG_pos = x.find("TAG") + genome_start + 1
        else:
            TAG_pos = positive_pos

        if x.find("TAA") != -1:
            TAA_pos = x.find("TAA") + genome_start + 1
        else:
            TAA_pos = positive_pos

        if x.find("TGA") != -1:
            TGA_pos = x.find("TGA") + genome_start + 1
        else:
            TGA_pos = positive_pos

        if ATG_pos == positive_pos and TAA_pos == positive_pos and TGA_pos == positive_pos and TAG_pos == positive_pos:
            break

        if ATG_pos < TAA_pos and ATG_pos < TGA_pos and ATG_pos < TAG_pos:
            genome_start = ATG_pos + 3
            continue
        elif TAG_pos < ATG_pos and TAG_pos < TAA_pos and TAG_pos < TGA_pos:
            genome_end = TAG_pos - 1
        elif TAA_pos < ATG_pos and TAA_pos < TAG_pos and TAA_pos < TGA_pos:
            genome_end = TAA_pos - 1
        elif TGA_pos < ATG_pos and TGA_pos < TAA_pos and TGA_pos < TAG_pos:
            genome_end = TGA_pos - 1

        sequenze.append(genome[genome_start : (genome_end - (len(genome[genome_start:genome_end]) % 3))])
        genome_start = genome_end

    if sequenze:
        print("\nGenome strings found:")
        print("-------------------------")
        for x in sequenze:
            if x == "":
                pass
            else:
                print(x)
        print("-------------------------\n")
    else:
        print("\nNo gene is found.")


def main():
    genome = input("Enter a genome string: ").upper()
    check_if_gene(genome)


if __name__ == "__main__":
    main()
