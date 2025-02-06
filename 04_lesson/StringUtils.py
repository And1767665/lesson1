class StringUtils:
    @staticmethod
    def reverse_string(s: str) -> str:
        if s is None:
            return None
        words = s.split(" ")
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)

    @staticmethod
    def capitalize_string(s: str) -> str:
        if s is None:
            return None
        if s == "":
            return ""
        return s[0].upper() + s[1:]

    @staticmethod
    def join_strings(list_of_strings: list) -> str:
        if list_of_strings is None:
            return None
        return " ".join(list_of_strings)

    @staticmethod
    def is_palindrome(s: str) -> bool:
        if s is None:
            return False
        cleaned = ''.join(e for e in s if e.isalnum()).lower()
        return cleaned == cleaned[::-1]
