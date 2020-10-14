import ffmpeg
import os
#Directories
Outputfolder=r"D:\Courses\LINQ Fundamentals"
Videofolder=r"D:\Courses\LINQ Fundamentals Video"
Audiofolder=r"D:\Courses\LINQ Fundamentals Audio"
#################################################

#Get file names
videos=[]
audios=[]
for file in os.listdir(Videofolder):
    if file.split('.')[1]=='ts':
        videos.append(file)

for file in os.listdir(Audiofolder):
    audios.append(file)
################################################


#Merge video with audio
#videos and audios must be the same lenght
for i in range(len(videos)):
    vid=ffmpeg.input(os.path.join(Videofolder,videos[i]))
    aud=ffmpeg.input(os.path.join(Audiofolder,audios[i]))
    outname=videos[i].split('.')[0]
    outname+='.mp4'
    print("converting..." + outname)
    ffmpeg.concat(vid,aud,v=1,a=1).output(os.path.join(Outputfolder, outname)).run()
print("conversion Done successfully...")
###################################################
