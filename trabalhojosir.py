import streamlit as st
import random
import io
from datetime import datetime

st.set_page_config(page_title="Recomendador de Looks", page_icon="👗", layout="centered")
st.title("👗 Recomendador de Looks Personalizado")
st.markdown("Responda algumas perguntas e receba uma sugestão de look com a sua cara!")

# PERGUNTAS DO FORMULÁRIO
ocasião = st.selectbox("1️⃣ Qual a ocasião?", [ 
    "Faculdade", "Shopping", "Date", "Praia", "Festa / Balada",
    "Museu", "Brunch", "Churrasco", "Cinema", "Teatro"
])

estilo = st.selectbox("2️⃣ Qual estilo você prefere?", [
    "Básico", "Fashionista", "Esportivo", "Romântico", "Despojado"
])

clima = st.selectbox("3️⃣ Como está o clima hoje?", [
    "Calor", "Frio", "Ameno", "Chuvoso"
])

humor = st.selectbox("4️⃣ Como você está se sentindo hoje?", [
    "Confiante", "Na dúvida", "Preguiçosa", "Quieta e estilosa", "Pronta pra brilhar"
])

tempo_fora = st.radio("5️⃣ Vai passar quanto tempo fora de casa?", [
    "O dia inteiro", "Só algumas horinhas", "Não sei ainda"
])

locomocao = st.selectbox("6️⃣ Vai como?", [
    "A pé", "Transporte público", "De carro", "Moto"
])

calçado_preferido = st.radio("7️⃣ Tem preferência de calçado?", [
    "Tênis", "Sandália", "Salto", "Bota", "Tanto faz"
])

vibe_cor = st.radio("8️⃣ Prefere algo mais colorido ou neutro?", [
    "Coloridão", "Tons pastéis", "Neutro e elegante", "Preto sempre"
])

acessorios = st.radio("9️⃣ Curte usar acessórios?", [
    "Sim, amo!", "Apenas alguns", "Prefiro evitar"
])

# BANCO DE DADOS DE OPÇÕES
partes_cima = {
    "Calor": ["regata soltinha", "cropped leve", "blusa de alça"],
    "Frio": ["suéter quentinho", "blusa de gola alta", "moletom estiloso"],
    "Ameno": ["camisa leve", "blusa de manga longa", "cardigan fofo"],
    "Chuvoso": ["jaqueta impermeável", "capa estilosa", "blusa com capuz"]
}

partes_baixo = {
    "Básico": ["jeans reto", "short jeans", "legging confortável"],
    "Fashionista": ["saia midi estampada", "calça cargo", "minissaia de couro"],
    "Esportivo": ["calça jogger", "short de treino", "legging com recortes"],
    "Romântico": ["saia rodada", "vestido floral curto", "short de linho"],
    "Despojado": ["calça rasgada", "short estampado", "bermuda jeans"]
}

calçados = {
    "Tênis": ["tênis branco", "tênis chunky", "tênis plataforma"],
    "Sandália": ["rasteirinha", "sandália plataforma", "sandália de tiras"],
    "Salto": ["salto grosso", "scarpin", "salto bloco confortável"],
    "Bota": ["coturno", "bota cano médio", "bota tratorada"],
    "Tanto faz": ["tênis estiloso", "sandália confortável", "bota leve"]
}

acessorios_por_estilo = {
    "Básico": ["relógio simples", "bolsa transversal"],
    "Fashionista": ["óculos escuros estilosos", "brincos grandes"],
    "Esportivo": ["boné", "mochilinha"],
    "Romântico": ["colar delicado", "tiara ou presilha"],
    "Despojado": ["pulseira de miçanga", "bucket hat"]
}

cores = {
    "Coloridão": "em cores vibrantes 🌈",
    "Tons pastéis": "em tons suaves 💗",
    "Neutro e elegante": "em neutros chiques 🤍",
    "Preto sempre": "em preto total 🖤"
}

# LÓGICA DE MONTAGEM
def montar_look():
    topo = random.choice(partes_cima[clima])
    base = random.choice(partes_baixo[estilo])
    sapato = random.choice(calçados[calçado_preferido])

    if humor == "Preguiçosa":
        topo = "camiseta oversized"
        base = "moletom estiloso"
    elif humor == "Pronta pra brilhar":
        topo += " com brilho ✨"
    
    if tempo_fora == "O dia inteiro":
        topo += " com sobreposição leve"

    if locomocao in ["A pé", "Transporte público"] and calçado_preferido == "Salto":
        sapato = "tênis confortável"

    acess = []
    if acessorios != "Prefiro evitar":
        acess = random.sample(acessorios_por_estilo[estilo], 1)

    look_texto = f"{topo} + {base} + {sapato} {cores[vibe_cor]}"
    return look_texto, acess

