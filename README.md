# French:English Flashcard App
Flashcard Game to practice French

```
Note: I am aware this project could use considerable refactoring to make it more robust, implement OOP, etc. 
This was a training exercise uploaded as-is.
I am currently focused on exploring new concepts rather than perfecting what currently exists. 
```

## How it Works

The game initializes by reading in the words_to_learn.csv file
* there is a line in main.py to reset the word list
* if the words_to_learn.csv file is missing, it will generate a fresh file from french_words.csv

You have 3 seconds to think of the translation before the card flips over

If you had the right translation, select the Checkmark icon to remove it from the flashcard stack

If you did not know the word, select the Red X icon to keep the card in the stack and try it again


Have fun!
