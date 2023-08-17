# GETTING STARTED WITH FLASK
# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello World"
#
#
# if __name__ == '__main__':
#     app.run()


# PYTHON DECORATORS - Helps us add extra functionalities to function without changing the actual function code.
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         function()
#         time.sleep(2)
#         function()
#         time.sleep(2)
#         print("Executed")
#     return wrapper_function
#
#
# @delay_decorator
# def print_hello():
#     print("Hello World")
#
#
# print_hello()
