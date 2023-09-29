# LipSync

To run and validate the result follow the procedure below:

1. Open the LipSync.ipynb notebook in Google colab or in an editor. 
2. Code explanation :
   1) Creates a folder called "LipSync" in your current directory
   2) Clones the 'Wav2Lip' repository from Git Hub.
   3) Installs libraries mentioned in 'requirements.txt' present inside of the 'Wav2Lip' directory.
   4) Downloads the pre-trained model from :
       https://iiitaphydmy.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspxshare=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA
   6) Downloads the pre-trained model for face detection from       
       https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth
   5) import necessary libraries
   6) Asks to Upload video and audio files
   7) Runs the Inference by taking inputs such as model_checkpoints path,video_path, and audio_path.
   8) The final resultant video file will be stored in the Wav2lip/results/result_voice.mp4 path.
