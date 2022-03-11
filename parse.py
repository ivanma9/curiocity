tag_definitions = open('tagdefinitions.txt', 'r')

tag_list = tag_definitions.readlines() #list of all the tags 

titles = {'active':'Active Life','beaches' :'Beaches'} 

for tag in tag_list:

    #skip the line if it doesn't contain a tag
    if tag == "\n" or tag[0] == "*" or tag[0] ==" ":
        continue

    title = ""
    i = 0

    #read in characters and add to title until there is a " ("
    while True:
        if tag[i] == " ":
            if tag[i+1] == "(":
                i+=2
                break
        title += tag[i]
        i+=1

    alias = ""

    #read in characters and to alias until there is a ","
    while tag[i] != ',':
        alias += tag[i]
        i+=1
    
    #create a new entry in myDict with key alias and value title 
    titles[alias] = title

titles['food'] = 'Restaurants'
