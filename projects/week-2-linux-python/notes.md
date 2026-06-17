1. What's the difference between absolute and relative paths?
    - Absolute Path: Always starts from the root directory (represented by a forward slash /). It is the complete, unabridged address to a file or folder, no matter where you are currently working in the system.
    - Starts from your current working directory (where you are "standing" right now). It uses shortcuts like . (current folder) or .. (parent folder) to navigate from your present location.
2. What does ~ mean?
    - A shortcut that represents the current user's home directory
3. What are the three permission levels?
    - User (u): The owner of the file or directory (usually the person who created it).
    - Group (g): A collection of users who share the same access permissions to that file.
    - Others (o): Everyone else on the system who is not the owner and not in the group (often referred to as "the world").
4. What does the | (pipe) do?
    - The pipe operator (|) takes the standard output (stdout) of one command and feeds it directly as the standard input (stdin) to the next command.

## Lesson 2 — Python Done Right

1. What is pyenv and why do I need multiple Python versions?
    - pyenv lets me use which Python version I need per project and that is exactly the reason why I need mutiple versions of Python to satisfy project requirements.
2. What is a virtual environment? Why does each project get one?
    - It acts as a Python isolator. It lets install a specific version of Python to satify projects requirements that will not affect other projects.
3. What does `source venv/bin/activate` actually do to my shell?
    - It activiated the venv I created
4. Why does `venv/` go in `.gitignore`?
    - venv/ contains thousands of files that are useless to track
5.  Bonus: what's the difference between `pyenv` (version manager) and `venv` (per-project bubble)?
    - pyenv lets me download and navigate different versions of Pyhthon while venv is the virtual environment that will contain one specific version of python for project requirements