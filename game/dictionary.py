"""import unicodedata

class Dictionary:
    def search_word(file_path, word):
        word_no_accent = unicodedata.normalize ('NFKD', word).encode ('ascii', 'ignore').decode ('utf-8', 'ignore')
        with open(file_path, 'r') as file:
            content = file.read()
            if word in content:
                print('existe')
            else:
                print('no existe')
    search_word(r'/home/celi/Computacion/scrabble/game/WordlistSpanish.txt', word_no_accent)"""


##NO FUNCIONA