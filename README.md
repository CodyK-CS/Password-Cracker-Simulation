# Password Security Tester

A Python cybersecurity project that simulates how quickly a password's characters can be identified by searching through a predefined character dictionary.

## What It Does

The program takes a password entered by the user and searches through a dictionary containing:

* Lowercase letters
* Uppercase letters
* Numbers
* Common keyboard symbols

It records how long the process takes and uses the elapsed time to give the password a basic security rating.

## How It Works

1. The user enters a password.
2. The program checks each character against the character dictionary.
3. When a matching character is found, it is added to the discovered password.
4. The program measures how long the process takes.
5. A basic security rating is displayed based on the elapsed time.

## Features

* Character searching simulation
* Uppercase and lowercase character support
* Numbers and common symbols
* Execution time measurement
* Basic password security rating
* Runs entirely locally
* No external libraries required

## How to Run

Make sure Python is installed, then run:

```bash
python passwordSecurityTester.py
```

Enter a password when prompted.

Type `q` to quit the program.

## Example

```text
Enter a password (or type q to quit): Test123!

Password Security: Moderate
The password is: Test123!
```

## Limitations

This project is an educational simulation and does **not** perform a real brute-force attack.

The current program searches for each character individually rather than attempting every possible combination of characters.

The security rating is also based on the program's execution time and should not be treated as a real-world password strength measurement.

## What I Learned

This project helped me practice:

* Python loops
* Lists
* Functions
* Conditional statements
* User input
* Measuring execution time
* Basic cybersecurity concepts
* Debugging and improving existing code

## Technologies

* Python
* Git
* GitHub

## License

This project is licensed under the MIT License.
