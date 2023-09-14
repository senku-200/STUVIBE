import requests

api_key = 'AIzaSyBDyduzRDf1owqO6ylT0KVR90-PSeFVaAI'
query = 'greyman'

url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

response = requests.get(url)
data = response.json()
for item in data['items']:
    volume_info = item['volumeInfo']
    print(volume_info)
    # print(f"Title: {volume_info['title']}")
    # print(f"Author(s): {', '.join(volume_info.get('authors', []))}")
    # print(f"Description: {volume_info.get('description', 'N/A')}")
    print()
