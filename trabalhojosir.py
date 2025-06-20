import streamlit as st
import random
import io
from datetime import datetime

# Configuração geral da página
st.set_page_config(page_title="Recomendador de Looks", page_icon="👗", layout="centered")

st.title("👗 Recomendador de Looks Personalizado")
st.markdown("Responda algumas perguntas e receba uma sugestão de look que combine perfeitamente com você!")

# Perguntas do formulário
ocasiao = st.selectbox("1️⃣ Qual a ocasião?", [
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

calcado_preferido = st.radio("7️⃣ Tem preferência de calçado?", [
    "Tênis", "Sandália", "Salto", "Bota", "Tanto faz"
])

vibe_cor = st.radio("8️⃣ Prefere algo mais colorido ou neutro?", [
    "Coloridão", "Tons pastéis", "Neutro e elegante", "Preto sempre"
])

acessorios = st.radio("9️⃣ Curte usar acessórios?", [
    "Sim, amo!", "Apenas alguns", "Prefiro evitar"
])

# Banco de dados das peças
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

calcados = {
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

def montar_look():
    aviso = ""

    # Bloqueio de combinações incoerentes
    if clima in ["Chuvoso", "Frio"] and calcado_preferido == "Sandália":
        aviso += "🚫 Sandália não é ideal para clima frio ou chuvoso. Substituindo por bota.\n"
        calcado_escolhido = "Bota"
    elif calcado_preferido == "Salto" and locomocao in ["A pé", "Transporte público"] and clima in ["Chuvoso", "Frio"]:
        aviso += "🚫 Salto em clima ruim e locomoção a pé/transporte público não é ideal. Substituindo por tênis confortável.\n"
        calcado_escolhido = "Tênis"
    else:
        calcado_escolhido = calcado_preferido

    # Parte de cima baseada no clima
    topo = random.choice(partes_cima[clima])

    # Parte de baixo baseada em estilo + clima
    if clima == "Frio":
        if estilo == "Romântico":
            base = "saia longa com meia-calça"
        elif estilo == "Esportivo":
            base = "legging térmica"
        else:
            base = "calça estilosa de inverno"
    elif clima == "Chuvoso":
        base = "calça prática e impermeável"
    elif clima == "Calor":
        base = random.choice([item for item in partes_baixo[estilo] if any(k in item for k in ["short", "saia", "vestido"])])
    else:
        base = random.choice(partes_baixo[estilo])

    # Calçado final
    if calcado_escolhido == "Salto" and locomocao in ["A pé", "Transporte público"]:
        sapato = "tênis confortável"
    else:
        sapato = random.choice(calcados[calcado_escolhido])

    # Ajustes por humor
    if humor == "Preguiçosa":
        topo = "camiseta oversized"
        base = "calça ou short de moletom"
    elif humor == "Pronta pra brilhar":
        topo += " com brilho ✨"

    # Sobreposição se o dia for longo
    if tempo_fora == "O dia inteiro":
        topo += " com sobreposição leve"

    # Acessórios opcionais
    acess = []
    if acessorios != "Prefiro evitar":
        acess = random.sample(acessorios_por_estilo[estilo], 1)

    look_texto = f"{topo} + {base} + {sapato} {cores[vibe_cor]}"
    return look_texto, acess, aviso

if st.button("🔮 Me dá meu look!"):
    look, acessorios_escolhidos, alerta = montar_look()

    st.subheader(f"✅ Look ideal para {ocasiao}")
    st.write(f"👉 {look}")

    if acessorios_escolhidos:
        st.write("✨ Acessório sugerido: " + ", ".join(acessorios_escolhidos))

    st.write(f"🎯 Estilo: {estilo} | ☁ Clima: {clima} | 🧠 Humor: {humor}")
    st.write(f"🕒 Tempo fora: {tempo_fora} | 🚗 Transporte: {locomocao}")

    if alerta:
        st.warning(alerta.strip())

    if st.checkbox("💾 Quero salvar meu look"):
        buffer = io.StringIO()
        buffer.write("👗 LOOK SALVO\n")
        buffer.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        buffer.write(f"Ocasião: {ocasiao}\nEstilo: {estilo}\nClima: {clima}\n")
        buffer.write(f"Look: {look}\n")
        acess_str = ", ".join(acessorios_escolhidos) if acessorios_escolhidos else "Nenhum"
        buffer.write(f"Acessórios: {acess_str}\n")

        st.download_button(
            label="📥 Baixar meu look",
            data=buffer.getvalue(),
            file_name="meu_look.txt",
            mime="text/plain"
        )



