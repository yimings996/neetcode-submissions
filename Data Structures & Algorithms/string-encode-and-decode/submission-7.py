class Solution:

    def encode(self, strs: List[str]) -> str:
        return "😂".join(strs) + ("😂" if strs else "")

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s[:-1].split("😂")
