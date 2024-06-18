import json
def read_requestContent():
    file= open('C:\\Users\\Cloud Analogy\\Desktop\\request.json')
    jsonFile= file.read()
    jsonContent= json.loads(jsonFile)
    return jsonContent
x= read_requestContent()
print(x)