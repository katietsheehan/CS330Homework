"""Lab 3: Regexes and reformatting."""

# Katie Sheehan

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

import re

for contact in contacts:
    contact = re.split(",",contact) #split contact in parts
    name = re.split(" ",contact[0]) #split name into parts
    #rearrage name 
    if len(name) == 3:
        temp = name[0]
        name[0] = name[2]
        name[2] = name[1]
        name[1] = temp
    else:
        temp = name[0]
        name[0] = name[1]
        name[1] = temp
    name = ", ".join(name) 
    contact[0] = name
    
    temp = contact[1]
    contact[1] = contact[2] #Swap places
    
    number = re.findall("\d+",temp)
    if len(number) == 4: #remove "1" from phone numbers
        del number[0]
    if len(number) == 2: #split ending 7 digits
        pattern = re.findall("\d{1}", number[1])
        middle_three = pattern[0] + pattern[1] + pattern[2]
        last_digits = pattern[3] + pattern[4] + pattern[5] + pattern[6]
        number[1] = middle_three + " " + last_digits

    #area code   
    number[0] = re.sub("^", "(", number[0])
    number[0] = re.sub("$", ")", number[0])
    number = " ".join(number)
    contact[2] = number

    contact = "\n".join(contact)
    print(contact +"\n")
        
    

