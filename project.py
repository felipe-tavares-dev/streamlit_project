from turtle import title
import streamlit as st
import pandas as pd
st.write("""
    # Manipulação de dados com python!
""")

st.write("""
    **Para começarmos primeiramente temos que importar nossa base de dados!** 
""")

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

st.dataframe(df)

st.write("  ")

st.write("### Filtrando os dados com pandas + streamlit")

resultado = st.selectbox("Qual linguagem deseja escolher?", df["Linguagem"].unique(), index=0)

if st.button("Click em mim para filtrar"):
    df_filtrado = df[df["Linguagem"] == resultado]
    st.dataframe(df_filtrado)

st.write("  ")

st.write("### Filtrando os dados por Popularidade")

escolha_usuario = st.selectbox("Quem é a linguagem mais popular?", df["Popularidade"].unique(), index=0)

if st.button("Click em mim"): 
    df_filtrado = df[df["Popularidade"] == escolha_usuario]
    st.dataframe(df_filtrado)


st.write("  ")

st.write('''### Qual a linguagem mais popular?''')
st.bar_chart(df, x="Linguagem", y='Desenvolvedores', color='Linguagem')

st.write("  ")

st.write("### Empilhando as linguagens pela popularidade")
st.bar_chart(df, x = "Popularidade", y = 'Desenvolvedores')

st.write("Desenvolvido e criado por [Felip Tavares](https://github.com/felipe-tavares-dev?tab=repositories).")