## Mastermind Game

The Mastermind game is a classic code-breaking game where the player tries to guess a secret code consisting of 4 numbers between 0 and 7. The game provides feedback on the player's guesses, indicating the number of correct numbers and their correct locations.

### How to Run the Game

To run the Mastermind game, follow these steps:

1. Ensure you have Python installed on your system. This code was developed and tested using Python 3.9, but should work with other versions as well.
2. Ensure requests library is installed by running `pip install requests`
3. Clone the repository or download the source code files:
   - `mastermind.py`: The main game file containing the logic for playing Mastermind.
   - `test_mastermind.py`: A test file to verify the `check_guess` function.
   - `test_hint.py`: A test file to verify the `provide_hint` function from the `hints_extension.py` file.
   - `hints_extension.py`: A file containing the implementation of the `provide_hint` function.
4. Open a terminal or command prompt and navigate to the directory containing the downloaded files.
5. Run the `mastermind.py` file using the following command:
   `python mastermind.py`
6. This will start the Mastermind game, and you can begin playing.

### How to Play the game

The game will present you with the following instructions:

1. The secret code consists of a combination of 4 numbers from 0 to 7.
2. You need to guess the secret code within 10 attempts.
3. After each guess, you will receive feedback on the number of correct numbers and their correct locations.
4. After your first attempt, you can request a hint by typing "yes" when prompted(case sensitive).
5. After your second attempt, you can view the previous guesses and their feedback by typing "yes" when prompted(case sensitive).
6. The game will continue until you successfully guess the secret code or run out of attempts (10). If you run out of attempts, the game will reveal the secret code.
7. After the end of the game you will have an option to play again. If "yes" is selected, the game will restart(case sensitive).

![Command Line Interface](images/commandlineUI.PNG)

## Mindset and Thought Process

1. **Understanding the Game Mechanics:**

   - Thoroughly understand the rules and gameplay of the Mastermind game.
   - Identify key components such as generating the secret code, handling player guesses, providing feedback, and determining win/loss conditions.

2. **Identifying Core Functionality:**

   - Generate a random secret code.
   - Validate player guesses.
   - Check the player's guess against the secret code.
   - Provide feedback to the player based on the guess.
   - Track the game progress and determine the outcome.

3. **Designing the Structure:**

   - Design the overall structure of the application.
   - Create separate functions to handle various aspects of the game.
     - `generate_secret_code()`: Generate the secret code.
     - `get_valid_guess()`: Handle user input and validate the guess.
     - `check_guess()`: Compare the player's guess with the secret code.
     - `play_mastermind()`: Orchestrate the game flow.

4. **Crafting game mechanics**

   - The central goal was to craft code that seamlessly integrated to deliver a smooth and captivating gameplay experience. This journey commenced with a deep dive into the game's rules and mechanics, laying the groundwork for adopting a modular design paradigm. Fragmenting the game's functionalities into discrete modules—such as secret code generation, player guess management, and feedback provision—was aimed at bolstering maintainability, streamlining testing procedures, and paving the way for effortless future upgrades.

   - Throughout the implementation phase, challenges were encountered, particularly in accurately interpreting player guesses and furnishing pertinent feedback. Confronted with these obstacles, a solution-oriented approach was adopted, employing exhaustive testing and debugging methodologies. By meticulously scrutinizing the codebase, utilizing strategic print statements, and conducting thorough data analysis, discrepancies were pinpointed and swiftly addressed. This iterative process empowered the refinement of the game's core logic, ensuring its robustness and seamless operation.

   - Concurrently, the implementation of error handling and input validation mechanisms played a pivotal role in fostering a user-friendly environment. By preemptively identifying and addressing potential pitfalls, such as erroneous inputs, the aim was to furnish users with lucid guidance and mitigate disruptions to their gaming journey. This proactive stance not only enriched the user interface but also instilled a sense of assurance and accessibility for players.

### Creative Extensions

- **Hints**:

  - The game allows the player to request a hint after the first attempt.
  - Hints are generated based on the player's previous guesses and feedback.
  - The hints provide information about the numbers in the secret code and their positions.

- **Previous Guesses and Feedback**:
  - After the second attempt, the player can choose to view their previous guesses and the corresponding feedback.
  - This feature helps the player keep track of their progress and identify patterns in the secret code.

### Future Additions (Creative Extensions)

- **Configurable Difficulty Level**:

  - Allow players to adjust the difficulty level of the game.
  - Adjust the number of numbers used in the secret code based on the selected difficulty.

- **Multi-player Extension**:

  - Extend the game to support multi-player mode.
  - Players can take turns guessing the secret code or compete against each other.

- **Score Tracking**:

  - Implement a scoring system to track players' performance across multiple games.
  - Scores can be based on factors like number of attempts, time taken, and difficulty level.

- **Timer Feature**:
  - Add a timer for the entire game session.
  - Optionally, include a timer for each guess attempt to increase the challenge.
