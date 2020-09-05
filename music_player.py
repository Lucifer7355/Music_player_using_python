def unmutemusic():
  global currentvol
  root.unMuteButton.grid_remove()
  root.MuteButton.grid()
  mixer.music.set_volume(currentvol)
  
def mutemusic():
  global currentvol
  root.MuteButton.grid_remove()
  root.unMuteButton.grid()
  currentvol = mixer.music.get_volume()
  mixer.music.set_volume(0)
  
def resumemusic():
  root.ResumeButton.grid_remove()
  root.PauseButton.grid()
  mixer.music.unpause()
  
def stopmusic():
  mixer.music.stop()
  AudioStatusLabel.configure(text='stopped........')


def volumeupar():
  vol = mixer.music.get_volume()
  mixer.music.set_volume(vol+0.05)
  ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume()*100)))
  ProgressbarVolume['value'] = mixer.music.get_volume()*100
  
def volumeniche():
  vol = mixer.music.get_volume()
  mixer.music.set_volume(vol-0.05)
  ProgressbarVolumeLabel.configure(text = '{}%'.format(int(mixer.music.get_volume()*100)))
  ProgressbarVolume['value'] = mixer.music.get_volume()*100 

def pausemusic():
  mixer.music.pause()
  root.PauseButton.grid_remove()
  root.ResumeButton.grid()
  AudioStatusLabel.configure(text='paused........')

def playmusic():
  ad = audiotrack.get()
  mixer.music.load(ad)
  ProgressbarLabel.grid()
  root.MuteButton.grid()
  ProgressbarMusicLabel.grid()
  mixer.music.set_volume(0.4)
  ProgressbarVolume['value'] = 40
  ProgressbarVolumeLabel['text'] = '40%'
  mixer.music.play()
  AudioStatusLabel.configure(text='playing........')

  Song = MP3(ad)
  totalsonglength = int(Song.info.length)
  ProgressbarMusic['maximum'] = totalsonglength 
  ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
  def Progressbarmusictick():
    CurrentSongLength = mixer.music.get_pos()
    ProgressbarMusic['value'] = CurrentSongLength
    ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
    ProgressbarMusic.after(2,Progressbarmusictick)
  Progressbarmusictick()
  
def musicurl():
  try:
    dd = filedialog.askopenfilename(initialdir='C://Users//acer//Downloads//music',title='Select Audio File',filetype=(('MP3','.mp3'),('WAV','.wav')))
  except:
    dd = filedialog.askopenfilename(title='Select Audio File',filetype=(('MP3','.mp3'),('WAV','.wav')))

  audiotrack.set(dd)

def createwidthes():

  global iamplay,iampause,iamsearch,iamvolumeup,iamvolumedown,iamstop,iamresume,iammute,iamunmute
  global ProgressbarMusicEndTimeLabel,AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic
  global ProgressbarMusicStartTimeLabel
  
  iamplay = PhotoImage(file='play.png')
  iampause = PhotoImage(file='pause.png')
  iamstop = PhotoImage(file='stop.png')
  iamsearch = PhotoImage(file='search.png')
  iamvolumeup = PhotoImage(file='turn-up-volume.png')
  iamvolumedown = PhotoImage(file='volume-down.png')
  iamresume = PhotoImage(file='end.png')
  iammute = PhotoImage(file='')
  iamunmute = PhotoImage(file='')
  
  
  iamplay = iamplay.subsample(20,20)
  iampause = iampause.subsample(20,20)
  iamstop = iamstop.subsample(20,20)
  iamsearch = iamsearch.subsample(20,20)
  iamvolumeup = iamvolumeup.subsample(20,20)
  iamvolumedown = iamvolumedown.subsample(20,20)
  iamresume = iamresume.subsample(20,20)
  iammute = iammute.subsample(20,20)
  iamunmute = iamunmute.subsample(20,20)
  
  TrackLabel = Label(root,text='Select Audio Track : ',background='lightskyblue',font=('arial',15,'italic bold'))
  TrackLabel.grid(row=0,column=0,padx=20,pady=20)
  
  AudioStatusLabel = Label(root,text='',background='lightskyblue',font=('arial',15,'italic bold'),width=20)
  AudioStatusLabel.grid(row=2,column=1)
  
  TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
  TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

  BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamsearch,compound=RIGHT,command=musicurl)
  BrowseButton.grid(row=0,column=2,padx=20,pady=20)

  PlayButton = Button(root,text='Play',bg='green2',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamplay,compound=RIGHT,command=playmusic)
  PlayButton.grid(row=1,column=0,padx=20,pady=20)

  root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iampause,compound=RIGHT,command=pausemusic)
  root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

  root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamresume,compound=RIGHT,command=resumemusic)
  root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)

  root.ResumeButton.grid_remove()

  root.MuteButton = Button(root,text='Mute',bg='yellow',font=('arial',13,'italic bold'),width=100,bd=5,activebackground='purple4',image=iammute,compound=RIGHT,command=mutemusic)
  root.MuteButton.grid(row=3,column=3)
  root.MuteButton.grid_remove()
  
  root.unMuteButton = Button(root,text='Unmute',bg='yellow',font=('arial',13,'italic bold'),width=100,bd=5,activebackground='purple4',image=iamunmute,compound=RIGHT,command=unmutemusic)
  root.unMuteButton.grid(row=3,column=3)
  root.unMuteButton.grid_remove()

  VolumeUpButton = Button(root,text='VolumeUp',bg='blue',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamvolumeup,compound=RIGHT,command=volumeupar)
  VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)
  
  StopButton = Button(root,text='Stop',bg='red',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamstop,compound=RIGHT,command=stopmusic)
  StopButton.grid(row=2,column=0,padx=20,pady=20)

  VolumeDownButton = Button(root,text='VolumeDown',bg='blue',font=('arial',13,'italic bold'),width=200,bd=5,activebackground='purple4',image=iamvolumedown,compound=RIGHT,command=volumeniche)
  VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

  ProgressbarLabel = Label(root,text='',bg='red')
  ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
  ProgressbarLabel.grid_remove()
  
  ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
  ProgressbarVolume.grid(row=0,column=0,ipadx=5)

  ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
  ProgressbarVolumeLabel.grid(row=0,column=0)

  ProgressbarMusicLabel = Label(root,text='',bg='red')
  ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
  ProgressbarMusicLabel.grid_remove()
  
  ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=6)
  ProgressbarMusicStartTimeLabel.grid(row=3,column=0)

  ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
  ProgressbarMusic.grid(row=3,column=1,ipadx=370,ipady=3)
  #ProgressbarMusic.grid_remove()
  
  ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red')
  ProgressbarMusicEndTimeLabel.grid(row=3,column=2)
  
  
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3


root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player...')
root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')

audiotrack = StringVar()
currentvol = 0
ss = 'Developed By Ankit Srivastava'
totalsonglength = 0
count =0
text = ''
SliderLabel = Label(root,text='',bg='lightskyblue',font=('arial',40,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
  global count,text
  if(count>=len(ss)):
    count = -1
    text=''
    SliderLabel.configure(text=text)
  else:
    text = text + ss[count]
    SliderLabel.configure(text=text)
  count+=1
  SliderLabel.after(80,IntroLabelTrick)
  


IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()
