List= input("Please input a List of words to checked : ")
lenght = 0
for words in List.split():
           if len(words) > lenght:
                  lenght = len(words)
print ("The lenght of longest word is",lenght)
