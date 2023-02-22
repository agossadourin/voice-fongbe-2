from flask import Flask, jsonify, send_file, send_from_directory
from number_reader import prixReader
from number_reader import concatenate_audio_moviepy, denreeReader, marcheReader
import sys
import os
from pydub import AudioSegment
from os.path import exists
app = Flask(__name__)
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
print(os.path.join(dirname,'voix/tmp/output.wav'))

@app.route('/')
def index():
    return "Welcome to fongbe kwe api"


@app.route("/read/<int:number>/<string:denree>/<string:marche>", methods = ['GET'])
def readPrice(number, denree,marche):
    d = denreeReader(denree)
    price = prixReader(number)
    m = marcheReader(marche)
    e = d+m+price
    print(e)
    outpath = os.path.join(dirname,'voix\\tmp\\output.mp3')
    if exists(outpath):
        os.remove(outpath)
    concatenate_audio_moviepy(e, outpath)
    #a = AudioSegment.from_file(outpath)
    try:
        print('sucess')
        return send_file(outpath, as_attachment=False)
    except FileNotFoundError:
        print("file not found")


if __name__ == "__main__":
    app.run(debug=True)