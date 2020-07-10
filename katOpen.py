import webbrowser

ID = input("Enter ID Here: ")

URL = 'https://open.kattis.com/problems/' + ID

webbrowser.open(URL, new=2)