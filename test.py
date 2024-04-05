import requests

url = 'http://127.0.0.1:5000/predict'
image_url = 'https://media.istockphoto.com/id/1443328418/photo/tabby-cat-closeup-portrait.jpg?s=1024x1024&w=is&k=20&c=YLswAUjNHz34ZNHajbhuiRfCQen4y47-5oS13dbvdsQ='
candidate_labels = ['cat', 'dog']

# Send the image URL and candidate labels in the POST request
data = {'image_url': image_url, 'candidate_labels': ','.join(candidate_labels)}
response = requests.post(url, data=data)

print(response.json())