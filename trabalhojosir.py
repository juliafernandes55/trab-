import streamlit as st
import random
import io
from datetime import datetime

st.set_page_config(page_title="Recomendador de Looks", page_icon="👗", layout="centered")

st.title("👗 Recomendador de Looks Personalizado")
st.markdown("Responda algumas perguntas e receba uma sugestão de look que combine perfeitamente com você!")

# -------- PERGUNTAS --------
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

# -------- BANCOS DE PEÇAS --------
partes_cima = {
    "Calor": ["regata soltinha", "cropped leve", "top de alça"],
    "Frio": ["suéter quentinho", "blusa de gola alta", "casaco peluciado"],
    "Ameno": ["camisa de linho", "blusa de manga longa", "cardigan leve"],
    "Chuvoso": ["jaqueta impermeável", "anorak estiloso", "blusa com capuz"]
}

partes_baixo = {
    "Básico": ["jeans reto", "calça legging", "short jeans"],
    "Fashionista": ["calça cargo", "minissaia de couro", "saia midi estilosa"],
    "Esportivo": ["short de treino", "calça jogger", "legging de academia"],
    "Romântico": ["saia evasê", "vestido floral", "short de linho"],
    "Despojado": ["calça rasgada", "bermuda jeans", "short estampado"]
}

calcados = {
    "Tênis": ["tênis branco", "tênis esportivo", "tênis plataforma"],
    "Sandália": ["rasteirinha", "sandália plataforma", "sandália tiras finas"],
    "Salto": ["salto grosso", "salto bloco", "scarpin moderno"],
    "Bota": ["coturno", "bota cano curto", "bota tratorada"],
    "Tanto faz": ["tênis estiloso", "bota leve", "sandália confortável"]
}

acessorios_por_estilo = {
    "Básico": ["mochila pequena", "relógio clean"],
    "Fashionista": ["óculos escuros estilosos", "bolsa fashion"],
    "Esportivo": ["boné esportivo", "pochete"],
    "Romântico": ["colarzinho delicado", "tiara fofa"],
    "Despojado": ["bucket hat", "colar com pingente divertido"]
}

cores = {
    "Coloridão": "em cores vibrantes 🌈",
    "Tons pastéis": "em tons suaves 💗",
    "Neutro e elegante": "em neutros chiques 🤍",
    "Preto sempre": "em preto total 🖤"
}

# -------- FUNÇÃO PRINCIPAL --------
def montar_look():
    alerta = ""
    # Substituições por incoerência
    if clima in ["Frio", "Chuvoso"] and calcado_preferido == "Sandália":
        alerta += "🚫 Sandália não combina com frio ou chuva. Substituímos por bota.\n"
        calcado_final = "Bota"
    elif calcado_preferido == "Salto" and locomocao in ["A pé", "Transporte público"] and clima in ["Frio", "Chuvoso"]:
        alerta += "🚫 Salto com chuva e a pé não rola. Substituímos por tênis confortável.\n"
        calcado_final = "Tênis"
    else:
        calcado_final = calcado_preferido

    # Parte de cima
    topo = random.choice(partes_cima[clima])

    # Parte de baixo coerente
    if clima == "Frio":
        base = "calça quente ou saia com meia-calça"
    elif clima == "Chuvoso":
        base = "calça impermeável ou jeans resistente"
    elif clima == "Calor":
        base = random.choice([b for b in partes_baixo[estilo] if "short" in b or "saia" in b or "vestido" in b])
    else:
        base = random.choice(partes_baixo[estilo])

    # Calçado final
    sapato = random.choice(calcados[calcado_final])

    # Ajustes por humor
    if humor == "Preguiçosa":
        topo = "camiseta oversized"
        base = "calça de moletom ou bermuda confortável"
    elif humor == "Pronta pra brilhar":
        topo += " com brilho ✨"

    # Sobreposição
    if tempo_fora == "O dia inteiro":
        topo += " + sobreposição prática"

    # Acessórios
    acess = []
    if acessorios != "Prefiro evitar":
        acess = random.sample(acessorios_por_estilo[estilo], 1)

    look = f"{topo} + {base} + {sapato} {cores[vibe_cor]}"
    return look, acess, alerta

# -------- EXECUÇÃO --------
if st.button("🔮 Me dá meu look!"):
    look, acessorios_sugeridos, aviso = montar_look()

    st.subheader(f"✅ Look ideal para {ocasiao}")
    st.write(f"👉 {look}")
    if acessorios_sugeridos:
        st.write(f"✨ Acessório sugerido: {', '.join(acessorios_sugeridos)}")

    st.write(f"🎯 Estilo: {estilo} | ☁ Clima: {clima} | 🧠 Humor: {humor}")
    st.write(f"🕒 Tempo fora: {tempo_fora} | 🚗 Transporte: {locomocao}")

    if aviso:
        st.warning(aviso.strip())

    if st.checkbox("💾 Quero salvar meu look"):
        buffer = io.StringIO()
        buffer.write("👗 LOOK SALVO\n")
        buffer.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        buffer.write(f"Ocasião: {ocasiao}\nEstilo: {estilo}\nClima: {clima}\n")
        buffer.write(f"Look: {look}\n")
        acess_str = ", ".join(acessorios_sugeridos) if acessorios_sugeridos else "Nenhum"
        buffer.write(f"Acessórios: {acess_str}\n")

        st.download_button(
            label="📥 Baixar meu look",
            data=buffer.getvalue(),
            file_name="meu_look.txt",
            mime="text/plain"
        )




