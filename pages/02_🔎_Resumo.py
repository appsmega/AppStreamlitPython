import streamlit as st
from st_aggrid  import AgGrid

st.markdown(
    '''
    <h2 style='text-align: center'>Resumo de Dados</h2>
    ''', unsafe_allow_html=True
)

if 'dados' not in st.session_state:
    st.error('Dados não carregados!')
else:
    dados = st.session_state['dados'].describe().reset_index()
    st.write(dados)