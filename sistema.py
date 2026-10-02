# Passo a passo 

# Streamlit -- para criar a interface web
# pandas -- para analise de dados
# Plotly -- para gráficos interativos
# pip install streamlit Pandas Plotly

    


    # Tabela com as vendas cadastradas
        # Colunas: Data, Vendedor, Quantidade, Valor

    

import streamlit as st
import pandas as pd 
import plotly.express as px


# streamlit run sistema.py
#st.title("Usar para por nome do sistema barra de pesquisa")

# titulo - Sistema de Vendas
st.write("# Sistema de Vendas") # nome do sistema

# carregar a base de dados de vendas
tabela_vendas = pd.read_csv("vendas.csv") # extraindo a base de dados do arquivo vendas.csv

st.write("## Cadastrar Vendas") # nome da seção de cadastro de vendas

# Seção Cadastrar Vendas

st.sidebar.write("## Cadastrar Vendas") # nome da seção de cadastro de vendas na barra lateral
# Campo Data"
data = st.sidebar.date_input("Data") # campo para selecionar a data da venda
# Campo Vendedor - Ana, Bruno, Carla
st.sidebar.selectbox(" Vendedor", ["Ana", "Bruno", "Carla"]) # campo para selecionar o vendedor
vendedor = st.selectbox("Vendedor", ["Ana", "Bruno", "Carla"]) # campo para selecionar o vendedor
# campo Produto - Celular, Notbook, Fone de Ouvido
st.sidebar.selectbox("Produto", ["Celular", "Notebook", "Fone de Ouvido"]) # campo para selecionar o produto
produto = st.selectbox("Produto", ["Celular", "Notebook", "Fone de Ouvido"]) # campo para selecionar o produto
# Campo Quantidade
st.sidebar.selectbox("Quantidade", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # campo para selecionar a quantidade de produtos
quantidade = st.selectbox("Quantidade", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # campo para selecionar a quantidade de produtos
# Campo Valor
st.sidebar.selectbox("Valor", [000.00, 100.00, 200.00, 300.00, 400.00]) # campo para selecionar o valor do produto
valor = st.selectbox("Valor", [000.00, 100.00, 200.00, 300.00, 400.00]) # campo para selecionar o valor do produto
# Botão Cadastrar Venda
botao_cadastrar = st.sidebar.button("Cadastrar Venda") # botão para cadastrar a venda

# seção de cadastro de vendas
if botao_cadastrar: # verifica se o botão de cadastrar venda foi clicado
    nova_venda = [str(data), vendedor, produto, quantidade, valor] # nova venda cadastrada
    ultima_linha = len(tabela_vendas) # pegar a ultima linha da tabela de vendas
    tabela_vendas.loc[ultima_linha] = nova_venda # adicionar a nova venda na tabela de vendas
    tabela_vendas.to_csv("vendas.csv", index=False) # salvar a tabela de vendas no arquivo vendas.csv
    st.success("Venda cadastrada com sucesso!") # mostrar a mensagem de sucesso ao cadastrar a venda

# Seção de visualização Vendas Cadastradas
st.write("## Vendas Cadastradas") # mostrar a tabela de vendas cadastradas
st.dataframe(tabela_vendas) # mostrar a tabela de vendas cadastradas na tela

# Seção Dashboard
st.write("## Dashboard") # mostrar o dashboard com os gráficos de vendas
st.metric("Total de Vendas Cadastradas", len(tabela_vendas))
# Card com o total de vendas cadastradas
faturamento = tabela_vendas["valor"].sum() # calcular o faturamento total das vendas cadastradas
st.metric("Faturamento Total", f"R$ {faturamento:.2f}")

# Gráfico de barras com a quantidade de vendas por vendedor
grafico_barras = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", title="Quantidade de Vendas por Vendedor") # gráfico de barras com a quantidade de vendas por vendedor
st.plotly_chart(grafico_barras) # mostrar o gráfico de barras

# Gráfico de pizza com a porcentagem de vendas por vendedor
grafico_pizza = px.pie(tabela_vendas, values="valor", names="produto", title="Porcentagem de Vendas por Vendedor", hole=0.60) # gráfico de pizza com a porcentagem de vendas por vendedor
st.plotly_chart(grafico_pizza) # mostrar o gráfico de pizza

# mostrar a mensagem "Venda cadastrada com sucesso!"
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor] # nova venda cadastrada
    tabela_vendas.loc[ultima_linha] = nova_venda # adicionar a nova venda na tabela de vendas
    tabela_vendas.to_csv("vendas.csv", index=False) # salvar a tabela de vendas no arquivo vendas.csv
    st.success("Venda cadastrada com sucesso!") # mostrar a mensagem de sucesso ao cadastrar a venda