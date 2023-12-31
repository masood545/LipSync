# -*- coding: utf-8 -*-
"""Untitled98.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HSGejqHcsKEGyoa6eCQuaEI_yW1KRmEY
"""

import os
directory = 'LipSync'
path = os.path.join(os.getcwd(),directory)
os.mkdir(path)
os.chdir(path)

!git clone https://github.com/zabique/Wav2Lip

#download the pretrained model

!wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O 'Wav2Lip/checkpoints/wav2lip_gan.pth'
a = !pip install https://raw.githubusercontent.com/AwaleSajil/ghc/master/ghc-1.0-py3-none-any.whl

# !pip uninstall tensorflow tensorflow-gpu
!cd Wav2Lip && pip install -r requirements.txt

#download pretrained model for face detection
!wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "Wav2Lip/face_detection/detection/sfd/s3fd.pth"

!pip install -q youtube-dl
!pip install ffmpeg-python
!pip install librosa==0.9.1
!pip install numpy
!pip install opencv-contrib-python>=4.2
!pip install opencv-python==4.1.0.25
!pip install pytorch-cpu==1.1.0 torchvision-cpu==0.3.0 cpuonly -c pytorch
!pip install tqdm

os.chdir(str(os.getcwd())+'/Wav2Lip')
from google.colab import files
uploaded = files.upload()

file_list = os.listdir(os.getcwd())
video_file_path = str(os.getcwd())+'/'+str([path for path in file_list if path[-4:]=='.mp4'][0])
audio_file_path = str(os.getcwd())+'/'+str([path for path in file_list if path[-4:]=='.wav'][0])

os.rename(video_file_path,str(os.getcwd())+'/'+'video.mp4')
os.rename(audio_file_path,str(os.getcwd())+'/'+'audio.wav')

!python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "video.mp4" --audio "audio.wav"