# GERAR LOOK
if st.button("🔮 Me dá meu look!"):
    look, acessorios_escolhidos = montar_look()
    
    st.subheader(f"✅ Look ideal para {ocasião}")
    st.write(f"👉 {look}")
    
    if acessorios_escolhidos:
        st.write("✨ Acessório sugerido: " + ", ".join(acessorios_escolhidos))

    st.write(f"🎯 Estilo: {estilo} | ☁ Clima: {clima} | 🧠 Humor: {humor}")
    st.write(f"🕒 Tempo fora: {tempo_fora} | 🚗 Transporte: {locomocao}")

    # SALVAR LOOK
    if st.checkbox("💾 Quero salvar meu look"):
        buffer = io.StringIO()
        buffer.write("👗 LOOK SALVO\n")
        buffer.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        buffer.write(f"Ocasião: {ocasião}\nEstilo: {estilo}\nClima: {clima}\n")
        buffer.write(f"Look: {look}\n")
        acess_str = ", ".join(acessorios_escolhidos) if acessorios_escolhidos else "Nenhum"
        buffer.write(f"Acessórios: {acess_str}\n")

        st.download_button(
            label="📥 Baixar meu look",
            data=buffer.getvalue(),
            file_name="meu_look.txt",
            mime="text/plain"
        )
import streamlit as st
import google.generativeai as genai
# Título da página
st.set_page_config(page_title="Chat com IA - Gemini", layout="centered")
st.title("💬 Chat com a IA da Google (Gemini)")
# Campo para digitar a API Key
api_key = st.text_input("Digite sua chave da API Gemini", type="password")
# Campo para digitar a pergunta
user_input = st.text_area("Digite sua pergunta:")
# Botão para enviar
if st.button("Enviar"):
   if not api_key:
       st.warning("Por favor, insira sua chave da API.")
   elif not user_input.strip():
       st.warning("Digite algo para a IA responder.")
   else:
       try:
           # Configurar a API com a chave informada
           genai.configure(api_key=api_key)
           # Selecionar o modelo
           model = genai.GenerativeModel("gemini-pro")
           # Fazer a geração
           response = model.generate_content(user_input)
           # Mostrar a resposta
           st.subheader("Resposta da IA:")
           st.write(response.text)
       except Exception as e:
           st.error(f"Erro: {e}")
           import streamlit as st
import google.generativeai as genai
# Título da página
st.set_page_config(page_title="Chat com IA - Gemini", layout="centered")
st.title("💬 Chat com a IA da Google (Gemini)")
# Campo para digitar a API Key
api_key = st.text_input("Digite sua chave da API Gemini", type="password")
# Campo para digitar a pergunta
user_input = st.text_area("Digite sua pergunta:")
# Botão para enviar
if st.button("Enviar"):
   if not api_key:
       st.warning("Por favor, insira sua chave da API.")
   elif not user_input.strip():
       st.warning("Digite algo para a IA responder.")
   else:
       try:
           # Configurar a API com a chave informada
           genai.configure(api_key=api_key)
           # Selecionar o modelo
           model = genai.GenerativeModel("gemini-pro")
           # Fazer a geração
           response = model.generate_content(user_input)
           # Mostrar a resposta
           st.subheader("Resposta da IA:")
           st.write(response.text)
       except Exception as e:
           st.error(f"Erro: {e}")
           import streamlit as st
import google.generativeai as genai
# Título da página
st.set_page_config(page_title="Chat com IA - Gemini", layout="centered")
st.title("💬 Chat com a IA da Google (Gemini)")
# Campo para digitar a API Key
api_key = st.text_input("Digite sua chave da API Gemini", type="password")
# Campo para digitar a pergunta
user_input = st.text_area("Digite sua pergunta:")
# Botão para enviar
if st.button("Enviar"):
   if not api_key:
       st.warning("Por favor, insira sua chave da API.")
   elif not user_input.strip():
       st.warning("Digite algo para a IA responder.")
   else:
       try:
           # Configurar a API com a chave informada
           genai.configure(api_key=api_key)
           # Selecionar o modelo
           model = genai.GenerativeModel("gemini-pro")
           # Fazer a geração
           response = model.generate_content(user_input)
           # Mostrar a resposta
           st.subheader("Resposta da IA:")
           st.write(response.text)
       except Exception as e:
           st.error(f"Erro: {e}")
           import streamlit as st
