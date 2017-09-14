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
fh = open("/Users/sumairazaman/Downloads/demo.fasta","r")
print fh.read()

#read one line at a time
fh = open("/Users/sumairazaman/Downloads/demo.fasta","r")
print fh.readline()
print fh.readline()
print fh.readline()

#read it as a list of lines
fh = open("/Users/sumairazaman/Downloads/demo.fasta","r")
print fh.readlines

#save the list of lines into a variable instead of printing it
fh = open("/Users/sumairazaman/Downloads/demo.fasta","r")
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



