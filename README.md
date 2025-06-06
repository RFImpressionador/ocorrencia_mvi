# ocorrencia_mvi

Simple Streamlit project for registering police occurrences using Supabase as backend storage.

## Setup

1. Install Python and the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Define your Supabase credentials in the environment variables `SUPABASE_URL` and `SUPABASE_KEY`. You can export them in the shell or create a `.env` file and load it before running the app.

## Running

Launch the Streamlit application with:
```bash
streamlit run app.py
```

## Images in Supabase

Uploaded photos are stored in the Supabase Storage bucket named `imagens`. Each record is placed in subfolders (e.g., `vitimas`, `autores`, `testemunhas`) and receives a unique name.
