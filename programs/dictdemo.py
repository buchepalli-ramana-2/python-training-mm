book = {"chap1": 10,"chap2": 23, "chap3":24,"chap4":24}

#Display individual values
print(book['chap1'])
print(book['chap2'])

# display keys in dictionary
print(book.keys())
#display values in dictionary
print(book.values())

#display items as a list
print(book.items())

#removing element based on the key
book.pop('chap3')
print(book)

# book.update("chap2") = "27"

#Adding new element
book['chap3'] = "28"
print(book)

book1 = {"chap6":"24","chap7": "26"}
#print(book1["chap8"])

#Combining two dicts
newbook = {**book,**book1}

book.update(book1)
print(book)

print(book.get("chap8"))
print(book.get("chap1"))

data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(data.keys())
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])

#print XML
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][1])

#####################################################

book2 = {"context":0,"lesson1":2,"lession2":4}

#Display keys
for key in book2.keys():
    print(key)

#Display valuess
for val in book2.values():
    print(val)

#display values
for key,val in book2.items():
    print(key,val)

#validating the key
key = "lesson1"
if key in book2.keys():
    print(f"{key} is exists")
else:
    print(f"{key} is not exists")