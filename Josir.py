from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
      {
        "role": "system",
        "content": "Voce é um programa de recomendação de looks \n\n\nAs perguntas feitas para o usuario serão essas e essas são as opçoes de respostas \n\nQual a ocasião?\nFaculdade\nShopping\nDate\nPraia\nFesta / Balada\nMuseu\nBrunch\nChurrasco\nCinema\nTeatro\n\n Qual estilo você prefere?\nBásico\nFashionista\nEsportivo\nRomântico\nDespojado\n\n Como está o clima hoje?\nCalor\nFrio\nAmeno\nChuvoso\n\n\n Como você está se sentindo hoje?\nConfiante\nNa dúvida\nPreguiçosa\nQuieta e estilosa\nPronta pra brilhar\n\n Vai passar quanto tempo fora de casa?\nO dia inteiro\nSó algumas horinhas\nNão sei ainda\n\n Vai como?\nA pé\nTransporte público\nDe carro\nMoto\n\nTem preferência de calçado?\nTênis\nSandália\nSalto\nBota\nTanto faz\n\n Prefere algo mais colorido ou neutro?\nColoridão\nTons pastéis\nNeutro e elegante\nPreto sempre\n\nCurte usar acessórios?\nSim, amo!\nApenas alguns\nPrefiro evitar"
      },
      {
        "role": "user",
        "content": ""
      },
      {
        "role": "assistant",
        "content": "Estou aqui para te ajudar a escolher um look incrível!\n\nVamos começar! Por favor, responda às perguntas:\n\n1. **Qual a ocasião?**\n - Faculdade\n- Shopping\n- Date\n- Praia\n- Festa / Balada\n- Museu\n- Brunch\n- Churrasco\n- Cinema\n- Teatro\n\n2. **Qual estilo você prefere?**\n - Básico\n- Fashionista\n- Esportivo\n- Romântico\n- Despojado\n\n3. **Como está o clima hoje?**\n - Calor\n- Frio\n- Ameno\n- Chuvoso\n\n4. **Como você está se sentindo hoje?**\n - Confiante\n- Na dúvida\n- Preguiçosa\n- Quieta e estilosa\n- Pronta pra brilhar\n\n5. **Vai passar quanto tempo fora de casa?**\n - O dia inteiro\n- Só algumas horinhas\n- Não sei ainda\n\n6. **Vai como?**\n - A pé\n- Transporte público\n- De carro\n- Moto\n\n7. **Tem preferência de calçado?**\n - Tênis\n- Sandália\n- Salto\n- Bota\n- Tanto faz\n\n8. **Prefere algo mais colorido ou neutro?**\n - Coloridão\n- Tons pastéis\n- Neutro e elegante\n- Preto sempre\n\n9. **Curte usar acessórios?**\n - Sim, amo!\n- Apenas alguns\n- Prefiro evitar\n\nPor favor, responda com o número da sua escolha para cada pergunta!"
      },
      {
        "role": "user",
        "content": "Faculdade,  basico, frio, preguiçosa, so algumas horinhas, moto, tenis, preto sempre, sim"
      },
      {
        "role": "assistant",
        "content": "Com base nas suas respostas, aqui vai uma sugestão de look para você:\n\n**Look Sugerido:**\n\n* **Roupas:**\n + Uma blusa ou camiseta simples de manga longa, preferencialmente em tons neutros ou pretos (já que você gosta de preto sempre).\n + Uma calça jeans ou legging confortável e básica, ideal para um dia de faculdade e para pilotar uma moto.\n* **Calçado:**\n + Um par de tênis confortável e preto, que combine com o seu estilo básico e preferido.\n* **Acessórios:**\n + Um relógio simples e elegante, que seja fácil de usar e não atrapalhe enquanto você estiver pilotando a moto.\n + Um colar simples ou uma pulseira discreta, já que você gosta de usar acessórios, mas de forma moderada.\n* **Maquiagem e Cabelo:**\n + Uma maquiagem leve e natural, que não exija muito esforço (já que você está se sentindo preguiçosa).\n + O cabelo pode estar solto e um pouco desalinhado, ou preso em um coque baixo e simples.\n\n**Dicas:**\n\n* Como está fazendo frio, você pode adicionar uma jaqueta ou um casaco leve sobre a blusa para se manter aquecida.\n* Certifique-se de que as roupas sejam confortáveis e não atrapalhem enquanto você estiver pilotando a moto.\n* Se você quiser adicionar um toque de cor ao look, pode usar um lenço ou uma echarpe simples em um tom neutro.\n\nEspero que esse look sugerido seja do seu agrado! Se tiver alguma dúvida ou precisar de mais ajuda, basta perguntar."
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
