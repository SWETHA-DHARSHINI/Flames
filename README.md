**FLAMES Compatibility Game**

Flame.py is a Python script that recreates the classic FLAMES game, a lighthearted way to explore the relationship dynamic between two names. FLAMES stands for Friend, Love, Affection, Marriage, Enemy, and Sibling, and the program calculates the relationship based on the characters in the given names.

**How It Works**
Enter two names when prompted by the program.
The script removes common characters from both names.
Based on the total count of remaining characters, the game calculates the result using the FLAMES logic:
F = Friend
L = Love
A = Affection
M = Marriage
E = Enemy
S = Sibling
The outcome gives a playful representation of the relationship between the two names.

**Features**
User-Friendly Input: Accepts names with spaces and mixed case.
Error Handling: Ensures only alphabetic input is processed.
Dynamic Calculation: Uses modular arithmetic for circular indexing.
Interactive Output: Displays the process and the final result clearly.

**Requirements**
Python 3.7 or later.

**Installation and Setup**
Clone the repository: git clone https://github.com/yourusername/FlameGame.git
Move into the project directory: cd FlameGame
Run the script: python Flame.py

**Example**
**Input:** 

	  Enter the 1st Name: Alice


       Enter the 2nd Name: Bob
       
**Output:** Remaining characters after removing common letters: 5


**FLAMES Result:** Marriage
