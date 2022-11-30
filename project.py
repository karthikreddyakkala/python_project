def acr(self):
    oupt = self[0]

    for i in range(1, len(self)):
        if self[i-1] == ' ':
            oupt += self[i]
   
    oupt = oupt.upper()
    return oupt

x = input("Enter the word: ")
print(acr(x))

