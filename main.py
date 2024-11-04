class Flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+ " = " +self.meaning 
flash=[]
print("Welcome to the flashcrad application")
while True:
    word=input("Enter the word you want to add to the flashcard : ")
    meaning=input("Enter the meaning of the word you want to add to the flashcard : ")
    flash.append(Flashcards(word,meaning))
    option=int(input("Enter 0 if you want to leave or 1 to add another flashcard : "))
    if option==0:
        break
for i in flash:
    print(i)
