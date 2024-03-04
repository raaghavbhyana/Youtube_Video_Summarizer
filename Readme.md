## YouTube Video Summarizer

This project provides an automated solution for summarizing YouTube videos. It leverages the `youtube_transcript_api` to fetch transcripts, utilizes `langchain` to harness an open-source, locally installed large language model (LLM), and employs the `streamlit` library to create a user-friendly web application for video summarization.


**Features:**

* Automatic video summarization

*Features:**

- Leverages `youtube_transcript_api` to fetch transcripts
- Utilizes `langchain` to harness the open-source, locally installed OLLama's Llama2 large language model (LLM) for summarization
- Employs the `streamlit` library to create a user-friendly web application

**How It Works:**

1. **User Input:** The user enters a YouTube video URL and specifies the desired summary length (number of words).
2. **Transcript Fetching:** The transcript is retrieved using the `youtube_transcript_api`.
3. **Summarization:** The script feeds the transcript to the Llama2 model through `langchain` to generate a summary.
4. **Output:** The generated summary is displayed on the web app using Streamlit.

**Disclaimer:**

- This project requires a locally installed Ollama application and the Llama2 LLM model.
- Refer to the `langchain` documentation for setup instructions.

**Upcoming Enhancements:**

- Server deployment to avoid reliance on local LLMs for users.

**Contributions Welcome!**

Feel free to contribute to this project and share your ideas!