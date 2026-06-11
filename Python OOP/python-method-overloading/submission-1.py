class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str, text2: str = None) -> str:
        # Check "if text2 is None" instead of just "if text2" because of the empty string edge case. 
        if text2 is None:
            return text1.upper()
        return text1 + text2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
