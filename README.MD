# NeroTask

NeroTask is a task management application developed by Salhi Abdennour/CHR0N1.

## Features

- User Authentication:
  - Sign up with a unique username and password
  - Log in with existing credentials
  - Log out functionality

- Task Management:
  - Create new tasks with title, description, and importance level
  - List all tasks
  - Sort tasks by importance
  - Edit existing tasks
  - Delete individual tasks
  - Delete all tasks

- User Interface:
  - Command-line interface with colorful output
  - Clear screen functionality
  - Help command to display available options

## Detailed Documentation

### Installation

NeroTask is a Python application. Ensure you have Python installed on your system.

### Usage

Run the `main.py` file to start the application:

### Commands

- `help`: Displays a list of all available commands and their explanations.
- `exit`: Exit the NeroTask app.
- `logout`: Logs you out of the app.
- `list`: Displays all of your current ToDos.
- `list--sort`: Displays all of your current ToDos sorted by importance.
- `delete`: Prompts you to select a ToDo to delete.
- `delete--all`: Delete all ToDos.
- `create`: Allows you to create a new ToDo and add it to your list.
- `clear`: Clear screen buffer.
- `edit`: Allows you to edit your ToDo.

### Task Structure

Each task (ToDo) consists of:
- Title (unique)
- Task description
- Date (automatically set to creation time)
- Importance (integer value between 1 and 5)

### File Structure

- `main.py`: Main application file
- `regestredUsers.py`: Contains User class definition
- `package_info.py`: Contains package information
- `users.dat`: Binary file storing user data

### Security

- Passwords are hashed before storage
- User authentication is required to access tasks

## License

Licensed under the Apache License, Version 2.0. See the LICENSE file for details.

## Additional Information

### Dependencies
- colorama: Used for colored console output

### Data Storage
User information and tasks are stored in a binary file named `users.dat`.

### Version
Current version: 0.1.0

### Note
This application is a command-line interface (CLI) tool and does not have a graphical user interface (GUI).

## Contact

Author: Salhi Abdennour
Email: abdennoursalhi@yandex.com
GitHub: https://github.com/Salhi-Abdennour/NeroTask
itchio: https://chrony.itch.io/
carrd: https://wh01m1.carrd.co/
twitter: https://x.com/CHR0N1_101
