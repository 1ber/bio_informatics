#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#License http://www.apache.org/licenses/

def main():
    #http://rosalind.info/problems/dna/
    cadeia_dna="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    #Substituir T por um
    cadeia_rna=cadeia_dna.replace( 'T', 'U' )
    print( cadeia_rna )
        
if __name__ == "__main__":
    
    main()

