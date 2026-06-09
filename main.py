import pandas as pd
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

st.set_page_config(page_title="CPTM Ocorrência")

st.markdown("""
            # CPTM

            ## Ocorrências dentro da Companhia Paulista de Trens Metropolitanos

            Será apresentado análises voltado as ocorrências
            """)

arquivo_baixado: UploadedFile | None = st.file_uploader(
    label="Escolha o arquivo que deseja", type="csv"
)

if arquivo_baixado:
    df = pd.DataFrame(arquivo_baixado)
    st.dataframe(df)
