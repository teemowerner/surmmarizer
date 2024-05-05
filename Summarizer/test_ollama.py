import ollama

file = open('myfile.txt', 'r')
# print(file.read())

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': file.read()+'Summarzie this into 5 sentences in 한국어, 꼭 한국말로 써 : ',
  },
])
print(response['message']['content'])

file = open('final.txt', 'w')
file.write(response['message']['content'])
# for i in response['message']['content']:
#     file.write(i)
#     file.write(' ')

file.close()