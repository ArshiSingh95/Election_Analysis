# create a filename variable to a direct or indirect path to the file 
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the same statement open the file as a text file
##using the with Statement to open file as a txt file
#Write in file
with open(file_to_save, "w") as txt_file: 
   #txt_file.write("Hello World :)")
    txt_file.write( "Araphoe\nDenver\nJefferson")
