class WordDictionary:

    def __init__(self):
        self.wordDic = []

    def addWord(self, word: str) -> None:
        self.wordDic.append(word)

    def search(self, word: str) -> bool:
        for i in self.wordDic:
            if re.fullmatch(word,i):
                return True
        return False