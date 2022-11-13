PROTEIN_DICT = {
    # Phenylalanine
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}


def protein(rna):
    result = ""
    for i in range(len(rna) // 3):
        p = PROTEIN_DICT[rna[i * 3: (i + 1) * 3]]
        if p == "Stop":
            return result
        result += PROTEIN_DICT[rna[i * 3: (i + 1) * 3]]
    return result


def test_protein():
    assert protein("AUG") == "M"
    assert protein("AUGUGA") == "M"
    assert protein("AUGGUUAGUUGA") == "MVS"
    assert protein("UGCGAUGAAUGGGCUCGCUCC") == "CDEWARS"
    assert protein(
        "AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA") == "MSFHQGNHARSAF"
    assert protein(
        "AUGCUUCAAGUGCACUGGAAAAGGAGAGGGAAAACCAGUUGA") == "MLQVHWKRRGKTS"
    assert protein(
        "AUGGCGUUCAGCUUUCUAUGGAGGGUAGUGUACCCAUGCUGA") == "MAFSFLWRVVYPC"
    assert protein(
        "AUGCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCUGA") == "MQLSMEGSVNYHA"
    assert protein(
        "AUGCUAUGGAGGGUAGUGUUAACUACCACGCCCAGUACUUGA") == "MLWRVVLTTTPST"
    assert protein(
        "AUGUAUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUAUGGAGGGUAGUGUUAACUACCACGCCU"
        "UCAAGUGCACUGGAAAAGGAGAGGGAAAACCAUACGAAGGCACCCAAAGCCUGAAUAUUACAAUAACUGA"
        "AGGAGGUCCUCUGCCAUUUGCUUUUGACAUUCUGUCACACGCCUUUCAGUAUGGCAUCAAGGUCUUCGCC"
        "AAGUACCCCAAAGAAAUUCCUGACUUCUUUAAGCAGUCUCUACCUGGUGGUUUUUCUUGGGAAAGAGUAA"
        "GCACCUAUGAAGAUGGAGGAGUGCUUUCAGCUACCCAAGAAACAAGUUUGCAGGGUGAUUGCAUCAUCUG"
        "CAAAGUUAAAGUCCUUGGCACCAAUUUUCCCGCAAACGGUCCAGUGAUGCAAAAGAAGACCUGUGGAUGG"
        "GAGCCAUCAACUGAAACAGUCAUCCCACGAGAUGGUGGACUUCUGCUUCGCGAUACCCCCGCACUUAUGC"
        "UGGCUGACGGAGGUCAUCUUUCUUGCUUCAUGGAAACAACUUACAAGUCGAAGAAAGAGGUAAAGCUUCC"
        "AGAACUUCACUUUCAUCAUUUGCGUAUGGAAAAGCUGAACAUAAGUGACGAUUGGAAGACCGUUGAGCAG"
        "CACGAGUCUGUGGUGGCUAGCUACUCCCAAGUGCCUUCGAAAUUAGGACAUAACUGA"
    ) == (
               "MYPSIKETMRVQLSMEGSVNYHAFKCTGKGEGKPYEGTQSLNITITEGGPLPFAFDILSHAFQ"
               "YGIKVFAKYPKEIPDFFKQSLPGGFSWERVSTYEDGGVLSATQETSLQGDCIICKVKVLGTNF"
               "PANGPVMQKKTCGWEPSTETVIPRDGGLLLRDTPALMLADGGHLSCFMETTYKSKKEVKLPEL"
               "HFHHLRMEKLNISDDWKTVEQHESVVASYSQVPSKLGHN"
           )