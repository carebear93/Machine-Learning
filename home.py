# About this program
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print "                                                                        @"
print "Thursday 1 Nov 2018 - University of Aberdeen                            @"
print "Created by (Bsc)Kristian Care                                           @"
print "Neural Network Source code used: iamtrask (2015) & Siraj Raval (2016)   @"
print "                                                                        @"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

print ""
print ""

# Select what to fire
X = raw_input ("Would you like execute this neural network? [Y/N] ")

print ""

#Check user input
if X == 'Y':
    execfile('nn.py')
else:
    #close program if user does not select a valid option
    print "Goodbye"
