# -*- coding: utf-8 -*-

import sys
import threading
import os, platform
import subprocess
import signal
import classes.extras as ex

class Speaker(threading.Thread):
    def __init__(self, lang, configo):
        threading.Thread.__init__(self)
        self.lang = lang
        self.enabled = True
        self.started = False

        self.process = None
        self.talkative = False
        if sys.version_info < (3, 0):
            self.needs_encode = False
        else:
            self.needs_encode = True

    def start_server(self):
        if self.enabled and self.lang.voice is not None:
            #voices = ["-s 190 -a 100 -p 75 -ven+m1 ", "-s 170 -a 100 -p 80 -ven+m2 ","-s 175 -a 100 -p 80 -ven+m3 ","-s 190 -a 100 -p 60 -ven+f1 ","-s 170 -a 100 -p 75 -ven+f2 ","-s 170 -a 100 -p 80 -ven+m2 "]
            cmd = ['espeak']
            cmd.extend(self.lang.voice)
            try:
                #IS_WIN32 = 'win32' in str(sys.platform).lower() #maybe sys.platform is more secure
                is_win = platform.system() == "Windows"
                if is_win:
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = subprocess.SW_HIDE
                    kwargs = {}
                    kwargs['startupinfo'] = startupinfo
                    #self.process = subprocess.Popen(cmd, shell=True, bufsize=0, close_fds=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
                    self.process = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
                else:
                    self.process = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                #self.process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.started = True

            except:
                self.enabled = False
                self.started = False
                print("pySioGame: You may like to install espeak to get some extra functionality, however this is not required to successfully use the game.")
            #stdout and stderr only used to hide the messages from terminal
        else:
            self.process = None

    def restart_server(self):
        if self.started:
            self.stop_server()
        self.start_server()
        
    def run(self):
        pass
        
    def stop_server(self):
        if self.enabled and self.started and self.process is not None:
            self.process.stdin.close()
            self.process.stdout.close()
            self.process.stderr.close()
            try:
                os.kill(self.process.pid, signal.SIGTERM)
            except OSError:
                print("Error killing the espeak process")

    def say(self,text,voice=1):
        if self.enabled and self.talkative and self.lang.voice is not None:
            text = self.check_letter_name(text)
            text = text + "\n"
            try:
                text = text.encode("utf-8")
            except:
                pass
                
            try:
                self.process.stdin.write(text)
                self.process.stdin.flush()
            except:
                pass
            
    def check_letter_name(self,text):
        if sys.version_info < (3, 0):
            try:
                val = ex.unival(text)
            except:
                val = text
            if len(val) == 1 and len(self.lang.letter_names) > 0:
                t = ex.unival(val.lower())
                for i in range(len(self.lang.alphabet_lc)):
                    if t == ex.unival(self.lang.alphabet_lc[i]):
                        text = self.lang.letter_names[i]
                        break
        else:
            if len(text) == 1 and len(self.lang.letter_names)>0:
                t = text.lower()
                for i in range(len(self.lang.alphabet_lc)):
                    if t == self.lang.alphabet_lc[i]:
                        text = self.lang.letter_names[i]
                        break
        return text
