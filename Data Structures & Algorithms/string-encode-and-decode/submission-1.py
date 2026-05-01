class Solution:

    def encode(self, strs: List[str]) -> str:
        # Strategy: precede each string with its length
        # We need a separater character to handle lengths > 9!
        result = []
        for s in strs:
            result.extend([str(len(s)), '#', s])
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = []
            while s[i] != '#':
                length.append(s[i])
                i += 1
            # Now push past the '#' char    
            i += 1
            
            s_length = int(''.join(length))
            result.append(s[i:i + s_length])
            i += s_length

        return result
