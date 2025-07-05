s = input()

if s[:3] == "NXT" and (int(s[3:]) % 2 == 0 or int(s[3:]) % 7 == 0):
    print("Special String")
else:
    print("Not a Special String")