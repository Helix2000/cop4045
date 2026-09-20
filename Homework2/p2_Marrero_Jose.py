# Name: Jose Marrero
# Z number: Z23816617

# Step A
tuple_list = [(a, b, c, d)
for a in range(1, 11)
    for b in range(1, 11)
        if b != a 
        for c in range(1, 11)
            if c != a and c != b
                 
            for d in range(1, 11)
                if d != a and d != b and d != c
                     
                if a**2 + b**2 == c**2 + d**2
                ]
print(f"Tuples found: {len(tuple_list)}")
for t in tuple_list:
    print(t)

# Step B
string_list = ['One', 'SEVEN', 'three', 'two', 'Ten']
string_list = [ (word.lower(), len(word))
    for word in string_list
        if len(word) < 5
    
]

print(f"String: {len(string_list)}")
for word in string_list:
    print(word)

# Step C
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
names = [name.split()[0] + " " + name.split()[1][0] + ". " + name.split()[2] 
    for name in names

]

print(names)

# Step D
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

anagram_pairs = [(word_1, word_2)
    for word_1 in lst1 
    for word_2 in lst2
    
    if sorted(word_1.lower()) == sorted(word_2.lower())
]

print(anagram_pairs)

# Step E
s = ['one', 'two', 'three']

dict1 = {
    word: len(word)
    for word in s
}

print(dict1)

# Step F
text = "Hello World"
vowel_dict = {
    i: character
    for i, character in enumerate(text)
    if character.lower() in "aeiou"
}
print(vowel_dict)