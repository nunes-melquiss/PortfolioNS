import streamlit as st
import base64
from PIL import Image


# Ajustar a página para modo "wide"
st.set_page_config(layout="wide",page_title='Nunes | Portfólio')

# Carregar a imagem da pasta 'data'
image = Image.open("data/foto.jpg")

# Criar duas colunas
col1, _, col2 = st.columns([1,0.5, 3])  # Ajusta a proporção entre as colunas

# Exibir a imagem na primeira coluna
with col1:
    st.image(image, width=300)  # Ajusta o tamanho da imagem

# Exibir o título na segunda coluna
with col2:
    st.markdown('<div class="title-column">', unsafe_allow_html=True)
    st.markdown('<h1>Olá!</h1>', unsafe_allow_html=True)
    st.markdown('<h1>Meu nome é <span style="color:#00A2E8;">Nunes</span>,</h1>', unsafe_allow_html=True)
    st.markdown('<h1>Promovo uma cultura de dados!</h1>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



col3, col4 = st.columns([4,2])
# Descrição inicial (abaixo das colunas)


with col3:
    st.subheader('\n \n \n')
    st.subheader('\n \n \n')
    st.title('SOBRE MIM')
    st.subheader('\n')

    st.markdown("""
        Sou apaixonado pela lapidação de dados brutos até a entrega de informações confiáveis e acessíveis. <br> Utilizo habilidades avançadas em 
        <span style="color:#00A2E8;">VBA</span> para automatizar processos no pacote Office, 
        <span style="color:#00A2E8;">Python</span> para elaboração de softwares, análises de dados e automação de tarefas, além de 
        <span style="color:#00A2E8;">M</span> para otimização na limpeza e transformação de dados através do 
        <span style="color:#00A2E8;">Power Query</span>. 
        <br> Domino também ferramentas de visualização de dados, especiamente o 
        <span style="color:#00A2E8;">Power BI</span> e tenho conhecimentos em computação em nuvem (coleta, tratamento e visualização de dados com ferramentas SAAS da 
         <span style="color:#00A2E8;">AWS e AZURE</span>)
        """, unsafe_allow_html=True)

    st.markdown("""
        Comecei minha trajetória acadêmica cursando Engenharia Mecânica na 
        <span style="color:#00A2E8;">Universidade Federal de Minas Gerais</span> em 2018. <br> 
        Após cursar alguns períodos, concluir o ciclo básico das engenharias e ter algumas experiências profissionais na área, descobri minha paixão em outro lugar: nos dados. <br>
        Atualmente estou conciliando uma graduação relacionada ao ecossistema dos dados na 
        <span style="color:#00A2E8;">PUC Minas</span>, inúmeros cursos livres na área e responsabilidades de um Analista de Dados em um emprego formal.
        """, unsafe_allow_html=True)
    
st.subheader('\n \n \n \n')
st.title('PROJETOS RECENTES')
st.subheader('\n')

col5, _, col6 = st.columns([1.5,0.5,2])
with col5:
    st.subheader('Distribuição Salarial por Gênero em MG')
    st.markdown("""
                Esse projeto foi realizado com o intuito de verificar a discrepância salarial entre genêros no funcionalismo público do Estado de Minas Gerais.
                Para sua execução utilizei apenas 
                <span style="color:#00A2E8;">Python</span>, fazendo uso das bibliotecas 
                <span style="color:#00A2E8;">Streamlite, Pandas, Numpy, Matplotlib e Plotly</span>.
                <br> Clique na imagem ou no link para ser redirecionado para a pagina do projeto.
                <br> <br> https://servidorasmg.streamlit.app/
                """, unsafe_allow_html=True)


with col6:
    # Função para converter a imagem para base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Caminho da imagem
    imagem_servidoras_path = "data/servidorasdash.jpg"  # Substitua pelo caminho da sua imagem
    url = "https://servidorasmg.streamlit.app/"  # Substitua pelo link desejado



    # Converter a imagem para base64
    img_base641 = image_to_base64(imagem_servidoras_path)


    st.markdown(
            f"""
            <style>
            .img-border {{
                border: 2px solid black;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <a href="{url}" target="_blank">
                <img src="data:image/jpeg;base64,{img_base641}" class="img-border" width="600">
            </a>
            """,
            unsafe_allow_html=True
        )

st.subheader('\n \n')
st.subheader('\n \n')


col7, _, col8 = st.columns([1.5,0.5,2])
with col7: 
    st.subheader('Verificador de Inconsistências em Bancos de Dados .csv')
    st.markdown("""
                Por vezes, temos a necessidade de executar complexas tarefas de análise de confiabilidade de dados e 
                temos disponíveis para isso apenas ferramentas do Pacote Office. 
                <br> Realizei esse projeto, que consiste em uma planilha de Excel incluindo várias 
                <span style="color:#00A2E8;">macros VBA</span> e um dashboard em 
                <span style="color:#00A2E8;">Power BI</span>, para essas ocasiões.
                <br> Em outro momento, dado a necessidade de escalabilidade da ferramenta, esse projeto também foi reescrito em 
                <span style="color:#00A2E8;">Python</span>.
                <br> Ao clicar na imagem ou no link você será redirecionado para a pagina do projeto.
                <br> <br> https://servidorasmg.streamlit.app/
                """, unsafe_allow_html=True)


with col8:
    # Caminho da imagem 2
    imagem_inconsistencia_path = "data/inconsistenciasferramenta.jpg"  # Substitua pelo caminho da sua imagem
    url = "https://servidorasmg.streamlit.app/"  # Substitua pelo link desejado
    # Converter a imagem para base64
    img_base642 = image_to_base64(imagem_inconsistencia_path)

    st.markdown(
            f"""
            <style>
            .img-border {{
                border: 2px solid black;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <a href="{url}" target="_blank">
                <img src="data:image/jpeg;base64,{img_base642}" class="img-border" width="600">
            </a>
            """,
            unsafe_allow_html=True
        )

st.subheader('\n')


col9, _, col10 = st.columns([1.5,0.5,2])
with col9: 
    st.subheader('Sistema de input de dados de CRM')
    st.markdown("""
                Antes de realizar uma análise dos dados de determinada área, é necessário garantir que o armazenamento e gerenciamento dos
                dados de interesse estão sendo realizados corretamente. 
                <br> Pensando na uniformidade do armazenamento dos dados de Customer Relationship Management, elaborei uma interface completa em 
                <span style="color:#00A2E8;">Python</span>, utilizando principalmente a biblioteca 
                <span style="color:#00A2E8;">PyQt5</span>, que facilita o gerenciamento e a consulta desses dados pelo usuário e garante a uniformidade dos dados para a elaboração de relatórios.
                <br> Ao clicar na imagem ou no link você será redirecionado para a pagina do projeto.
                <br> <br> https://servidorasmg.streamlit.app/
                """, unsafe_allow_html=True)


with col10:
    # Caminho da imagem 2
    imagem_crm_path = "data/crmn.jpg"  # Substitua pelo caminho da sua imagem
    url = "https://servidorasmg.streamlit.app/"  # Substitua pelo link desejado
    # Converter a imagem para base64
    img_base643 = image_to_base64(imagem_crm_path)

    st.markdown(
            f"""
            <style>
            .img-border {{
                border: 2px solid black;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            </style>
            <a href="{url}" target="_blank">
                <img src="data:image/jpeg;base64,{img_base643}" class="img-border" width="600">
            </a>
            """,
            unsafe_allow_html=True
        )