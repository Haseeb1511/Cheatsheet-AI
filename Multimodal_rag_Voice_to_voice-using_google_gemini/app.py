import streamlit as st
from model import voice_input,llm,text_to_speech

def main():
    st.title("MultiLingual AI assistant")
    if st.button("Click to Speak"):
        with st.spinner("listining...."):
            voice = voice_input()
            if voice:
                response = llm(voice)
                text_to_speech(response)

                with open("speech.mp3","rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.text_area(label="responses:",value=response)
                    st.audio(audio_bytes,format="audio/mp3")
                    st.download_button(label="Donwload file",
                                    data=audio_bytes,
                                    file_name="speech.mp3",
                                mime="audio/mp3")
            else:
                st.error("Could not capture voice")

if __name__=="__main__":
    main()