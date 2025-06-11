import streamlit as st
import random
import io
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Recomendador de Looks", page_icon="👗", layout="centered")
st.title("👗 Recomendador de Looks Personalizado")
st.markdown("Responda algumas perguntas e receba uma sugestão de look com a sua cara!")

# PERGUNTAS
ocasião = st.selectbox("1️⃣ Qual a ocasião?", [ 
    "Faculdade", "Escola", "Shopping", "Date", "Praia",
    "Festa / Balada", "Piquenique", "Museu", "Brunch",
    "Churrasco", "Cinema", "Teatro"
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

foto = st.file_uploader("📷 Quer subir uma foto pra gente entender sua vibe de hoje?", type=["jpg", "jpeg", "png"])

# ACESSÓRIOS POR ESTILO
acessorios_por_estilo = {
    "Básico": ["argolas pequenas", "relógio simples", "bolsa transversal"],
    "Fashionista": ["óculos escuros estilosos", "brincos grandes", "cinto marcante"],
    "Esportivo": ["boné", "mochilinha", "meia alta estilizada"],
    "Romântico": ["tiara ou presilha", "colar delicado", "bolsa de palha"],
    "Despojado": ["pulseira de miçanga", "anel colorido", "bucket hat"]
}

# PALETAS DE CORES
paletas = {
    "Calor": "https://i.pinimg.com/564x/67/ff/4a/67ff4a35439c31ea2ab53d5eb7e5a0ae.jpg",
    "Frio": "https://i.pinimg.com/564x/94/49/ba/9449ba7bcb305108de7bde1e43ff635e.jpg",
    "Ameno": "https://i.pinimg.com/564x/cf/99/41/cf99411b1e4f1b8a456cbbed3dbdc7c7.jpg",
    "Chuvoso": "https://i.pinimg.com/564x/79/23/95/792395b59bc25295a2798029e14f2cb1.jpg"
}

# IMAGENS DE EXEMPLO
imagens_ocasião = {
    "Date": "https://i.pinimg.com/564x/80/6b/ba/806bbad4eec9f2fef0bc646118c6ec2c.jpg",
    "Teatro": "https://i.pinimg.com/564x/57/ef/2c/57ef2c2bfe1a1d23cb9c14850c0131fc.jpg"
}

# SUGESTÕES ESPECIAIS
sugestoes_exclusivas = {
    "Date": "Vestido midi + sandália delicada + bolsa pequena",
    "Teatro": "Macacão elegante + blazer + sapato fechado"
}

# PARTES DE CIMA
partes_de_cima = {
    "Calor": ["Regata soltinha", "Cropped leve", "Blusa ciganinha"],
    "Frio": ["Blusa de lã", "Tricô oversized", "Moletom estiloso"],
    "Ameno": ["Camisa leve", "Blusa de manga longa", "Cardigan fofo"],
    "Chuvoso": ["Capa estilosa", "Jaqueta impermeável", "Blusa com capuz"]
}

# PARTES DE BAIXO
partes_de_baixo = {
    "Básico": ["calça jeans", "short jeans", "legging"],
    "Fashionista": ["calça cargo", "saia midi", "minissaia de couro"],
    "Esportivo": ["short de academia", "calça jogger", "legging com recortes"],
    "Romântico": ["saia rodada", "vestido floral", "short de linho"],
    "Despojado": ["bermuda jeans", "calça rasgada", "short estampado"]
}

# CALÇADOS
calçados_por_estilo = {
    "Tênis": ["tênis branco", "tênis plataforma", "tênis chunky"],
    "Sandália": ["rasteirinha", "sandália plataforma", "sandália de tiras"],
    "Salto": ["salto grosso", "scarpin", "salto bloco confortável"],
    "Bota": ["coturno", "bota cano médio", "bota tratorada"],
    "Tanto faz": ["tênis estiloso", "sandália confortável", "bota leve"]
}

# BOTÃO DE GERAÇÃO
if st.button("🔮 Me dá meu look!"):
    if ocasião in sugestoes_exclusivas:
        look = sugestoes_exclusivas[ocasião]
        imagem_look = imagens_ocasião[ocasião]
    else:
        parte_cima = random.choice(partes_de_cima[clima])
        parte_baixo = random.choice(partes_de_baixo[estilo])
        calcado = random.choice(calçados_por_estilo[calçado_preferido])
        look = f"{parte_cima} + {parte_baixo} + {calcado}"
        imagem_look = None

    st.markdown(f"## ✅ Seu look ideal para *{ocasião}*")
    st.write(f"👗 Sugestão: {look}")
    st.write(f"🎯 Estilo: {estilo} | ☁️ Clima: {clima} | 🧠 Humor: {humor}")
    st.write(f"🕒 Tempo fora: {tempo_fora} | 🚗 Transporte: {locomocao}")
    st.write(f"🎨 Vibe de cor: {vibe_cor}")

    if imagem_look:
        st.image(imagem_look, caption=f"Inspiração para {ocasião}", use_column_width=True)

    if foto:
        st.image(foto, caption="Sua vibe de hoje!", use_column_width=True)

    if acessorios != "Prefiro evitar":
        acessorios_escolhidos = random.sample(acessorios_por_estilo[estilo], 2)
        st.markdown("### ✨ Acessórios que combinam com seu estilo:")
        st.write("• " + "\n• ".join(acessorios_escolhidos))
    else:
        acessorios_escolhidos = []

    st.markdown("### 🎨 Paleta de cores para hoje:")
    st.image(paletas[clima], use_column_width=True)

    # BOTÃO PARA BAIXAR
    if st.checkbox("💾 Quero salvar meu look"):
        buffer = io.StringIO()
        buffer.write("👗 LOOK SALVO\n")
        buffer.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        buffer.write(f"Ocasião: {ocasião}\nEstilo: {estilo}\nClima: {clima}\n")
        buffer.write(f"Look: {look}\n")
        buffer.write(f"Cor: {vibe_cor}\n")
        buffer.write(f"Acessórios: {', '.join(acessorios_escolhidos) if acessorios_escolhidos else 'Nenhum'}\n")
        st.download_button("📥 Baixar meu look", data=buffer.getvalue(), file_name="meu_look.txt", mime="text/plain")
