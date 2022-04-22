word=input("Enter the word:")
def word_count(word):
  vowel= 0
  consonant=0
  for j in word:
      if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
        vowel=vowel+1
      else:
        consonant=consonant+1
  print("Number of vowels in the word:",vowel)
  print("Number of consonants in the word:",consonant)
word_count(word)
