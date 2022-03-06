import requests

link = "https://raw.githubusercontent.com/N7K5/copy_and_paste/main/copy.txt"


def web_to_chars(url):
    f = requests.get(link)
    res= f.text
    chars= []
    for c in res:
        chars.append(c)
    return chars
       

if __name__ == "__main__":
    print(web_to_chars(link))