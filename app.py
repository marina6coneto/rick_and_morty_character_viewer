from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route('/')
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character'
    response = urllib.request.urlopen(url)
    data = response.read()
    character_data = json.loads(data)  
    
    return render_template("characters.html", characters=character_data['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'  
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        profile_data = json.loads(data)
    except Exception as e:
        return f"Error fetching character profile: {e}"
    
    return render_template("profile.html", profile=profile_data)

@app.route('/lista')
def get_list_characters():
    url = 'https://rickandmortyapi.com/api/character'
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data) 
    
    characters_list = []
    
    for character in data_dict['results']:
        character_data = {
            'name': character['name'],
            'status': character['status'],
        }
        characters_list.append(character_data)
        
    return {'characters': characters_list}

