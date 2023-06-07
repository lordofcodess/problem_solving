class Solution:
    def interpret(self, command: str) -> str:
        interpretation = {"G": "G", "()": "o", "(al)": "al"}
        result = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                result += interpretation["G"]
                i += 1
            elif command[i:i+2] == "()":
                result += interpretation["()"]
                i += 2
            elif command[i:i+4] == "(al)":
                result += interpretation["(al)"]
                i += 4
        return result
