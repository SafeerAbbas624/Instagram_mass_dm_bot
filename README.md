# Instagram Direct Message Bot

## Introduction
This is a Python script that uses Selenium to automate sending direct messages on Instagram. The script reads a list of usernames from a file and sends a pre-defined message to each user.

## Features
- Automates sending direct messages on Instagram
- Reads a list of usernames from a file
- Sends a pre-defined message to each user
- Handles pop-ups and login process

## Installation for All OS

### Windows
1. Install Python from the official website: Python Downloads
2. Install Selenium using pip:
    ```sh
    pip install selenium
    ```
3. Install chromedriver_binary using pip:
    ```sh
    pip install chromedriver_binary
    ```
4. Download the ChromeDriver executable from the official website: ChromeDriver Downloads
5. Add the ChromeDriver executable to your system's PATH environment variable

### macOS (using Homebrew)
1. Install Python using Homebrew:
    ```sh
    brew install python
    ```
2. Install Selenium using pip:
    ```sh
    pip install selenium
    ```
3. Install chromedriver_binary using pip:
    ```sh
    pip install chromedriver_binary
    ```
4. Install ChromeDriver using Homebrew:
    ```sh
    brew install chromedriver
    ```
5. Add the ChromeDriver executable to your system's PATH environment variable

### Linux (using apt-get)
1. Install Python using apt-get:
    ```sh
    sudo apt-get install python3
    ```
2. Install Selenium using pip:
    ```sh
    pip install selenium
    ```
3. Install chromedriver_binary using pip:
    ```sh
    pip install chromedriver_binary
    ```
4. Install ChromeDriver using apt-get:
    ```sh
    sudo apt-get install chromedriver
    ```
5. Add the ChromeDriver executable to your system's PATH environment variable

## Usage
1. Create a file named `usernames.txt` containing the list of usernames to send messages to, one username per line. example included.
2. Create a file named `messages.txt` containing the message to be sent, or hardcode the message in the script. example included.
3. Run the script using Python:
    ```sh
    python script.py
    ```
4. The script will login to Instagram using the provided credentials, send messages to each user in the list, and quit the browser.

## Thanks Note
Thank you for using this script! Please note that this script is for educational purposes only and should not be used for spamming or other malicious activities. Also, be aware of Instagram's terms of service and usage policies.
