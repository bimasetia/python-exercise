import webbrowser

search = input("Input your google query:")
webbrowser.open('http://www.google.com/search?btnG=1&q=%s' % str(search), new=2)
