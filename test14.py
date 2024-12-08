def save_as_text(ascii_art):
    with open("test.bat", "w") as file:
        for line in ascii_art:
            file.write("curl ascii.live/rick")
        file.close()