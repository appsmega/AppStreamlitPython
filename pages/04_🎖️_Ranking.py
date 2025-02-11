import streamlit as st
import plotly.express as px

st.markdown(
    '''
    <h2 style='text-align: center'>Ranking</h2>
    ''', unsafe_allow_html=True
)

if 'dados' not in st.session_state:
    st.error('Dados não carregados!')
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        max_empenho = dados.nlargest(top_n, 'VALOREMPENHO')
        max_empenho = max_empenho.sort_values(by='VALOREMPENHO', ascending=True)
        graph01 = px.bar(max_empenho, x='VALOREMPENHO', y='MUNICIPIO', title='Maiores Empenhos por Munícipio', color_discrete_sequence=['#cb68e9'])
        graph01.update_layout(xaxis_title = 'Valor de Empenho', yaxis_title = '')
        st.plotly_chart(graph01, use_container_width=True)
        
    with col2:
        max_pib = dados.nlargest(top_n, 'PIB')
        max_pib = max_pib.sort_values(by='PIB', ascending=True)
        graph02 = px.bar(max_pib, x='PIB', y='MUNICIPIO', title='Maiores PIBs por Munícipio', color_discrete_sequence=['#cb68e9'])
        graph02.update_layout(xaxis_title = 'PIB', yaxis_title = '')
        st.plotly_chart(graph02, use_container_width=True)
        
    with col3:
        max_proporcao = dados.nlargest(top_n, 'PROPORCAO')
        graph03 = px.pie(max_proporcao, values='PROPORCAO', names='MUNICIPIO', title='Melhores Proporções ao PIB')
        st.plotly_chart(graph03, use_container_width=True)