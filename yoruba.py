from struct import pack_into

Yoruba_dictionary={"wa":'come',
                   "Olorun":'God',
                    "eshe":'thank u',
                    "ori":'head',
                    "owo":'money',
                    "aja":'Dog',
                    "oju":'eye',
                    "abo":'plate',
                    "ewa":'Beans',
                    "oba":'King',
                    "ete":'lip',
                    "eru":'load',
                    "aya":'wife',
                    "ata":'pepper',
                    "ara":'body',
                    "obo":'monkey',
                    "ilu":'drum',
                    "isu":'yam',
                    "ekun":'tears',
                    "okan":'heart'}
from tkinter import Tk,Entry,Button,Label,StringVar

window=Tk()
window.geometry("600x250")
window.title("Yoruba_dictionary")

word: StringVar = StringVar()
word_entry = Entry(window, textvariable=word, font=('ariel',19))
word_entry.pack()


result = StringVar()
result_label =Label(window , textvariable=result)
result_label.pack()


def search (word):
    if word in Yoruba_dictionary:
            result.set(Yoruba_dictionary[word])
            print(Yoruba_dictionary[word])
    else:
            result.set("not found")

search_btn = Button(window, text="search", command=lambda: search(word.get()))
search_btn.pack()


exit_button=Button(window, text="exit",command=lambda: exit())

word_entry =Entry(window, textvariable=word, font=('ariel',19))
window.mainloop()

