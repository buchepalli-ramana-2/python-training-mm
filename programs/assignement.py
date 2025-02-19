colors = [{
"colors": "red",
"values": "#f00"
},
{
"colors": "green",
"values": "#0f0"
},
{
"colors": "blue",
"values": "#00f"
},
{
"colors": "cyan",
"values": "#0ff"
},
{
"colors": "magenta",
"values": "#f0f"
},
{
"colors": "yellow",
"values": "#ff0"
},
{
"colors": "black",
"values": "#000"
}
]

'''
write a program to display all the colors and its values.

sample output :

red #f00
green #0f0
yellow  #ff0
magenta #f0f
'''
for item in colors:
    print(item['colors'], item['values'])

