class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer_value = 0
        roman_to_letters_list = [
            *s,
        ]
        for i in range(len(roman_to_letters_list)):
            if i < len(roman_to_letters_list) - 1:
                if (
                    roman_to_int[roman_to_letters_list[i]]
                    < roman_to_int[roman_to_letters_list[i + 1]]
                ):
                    integer_value -= roman_to_int[roman_to_letters_list[i]]
                else:
                    integer_value += roman_to_int[roman_to_letters_list[i]]
            else:
                integer_value += roman_to_int[roman_to_letters_list[i]]

        return integer_value


print(Solution.romanToInt("MCMXCIV"))
