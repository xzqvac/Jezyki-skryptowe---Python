digits = {
    "zero": 0, "jeden": 1, "dwa": 2, "trzy": 3, "cztery": 4, "pięć": 5, "sześć": 6, "siedem": 7, "osiem": 8,
    "dziewięć": 9, "dziesięć": 10, "dwadzieścia": 20, "trzydzieści": 30, "czterdzieści": 40, "pięćdziesiąt": 50,
    "jedenaście": 11, "dwanaście": 12, "trzynaście": 13, "czternaście": 14, "piętnaście": 15, "szesnaście": 16,
    "siedemnaście": 17, "osiemnaście": 18, "dziewiętnaście": 19
}


def wordToNumber(firstWord, secondWord=None):
    numerOfSecondWord = 0
    numberOfFirstWord = (digits.get(firstWord))
    if secondWord:
        numerOfSecondWord = (digits.get(secondWord))
    print(numberOfFirstWord+numerOfSecondWord)

word = input()
splittedWords = word.split()
splittedWords.append(0)
wordToNumber(splittedWords[0], splittedWords[1])
#assert (firstWord in digits) and (secondWord in dig)