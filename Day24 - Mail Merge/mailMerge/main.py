#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Day24/Mail Merge Project Start/Input/Names/invited_names.txt")
names = f.readlines()
f.close()

for nameofperson in names:
    new_name = nameofperson.strip()
    fin = open("Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt", "rt")
    fout = open(f"Day24/Mail Merge Project Start/Output/ReadyToSend/{nameofperson}.txt", "wt")
    for line in fin:
        fout.write(line.replace("[name]", new_name))
    fin.close()
    fout.close()