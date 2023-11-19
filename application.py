
import streamlit as st
import whisper
import os

# Set the FFMPEG_BINARY environment variable
#os.environ["FFMPEG_BINARY"] = "/usr/bin/ffmpeg"  # Replace with your ffmpeg path

st.title("call center")

# Rest of your code remains unchanged

st.title("call center")

audio_file = st.file_uploader("Upload Audio", type={"wav", "mp3", "m4a"})

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.sidebar.button("Transcribe Audio"):
	if audio_file is not None:
		st.sidebar.success("Transcribing Audio")
		transcription = model.transcribe(audio_file.name)
		st.sidebar.success("Transcription Complete")
		st.markdown(transcription["text"])
	else:
		st.sidebar.error("Please upload an audio file")
			
st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    st.run_on_save()
    st.server.run(port=port)
