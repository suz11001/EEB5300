#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 00:03:33 2017

@author: sumairazaman
"""

###playing with lists a LOT MORE

students = ["Tom", "Sarah", "Anne", "Bob"]
print students
students.append("Tyler")
print students
students.pop(4)
print students
students.remove("Anne")
print students
students.insert(2,"Anne")
print students

grades=[int]*4
print grades
grades[0]=90
grades[1]=88
grades[2]=94
grades[3]=93
print grades

program=[""]*4
print program
program.append("Masters")
program.append("phD")
program.append("Masters") 
program.append("phD")
print program

###opening a file

#only reading a text file
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
print fh.read()

#read one line at a time
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
print fh.readline()
print fh.readline()
print fh.readline()

#read it as a list of lines
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
print fh.readlines

#save the list of lines into a variable instead of printing it
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
lines=fh.readlines()
print lines[0]
for l in lines:
    print l

#close the file once you are done reading it
fh.close()

###write to an output file
fh=open("output.txt","w")
TextList=[lines[0],lines[1],lines[2],lines[3]]
fh.writelines(TextList)
fh.close


with open("temp.fasta", "w") as fout:
    for l in lines:
        fout.write(l)


###calculate GC content

#open the fasta file and save the lines into a list
fh = open("/Users/sumairazaman/Documents/EEB5300/CodingChallenge/demo.fasta","r")
lines=fh.readlines()

#initilize counters for each nucleotide 
A_count=0
T_count=0
G_count=0
C_count=0
#this var keeps track of ALL the nucleotides present in the sequence
nucleotides=0

#for each line in the fasta file (that is stored in the variable lines)
for line in lines:
    ###if the line is not a header
    if line[0]!=">":
        ###then proceed to count the nucleotides in the sequence
        for nuc in line: 
            if nuc=="A":
                A_count=A_count+1
                nucleotides=nucleotides+1
            elif nuc=="T":
                T_count=T_count+1
                nucleotides=nucleotides+1
            elif nuc=="G":
                G_count=G_count+1
                nucleotides=nucleotides+1
            elif nuc=="C":
                C_count=C_count+1
                nucleotides=nucleotides+1
            else:
                print "probably some new line character"

print A_count
print T_count
print G_count
print C_count
print nucleotides

###calculate GC content
GC= (G_count+C_count)/nucleotides
print GC ###produces unexpected results

GC= (G_count+C_count)/float(nucleotides)
print GC ###produces unexpected results


       