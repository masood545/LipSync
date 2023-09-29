# LipSync

To run and validate the result follow the procedure below:

1. Open the LipSync.ipynb notebook in Google colab or in an editor. 
2. Code explanation :
   i) Creates a folder called "LipSync" in your current directory.
   ii) Clones the 'Wav2Lip' repository from Git Hub.
   iii) Installs libraries mentioned in 'requirements.txt' present inside of the 'Wav2Lip' directory.
   iv) Downloads the pre-trained model for face detection from       
       https://iiitaphydmy.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspxshare=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA
   v) import necessary libraries
   vi) Asks to Upload video and audio files
   vii) Runs the Inference by taking inputs such as model_checkpoints path,video_path, and audio_path.
   ix) The final resultant video file will be stored in the Wav2lip/results/result_voice.mp4 path.
