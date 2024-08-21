import requests

def search_artist(artist_name):
    url = 'https://api.deezer.com/search/artist'
    params = {'q': artist_name}
    response = requests.get(url, params=params)
    data = response.json()
    
    # Print the full response for debugging
    print("Search Response Data:", data)
    
    if 'data' in data and len(data['data']) > 0:
        artist = data['data'][0]
        return artist['id']
    return None

def get_similar_artists(artist_id):
    url = f'https://api.deezer.com/artist/{artist_id}/related'
    response = requests.get(url)
    data = response.json()
    
    # Print the full response for debugging
    print("Similar Artists Response Data:", data)
    
    if 'data' in data:
        similar_artists = [artist['name'] for artist in data['data']]
        return similar_artists
    return ['No similar artists found or error occurred.']

artist_name = input("Enter an artist name (e.g., BTS): ")
artist_id = search_artist(artist_name)
if artist_id:
    recommendations = get_similar_artists(artist_id)
    print(f"Similar artists to {artist_name}: {recommendations}")
else:
    print("Artist not found.")
