# Password_Generator-

Certainly! Here’s a concise description for the code:

This script generates a strong and random password consisting of 2 lowercase letters, 2 uppercase letters, 2 digits, and 2 symbols. It then shuffles these characters to ensure a randomized order and prints the resulting password.

This Python script generates a strong, randomized password by selecting specific characters from different character sets. It performs the following steps:

Generate Characters:

Two random lowercase letters are selected from 'a' to 'z'.
Two random uppercase letters are selected from 'A' to 'Z'.
Two random digits are selected from '0' to '9'.
Two random symbols are selected from the ASCII range 33 to 47 (common special characters).

Concatenate and Shuffle:
The selected characters are concatenated into a single string.
This string is then converted into a list of characters and shuffled to ensure randomness.

Output:
The shuffled list of characters is joined back into a string and printed as the final password.

This approach ensures that the password includes a balanced mix of character types, enhancing its strength and security.
