#https://www.codewars.com/kata/57efab9acba9daa4d1000b30

def bald(s):
    hair_names = {
        0: "Clean!",
        1: "Unicorn!",
        2: "Homer!",
        3: "Careless!",
        4: "Careless!",
        5: "Careless!",
    }
    return [s.replace("/","-"),"Hobo!"] if s.count("/") > 5 else [s.replace("/","-"), hair_names[s.count("/")]]

def bald(s):
    print(s)
    c = len([el for el in s if el =="/"])
#     c = s.count("/")
    l = ["Clean!", "Unicorn!", "Homer!", "Careless!",  "Careless!",  "Careless!"]
    return [s.replace('/', '-'), l[c] if c <=5 else "Hobo!"]

# tests = (
#     (["----------", "Unicorn!"], "/---------"),
#     (["--------", "Homer!"], "/-----/-"),
#     (["---------------", "Careless!"], "--/--/---/-/---"),
# )