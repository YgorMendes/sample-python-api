from flask import Flask, request, jsonify
from models import MovieModel, UserModel
import os
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Conexão com dataBase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
client = create_client(url, key)

@app.route('/createMovie', methods=['POST'])
def create_movie():
  try:
      movie_data = MovieModel(**request.json)
      movie_dict = movie_data.model_dump()
      
      client.table("movies").insert(movie_dict).execute()

      return '', 201
  except Exception as e:
    return jsonify({"error": str(e)}), 400
  
@app.route('/createUser', methods=['POST'])
def create_user():
  try:
      user_data = UserModel(**request.json)
      user_dict = user_data.model_dump()

      client.table('users').insert(user_dict).execute();

      return '', 201
  except Exception as e:
    return jsonify({"error": str(e)}), 400
  
@app.route('/movies/<gender>', methods=['GET'])
def find_movies_by_gender(gender: str):
  try:
    response = client.table("movies").select('*').filter('gender', 'cs', f'{{"{gender}"}}').execute()

    return jsonify({"data": response.data}), 200
  except Exception as e:
    return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
