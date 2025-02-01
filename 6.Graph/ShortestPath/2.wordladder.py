# https://leetcode.com/problems/word-ladder/description/
# https://leetcode.com/problems/word-ladder-ii/description/


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        # USING BFS - q(word,level)
        q = deque()
        q.append((beginWord,1))
        wordList = set(wordList)  #- imp use set to find word in o(1)
        while q:
            word,level  = q.popleft()  #2- use popleft and not pop

            if word == endWord:  #3. no need to continue if get the ans , as further lvel wil inc
                return level 

            # hit - loop 3 times - len of word
            # Try all possible one-letter transformations
            for i in range(len(word)): 
                for ch in string.ascii_lowercase:  # 'a' to 'z'
                    newWord = word[:i] + ch + word[i + 1:]  # Replace character at index i

                    if newWord in wordList:
                        q.append((newWord,level+1))
                        wordList.remove(newWord)  #- so that dont go back to same word like hot to hit
                    
        return 0


                        

        
