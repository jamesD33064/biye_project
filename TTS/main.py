import pyttsx3

def TexttoSppech(content):
    engine = pyttsx3.init()
    engine.say(content)
    # engine.save_to_file(content, 'speech.wav')
    engine.runAndWait()

if __name__=="__main__":

    with open("./content.txt", 'r', encoding='utf-8') as fp:
        content = fp.read()
        print(content)
        TexttoSppech(content)