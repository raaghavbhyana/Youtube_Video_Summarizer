import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM




def transcript(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id,preserve_formatting=True)
        transcript=""
        for i in transcript_text:
            transcript +=" "+ i['text']
        
        return transcript
    except:
        pass

        
def summarizer(transcript_text,words):
    template="""You are  Youtube Video Summarizer. You will be taking transcript text 
    and summarizing the entire video and providing the  summary in  points in about {No_of_words} words.
    Please provide the summary here:{text}
    """
    llm = Ollama(model="llama2")
    prompt_one =PromptTemplate(input_variables=["No_of_words","text"],template=template)

    
    response=llm(prompt_one.format(No_of_words=words,text=transcript_text))
    return response
    
    



st.title("Youtube Video Summarizer")
youtube_link=st.text_input("Enter Youtube url you want summary of:")
words=st.text_input("Enter the number of words you want summary in:")
if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

if st.button("Get Summary:"):
    transcript_text=transcript(youtube_link)
    print(transcript_text)
    
    if transcript_text:
        
        st.markdown("##Summary")
        st.write(summarizer(transcript_text,words))
    
