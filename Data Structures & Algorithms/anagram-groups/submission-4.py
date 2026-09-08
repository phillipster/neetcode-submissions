class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {};
        for word in strs:
            counts = [0] * 26;
            for letter in word:
                counts[ord(letter)-ord('a')] += 1;
            if tuple(counts) not in result:
                result[tuple(counts)] = [word];
            else:
                result[tuple(counts)].append(word);
        return list(result.values())
        