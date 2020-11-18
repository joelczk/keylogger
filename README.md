# Keylogger

## Introduction
This project explores the use of a keylogger using `Python` as the main programming language, and how this keylogger can be utilised by a potential adversary, without the knowledge of his/her victim. This project is meant for educational purposes only.

## Requirements
1. Python 3.7

## Operating Systems
1. Ubuntu
2. Windows 10

## Use Case
1. Executable is able to run in the background without the user's knowledge
2. Executable is able to constantly log the keystrokes of the user
3. The keystrokes will be logged in a output file(`output.txt`)

## Running the code

```bash
$ pip install -r requirements.txt

$ python main.py

```

## Creating the executable 

```bash
$ pip install -r requirements.txt

$ pip install Pyinstaller

$ PyInstaller main.py --onefile --noconsole

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Disclaimer
This project is created for EDUCATIONAL purposes only. The owner will not be responsible for for any damages caused by the misuse of this project.

## License
[MIT](https://choosealicense.com/licenses/mit/)
