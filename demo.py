#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:12:58 2017

@author: sumairazaman
"""
#This script calculate GC content

#open the file and stores it in the variable fh
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
#store lines from fh in to list called lines
lines=fh.readlines()

NumGenes=0
for l in lines:
    #print l
    if l[0]==">":
        NumGenes=NumGenes+1
print NumGenes

countA=0
countG=0
countC=0
countT=0
nucleotides=0
for l in lines:
    if l[0]!=">":
        for nuc in l:
            if nuc=="A":
                countA=countA+1
                nucleotides=nucleotides+1
            elif nuc=="G": 
                countG=countG+1
                nucleotides=nucleotides+1
            elif nuc=="C": 
                countC=countC+1
                nucleotides=nucleotides+1
            elif nuc=="T": 
                countT=countT+1
                nucleotides=nucleotides+1
            else:
                print "it's probably a new line character"
print "A:", countA
print "G:", countG
print "C:", countC
print "T:", countT 
print nucleotides
print countA+countG+countT+countC

GC=(countG+countC)/nucleotides
print "GC content is: ", GC

GC=(countG+countC)/float(nucleotides)
print "GC content is: ", GC








