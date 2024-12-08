from src.app import app

HOST = "localhost"
PORT = 4000
DEBUG = True

if __name__ == "__main__":
    app.run(HOST, PORT, DEBUG)

# is a common Python construct used to execute code only when the script is run directly, not when it is imported as a module.

# if __name__ == "__main__": This checks whether the Python file is being run as the main program. If the script is executed directly (for example, python script.py), the value of __name__ will be set to "__main__", and the main() function will be called.

# main(): This calls the main function, where the main logic of your script should reside.

# If your script is meant to be executed directly, the block ensures that main() is called only in 
# this case. If this script is imported into another Python script as a module, the main() function will not be called automatically.