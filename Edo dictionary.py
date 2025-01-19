from struct import pack_into

Edo_dictionary ={"la re":  'come',
                  "oba":  'king',
                  "koyo":  'hello',
                  "Igho":  'money',
                  "edi ebo": 'pineapple',
                  "iye": 'mother',
                  "ara":'father',
                  "omo":  'child',
                  "aga": 'chair',
                  "uwese":  'thank you',
                  "osa lob wa": 'God hear',
                  "ito han": 'mercy',
                  "uwa":  'prosperity',
                  "efua":  'sunshine',
                  "igo" :  'money',
                  "efosa": 'God blessing',
                  "osaje":   'God sent',
                  "osarenmen":   'Ayewhosa',
                  'God gift':  'who is like God'}

from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("Edo_dictionary")

word: StringVar = StringVar()
word_entry =Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()

result = StringVar()
result_label =Label(window, textvariable=result)
result_label.pack()

def search(word):
    if word in Edo_dictionary:
        result.set(Edo_dictionary[word])
        print(Edo_dictionary[word])
    else:
          result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()

exit_button = Button(window, text="search", command=lambda: exit())

word_entry = Entry(window, textvariable=word, font=('ariel',19))

