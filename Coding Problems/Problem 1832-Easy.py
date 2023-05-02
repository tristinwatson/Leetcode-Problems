class Solution(ojbect):
    def checkIfPangram(self, sentence):
        string = "abcdefghijklmnopqrstuvwxyz"
        i = 0

        while i < len(string):
            if string[i] not in sentence:
                return False
            
            i += 1
        
        return True