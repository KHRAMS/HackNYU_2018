# @author Jinal Shah 
 
import collections 
import logging 
import os 
from copy import copy 
 
from flask import Flask, json 
from flask_ask import Ask, question, statement, audio, current_stream, logger 
 
app = Flask(__name__) 
ask = Ask(app, "/") 
logging.getLogger('flask_ask').setLevel(logging.INFO) 
 
 
calmdownplaylist = [ 
    # 'https://www.freesound.org/data/previews/367/367142_2188-lq.mp3', 
    'https://archive.org/download/mailboxbadgerdrumsamplesvolume2/Ringing.mp3', 
    'https://archive.org/download/petescott20160927/20160927%20RC300-53-127.0bpm.mp3', 
    'https://archive.org/download/plpl011/plpl011_05-johnny_ripper-rain.mp3', 
    'https://archive.org/download/piano_by_maxmsp/beats107.mp3', 
    'https://archive.org/download/petescott20160927/20160927%20RC300-58-115.1bpm.mp3', 
    'https://archive.org/download/PianoScale/PianoScale.mp3', 
    # 'https://archive.org/download/FemaleVoiceSample/Female_VoiceTalent_demo.mp4', 
    'https://archive.org/download/mailboxbadgerdrumsamplesvolume2/Risset%20Drum%201.mp3', 
    'https://archive.org/download/mailboxbadgerdrumsamplesvolume2/Submarine.mp3', 
    # 'https://ia800203.us.archive.org/27/items/CarelessWhisper_435/CarelessWhisper.ogg' 
] 
 
 
class QueueManager(object): 
    """Manages queue data in a seperate context from current_stream. 
    The flask-ask Local current_stream refers only to the current data from Alexa requests and Skill Responses. 
    Alexa Skills Kit does not provide enqueued or stream-histroy data and does not provide a session attribute 
    when delivering AudioPlayer Requests. 
    This class is used to maintain accurate control of multiple streams, 
    so that the user may send Intents to move throughout a queue. 
    """ 
 
    def __init__(self, urls): 
        self._urls = urls 
        self._queued = collections.deque(urls) 
        self._history = collections.deque() 
        self._current = None 
 
    @property 
    def status(self): 
        status = { 
            'Current Position': self.current_position, 
            'Current URL': self.current, 
            'Next URL': self.up_next, 
            'Previous': self.previous, 
            'History': list(self.history) 
        } 
        return status 
 
    @property 
    def up_next(self): 
        """Returns the url at the front of the queue""" 
        qcopy = copy(self._queued) 
        try: 
            return qcopy.popleft() 
        except IndexError: 
            return None 
 
    @property 
    def current(self): 
        return self._current 
 
    @current.setter 
    def current(self, url): 
        self._save_to_history() 
        self._current = url 
