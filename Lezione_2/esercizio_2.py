names =["Michele" , "Chiara" , "Gennaro"]
print(names[0])

message = ("Ti va di cenare da me?")
print(f"{names[0]}, {message}\n{names[1]}, {message}\n{names[2]}, {message}")

car_list = ["Lamburghini" , "Ferrari" , "Pagani"]
print(f"La {car_list[1]} è superiore alla {car_list[0] }.")

print(f"{names[2]} non puo venire.")
names.pop(2) 
names.append("Gattuso")
print(f"{names[0]}, {message}\n{names[1]}, {message}\n{names[2]}, {message}")

names2 = ["Del piero" , "Ronaldo" , "Antonella"]
names.insert(0, "Mario")
names.insert(2, "Flavia")
print(names)
names.extend(names2)
print(names)
for name in names:
    print(f"{name} {message}")

print(f"{names[4]} non sei invitato")   
names.pop(4)
del names[4:]
print(names) 

