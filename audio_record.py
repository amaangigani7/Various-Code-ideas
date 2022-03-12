# for recording on this PC

import pyttsx3
engine = pyttsx3.init()
text = "My name is Amaan"
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# engine.say(text)
# engine = pyttsx3.init()
engine.setProperty('rate', 160)
my_text = ''
with open('F:\\lightnovel_on_device\\titles.txt', encoding='utf8') as file:
    for line in file:
        my_text += line

print('started')
name = '52_53_54'
engine.save_to_file(my_text, 'F:\\lightnovel_on_device\\Audio\\C{}.mp3'.format(name))
engine.runAndWait()
print('saved as {}'.format(name))
#
# engine.runAndWait()
# v = engine.getProperty('voices')
# for voice in v:
#     print(voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say(text)
#     engine.runAndWait()

# to get the info. about various voices in our PC
    # print("ID: %s" % voice.id)
    # print("gender: %s" %voice.gender)
    # print("Name: %s" %voice.name)
    # print("Age: %s" %voice.age)
    # print("Languages Known: %s" %voice.languages)

# import pyttsx3
#
# number = 'Chapter 42 - '
# title = 'Domino'
# name = number + title
# t = ''
#
# with open('F:\\lightnovel\\titles.txt', 'r') as f:
#     for line in f:
        # if title == line:
        #     print('title already exists!')
        #     break
    # else:
        # x = title + '\n'
        # with open('F:\\lightnovel\\titles.txt', 'a') as j:
        #     j.writelines(x)
        # with open('F:\\lightnovel\\TXT\\{}.txt'.format(name), 'r', encoding="utf8") as e:
        #     for line in e:
        #         t = t + line + '\n'
        # with open('F:\\lightnovel\\TXT\\{}.txt'.format(name), 'w', encoding="utf8") as edit:
        #     edit.write(t)
        #
        # print('else...')


# for playing audio on any system with speakers
# import pygame
# file = 'F:\\udemy.django\\website\\my_web\\personal_web\\mysite\\my_app\\media\\audio\\{}.wav'.format('bigger text')
# pygame.mixer.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# x = pygame.mixer.music.get_volume()
# print(x)
#
# while pygame.mixer.music.get_busy():
#     print(pygame.mixer.music.get_pos())
#     control = input()
#
#     if control == "pause":
#         pygame.mixer.music.pause()
#         print(pygame.mixer.music.get_pos())
#     elif control == "play":
#         pygame.mixer.music.unpause()
#         print(pygame.mixer.music.get_pos())
#     elif control == "stop":
#         pygame.mixer.music.stop()
#     elif control == "+":
#         x = pygame.mixer.music.get_volume()
#         pygame.mixer.music.set_volume(x - 0.5)
#         print(pygame.mixer.music.get_volume())
#     else:
#         pass

# TTS using the gtts
# from gtts import gTTS
# tts = gTTS('hello')
# tts.save('hello.mp3')
# x = gTTS('Aarav', lang='en-us', slow=False)
# x.save('f.mp3')

# from gtts import gTTS
# my_text = ''
# with open('F:\\scripts\\EP.1 - Script Raymond Mark.txt', encoding='utf8') as file:
#     for line in file:
#         my_text += line
#
# my_obj = gTTS(text=my_text, lang='en-us', slow=False)
# my_obj.save("F:\\scripts\\EP.1 Raymond Mark.mp3")
