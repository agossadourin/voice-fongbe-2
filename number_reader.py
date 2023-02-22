# import required module
from pydub.effects import speedup
import os,sys
from pydub.playback import play
from pydub import AudioSegment
from playsound import playsound
import time
from moviepy.editor import concatenate_audioclips, AudioFileClip
import tempfile

i=1

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
def numberReader(nombre):
    quarantaine = int(nombre/40)
    dizaine = int((nombre - 40*quarantaine)/10)
    unites = int(nombre - 40*quarantaine - 10*dizaine)

    b = []
    if (quarantaine > 0):
        b.append(os.path.join(dirname,'voix/pref/q.wav'))
        if (quarantaine == 1):
            b.append(os.path.join(dirname,'voix/pref/v1mod.wav'))
        else:
            b.append(os.path.join(dirname,'voix/v'+str(quarantaine)+'.wav'))
    if (quarantaine > 0 and dizaine == 0 and unites > 0):
        b.append(os.path.join(dirname,'voix/v'+str(unites)+'.wav'))

    if (quarantaine == 0 and dizaine == 0 and unites > 0):
        b.append(os.path.join(dirname,'voix/v'+str(unites)+'.wav'))

    if (dizaine == 1):
        b.append(os.path.join(dirname,'voix/v10.wav'))
        if (unites > 0 and unites < 5):
            b.append(os.path.join(dirname,'voix/v' + str(unites) + '.wav'))
        elif (unites >= 5):
            b.remove(os.path.join(dirname,'voix/v10.wav'))
            b.append(os.path.join(dirname,'voix/v15.wav'))
            if (unites > 5):
                b.append(os.path.join(dirname,'voix/pref/n.wav'))
                b.append(os.path.join(dirname,'voix/v' + str(unites-5) + '.wav'))

    if (dizaine > 1):
        b.append(os.path.join(dirname,'voix/v'+str(dizaine)+'0.wav'))
        if (unites >= 5):
            b.append(os.path.join(dirname,'voix/v5.wav'))
            if (unites > 5):
                b.append(os.path.join(dirname,'voix/pref/n.wav'))
                b.append(os.path.join(dirname,'voix/v' +
                         str(unites-5) + '.wav'))
        elif (unites > 0 and unites < 5):
            b.append(os.path.join(dirname,'voix/pref/n.wav'))
            b.append(os.path.join(dirname,'voix/v' + str(unites) + '.wav'))

    return b


def prixReader(prix):

    #int(input("Entrez un montant: "))
    mille = int(prix/1000)
    vingtcinq = int((prix - mille*1000)/25)
    cinq = int((prix - mille*1000 - vingtcinq*25)/5)
    un = int(prix - mille*1000 - vingtcinq*25 - cinq*5)
    print(mille, vingtcinq, cinq, un)

    b = []
    if (mille > 0):
        b.append(os.path.join(dirname,'voix/pref/vm.wav'))
        a = numberReader(mille)
        print(a)
        for i in range(0, len(a)):
            b.append(a[i])
    if (vingtcinq > 0):
        b.append(os.path.join(dirname,'voix/pref/vv.wav'))
        a = numberReader(vingtcinq)
        print(a)
        for i in range(0, len(a)):
            b.append(a[i])
    if (cinq > 0):
        b.append(os.path.join(dirname,'voix/pref/vc.wav'))
        a = numberReader(cinq)
        print(a)
        for i in range(0, len(a)):
            b.append(a[i])
    if (un > 0):
        b.append(os.path.join(dirname,'voix/pref/vf.wav'))
        a = numberReader(un)
        print(a)
        for i in range(0, len(a)):
            b.append(a[i])
    return b


def denreeReader(denree):
    b=[]
    b.append(os.path.join(dirname,'voix/denree/'+denree+'.wav'))
    return b

def marcheReader(marche):
    b=[]
    b.append(os.path.join(dirname,'voix/marche/'+marche+'.wav'))
    return b




def concatenate_audio_moviepy(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""

    global i
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)

    final_clip.write_audiofile(output_path,)
    i=i+1




def send_audio(audio_clip_paths):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""

    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    f = AudioSegment(final_clip)
    return f
    
