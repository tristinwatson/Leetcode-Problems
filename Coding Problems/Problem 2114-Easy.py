class Solution(object):
    def mostWordsFound(self, sentences):
        hi = 0
        for i in range(len(sentences)):
            sentence = sentences[i].split()
            if hi <= len(sentence):
                hi = len(sentence)
        
        return hi