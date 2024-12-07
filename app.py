from flask import Flask, Response , jsonify
import os
from flask_cors import CORS 

app = Flask(__name__)

CORS(app)

application = app

out_dir = r'website/DataSet/Output/-'
video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
video_links = {}
mp4 = [mp4 for mp4 in os.listdir(out_dir) if mp4.endswith(video_extensions)]

for links in mp4:
    video_links[links.replace('.mp4' , ' ')] = os.path.join(out_dir, links)


@app.route('/')
def home():
    return jsonify(video_links)



@app.route('/<path:file_path>')
def render(file_path):

    try:
        def generate(video_path):
            with open(video_path, 'rb') as f:
                while True:
                    chunk = f.read(1024 * 1024)
                    if not chunk:
                        break
                    yield chunk

        return Response(generate(file_path), mimetype='video/mp4')
    
    except Exception as e:
        return f"an Error Occurred : {e}"


if __name__ == '__main__':
    app.run()
