import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url)
#print (response.json())


def readbooks():
    response = requests.get(url)
    return response.json()
    

def readbooks(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()
    
def createbook(book):
    response = requests.post(url, json=book)

    return response.json()

def updatebook(id, bookdiff):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=bookdiff)
    return response.json()
    pass



if __name__ == "__main__":
    book= {
        'author': 'xxx',
        'title': 'xxx',
        'price': 123 
        
    }
    bookdiff= {
        'price': 555
    }
    #print(readbooks())
    #print(readbooks(1552))
    #print(createbook(book))
    print(updatebook(55, bookdiff))