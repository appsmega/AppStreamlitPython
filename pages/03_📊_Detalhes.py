import streamlit as st
import plotly.express as px

st.markdown(
    '''
    <h2 style='text-align: center'>Distribuição de Dados</h2>
    ''', unsafe_allow_html=True
)

if 'dados' not in st.session_state:
    st.error('Dados não carregados!')
else:
    dados = st.session_state['dados']
    
    tab1, tab2 = st.tabs(['Valor de Empenho', 'Produto Interno Bruto - PIB'])
    
    with tab1:
        col1, col2 = st.columns(2)
    
        with col1:
            graph01 = px.histogram(dados, x = 'VALOREMPENHO', title='Histograma', color_discrete_sequence=['#cb68e9'])
            graph01.update_layout(xaxis_title = '', yaxis_title = '')
            st.plotly_chart(graph01, use_container_width=True)
        with col2:
            graph02 = px.box(dados, x = 'VALOREMPENHO', title='Boxplot', color_discrete_sequence=['#cb68e9'])
            graph02.update_layout(xaxis_title = '', yaxis_title = '')
            st.plotly_chart(graph02, use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
    
        with col1:
            graph03 = px.histogram(dados, x = 'PIB', title='Histograma', color_discrete_sequence=['#cb68e9'])
            graph03.update_layout(xaxis_title = '', yaxis_title = '')
            st.plotly_chart(graph03, use_container_width=True)
        with col2:
            graph04 = px.box(dados, x = 'PIB', title='Boxplot', color_discrete_sequence=['#cb68e9'])
            graph04.update_layout(xaxis_title = '', yaxis_title = '')
            st.plotly_chart(graph04, use_container_width=True)