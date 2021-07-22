#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
# ~ https://github.com/1ber
# ~ https://raw.githubusercontent.com/1ber/bio_informatics/main/License.txt
# ~ http://rosalind.info/problems/mrna/


def main():
    # RNA codon table http://rosalind.info/glossary/rna-codon-table/
    
    
    # There are 20 common amino acids, but some amino acids cand be
    # transcripted from more than one codon, lke GCU and GCC, both are
    # encoded to the amino acid "a".
    # I'm using small letters for the amino acids just to avoid
    # collisions in intermediate steps of analysis, the answers
    # should be in upper case letters
    # There are 3 combinations for the stop codon
    rna_codons={
        "UUU":"f" , "CUU":"l" , "AUU":"i" , "GUU":"v" , "UUC":"f" , "CUC":"l" , "AUC":"i" , "GUC":"v" , "UUA":"l" , "CUA":"l" , "AUA":"i" 
        , "GUA":"v" , "UUG":"l" , "CUG":"l" , "AUG":"m" , "GUG":"v" , "UCU":"s" , "CCU":"p" , "ACU":"t" , "GCU":"a" , "UCC":"s" , "CCC":"p"
        , "ACC":"t" , "GCC":"a" , "UCA":"s" , "CCA":"p" , "ACA":"t" , "GCA":"a" , "UCG":"s" , "CCG":"p" , "ACG":"t" , "GCG":"a" , "UAU":"y"
        , "CAU":"h" , "AAU":"n" , "GAU":"d" , "UAC":"y" , "CAC":"h" , "AAC":"n" , "GAC":"d" , "UAA":"stop" , "CAA":"q" , "AAA":"k" , "GAA":"e"
        , "UAG":"stop" , "CAG":"q" , "AAG":"k" , "GAG":"e" , "UGU":"c" , "CGU":"r" , "AGU":"s" , "GGU":"g" , "UGC":"c" , "CGC":"r" , "AGC":"s"
        , "GGC":"g" , "UGA":"stop" , "CGA":"r" ,  "AGA":"r" , "GGA":"g" , "UGG":"w" , "CGG":"r" , "AGG":"r" , "GGG":"g" 
    }

    # ~ sample_dataset = "MA"
    sample_dataset = "MRPRGPKAAEQVKLSKEIRMTVDIYKVFLYMWRENNLEYIHIVGILCQKDTQQHLRCHKGLMYNQTPAPFQFKRPRGPGHVGCPFKLTANQKPWGQDMAAIIDFQGWYLIYKNQNEVGNPHFMWSTRTFLWECHEVGMWHYGLGPMAGVAPKSPFRSWYQMLIGVYWITKICQADLLTGRALDFDDWGEFNWVKWCAMFHGQEISQQWGVGYVMSMFVQSPVDFTAGYCKHEAGPRIKNSWQSIQDDSSLYSRQHPMYDNFYAESRVYYAWDPGWCDICSRARYAGLGTWNMQWCQNLMCMENAGWNETLGRMKMNYSEVKWAPWNWWRRSFQDLKNQRRIRDCVMHSWKPQDNVFDDCSAYITWHLMGYGLGRNYSSQLCWVWRDTAACCSKGLMLAFMAQCLIMTMDLNEDNDRQTKNQWYDRRMFRFWELTITLMTAWNWTKSFGCAFPCTNYAIKQHVVQELPPQLRMCDSDPTDCSSCRSNYFTAGRSWGDDQPPNEDFGFKSKGVIVKYNYIGVTYWFCYCFFTCQLCSARYGYIHKFPRCQIMHTHVVCQAPMWNPKSQCMLAHVGDSSNSCETYYRWEACEESCKMMCTHHHGMGVEEMVTMLRQKECEDCFFRPLGRMAPDGDENHYFYYRGYQEVWQSDQMYWPWYDFYTGTMGVEGAFDTYCREAWKWEALGTPNPWPVCVVLVSIRPHIEVWVSDQANNKTPKLRVGWNSVMQLDAQTYNPVWKMTYNSHGLNCTNTVYEMSPVPVMKMCRCDSNHYYPCGIGHRNKPINETGEDQVCNMCSNCWVLPTSPRDGPRYYEICALKPIRKGPDQMRNPYGTNTGPKKMQHGFRKVDVRMTWHVPCRACYYWPDGLDLRLHGEGIRFCVEQEFGDTRQVFFTFGGHSMTEQEAPIKGPFNNWHIYHHMTKERTKCRRAFKMMFFELDWNTWGKEMMPNSTWHIHYMWWMWNRWPGQQKIIADNKPDCTPDVYISCPCKTSHQKWDILN"
    counter=1
    #lower just to match the case of the values in the dict
    for l in sample_dataset.lower():
        counter = counter * list(rna_codons.values()).count(l)
    #The problem wants just the module from the division by 1000000
    print( (counter*3 % 1000000 ) )


if __name__ == "__main__":
    
    main()

