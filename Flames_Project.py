from collections import Counter
def play(a,b):
    print(f"Playing with names {a} and {b} ")
    count_a=Counter(a)
    count_b=Counter(b)  
    
    for char in list(count_a.keys()):
        if char in count_b:
            min_count= min(count_a[char],count_b[char])     
            count_a[char] -= min_count                      
            count_b[char] -= min_count                     

            if count_a[char]==0:
                del count_a[char]

            if count_b[char]==0:
                del count_b[char]

    #print(count_a ,count_b,sep="\n")
    count_c=sum(count_a.values())+ sum(count_b.values()) 
    print(f"The Count is '{count_c}'")
    if (count_c > 1):
        game = ['f','l','a','m','e','s']        
        while len(game)>1:
            circular_index = (count_c-1) % len(game) # 7%6=1...
            #circular_index=1
            game.pop(circular_index) # game=[f,a,m,e,s]
            # slicing and reordering
            game=game[circular_index:] + game[:circular_index] #game=[ a,m,e,s,f]
            #game[0]='a'
        flames={
            "f":"Friend",
            "l":"Love",
            "a":"Affection",
            "e":"Enemy",
            "m":"Marraige",
            "s":"sibling"
            }
        print(F"the Flames is {flames.get(game[0])}" )
    else:
        print("Both Letters get canceled.")
   
    

def get_valid_name(prompt):
    while True:
        names=input(prompt).casefold().replace(" ","")
        if(names.isalpha()):
            return names
        print("Enter the Names only without any specific character or numeric value.")


Name_1=get_valid_name("Enter the 1st Name :")
Name_2=get_valid_name("Enter the 2nd name :")
play(Name_1,Name_2)

