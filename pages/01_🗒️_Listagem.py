import streamlit as st
from st_aggrid  import AgGrid

st.markdown(
    '''
    <h2 style='text-align: center'>Visualização de Dados</h2>
    ''', unsafe_allow_html=True
)

if 'dados' not in st.session_state:
    st.error('Dados não carregados!')
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']
    dados_filtrados = dados.head(top_n)
    AgGrid(dados_filtrados, fit_columns_on_grid_load=True)