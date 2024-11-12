import time
import telebot
import random
import google.generativeai as genai

CHAVE_API_IA = "AIzaSyDnCaK5RsrmG7T8IU8vY5E845WQ5a6daB8"
genai.configure(api_key=CHAVE_API_IA)

# Inicializa o modelo do Gemini
model = genai.GenerativeModel('gemini-pro')

CHAVE_API = "7905790394:AAH7mCUaA9SoR07gpfnsvbSM4ZJirPXJHvU"
bot = telebot.TeleBot(CHAVE_API)

# Função para gerar conteúdo com o modelo Gemini
def gerar_conteudo(mensagem_texto, mensagem):
    # Envia a mensagem de "digitando..." antes de gerar a resposta
    bot.send_chat_action(mensagem.chat.id, 'typing')
    bot.reply_to(mensagem, "Digitando...")  # Exibe a mensagem de "digitando..."
    time.sleep(0.5)  # Adiciona um pequeno delay para mostrar a ação de "digitando"
    response = model.generate_content(mensagem_texto)
    conteudo = response.text

    # Verifica se o conteúdo excede o limite de 4096 caracteres
    while len(conteudo) > 4096:
        # Envia a parte do conteúdo dentro do limite e atualiza o conteúdo com o restante
        bot.reply_to(mensagem, conteudo[:4096])
        conteudo = conteudo[4096:]

    # Envia o restante do conteúdo
    # bot.reply_to(mensagem, conteudo)
    return conteudo

# Função para enviar a primeira lista de opções para iniciar o bot
def enviar_opcoes_iniciais(mensagem):
    texto = """
    Escolha uma das opções para continuar:
    1: Trilha de estudos para o ENEM;
    2: Exercícios para o ENEM;
    3: Exercícios de Linguagens, Códigos e suas Tecnologias;
    4: Exercícios de Ciências Humanas e suas Tecnologias;
    5: Exercícios de Ciências da Natureza e suas Tecnologias;
    6: Exercícios de Matemática e suas Tecnologias;
    """
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(0.5)
    bot.reply_to(mensagem, texto)

# Função para enviar a segunda lista de opções para continuar escolhendo
def enviar_opcoes_continuacao(mensagem):
    texto = """
    Deseja selecionar mais uma opção?
    1: Trilha de estudos para o ENEM;
    2: Exercícios para o ENEM;
    3: Exercícios de Linguagens, Códigos e suas Tecnologias;
    4: Exercícios de Ciências Humanas e suas Tecnologias;
    5: Exercícios de Ciências da Natureza e suas Tecnologias;
    6: Exercícios de Matemática e suas Tecnologias;
    """
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(0.5)
    bot.reply_to(mensagem, texto)

# Funções de resposta para cada opção, usando a lista de opções de continuação ao final
@bot.message_handler(func=lambda mensagem: mensagem.text == "1")
def opcao_1(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora gostaria de receber uma trilha de estudos completa para me preparar para o ENEM...", mensagem)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Aqui está a trilha de estudos para o ENEM! Organizada especialmente para te guiar. Qualquer dúvida, estarei por aqui.")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

@bot.message_handler(func=lambda mensagem: mensagem.text == "2")
def opcao_2(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora por favor, me forneça 3 questões de provas anteriores do ENEM...")
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Encontrei alguns exercícios para você treinar. Espero que ajudem no seu preparo!")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

@bot.message_handler(func=lambda mensagem: mensagem.text == "3")
def opcao_3(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora por favor, me forneça questões de provas anteriores do ENEM para o seguinte assunto: Linguagens...", mensagem)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Essas questões de Linguagens vão te ajudar a praticar. Aproveite e bons estudos!")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

@bot.message_handler(func=lambda mensagem: mensagem.text == "4")
def opcao_4(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora por favor, me forneça questões de provas anteriores do ENEM para o seguinte assunto: Ciências Humanas...", mensagem)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Aqui estão algumas questões de Ciências Humanas para você praticar. Boa sorte!")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

@bot.message_handler(func=lambda mensagem: mensagem.text == "5")
def opcao_5(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora por favor, me forneça questões de provas anteriores do ENEM para o seguinte assunto: Ciências da Natureza...", mensagem)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Essas questões de Ciências da Natureza vão ajudar bastante no seu estudo!")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

@bot.message_handler(func=lambda mensagem: mensagem.text == "6")
def opcao_6(mensagem):
    conteudo = gerar_conteudo("Obrigado! Agora por favor, me forneça questões de provas anteriores do ENEM para o seguinte assunto: Matemática...", mensagem)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(1)
    bot.reply_to(mensagem, "Essas questões de Matemática são ótimas para você praticar. Bons estudos!")
    bot.reply_to(mensagem, conteudo)
    enviar_opcoes_continuacao(mensagem)

# Lista de saudações aleatórias
saudacoes = [
    "E aí, {nome}! Tudo bem? Em que posso te ajudar?",
    "Oi, {nome}! Estou aqui para ajudar com seus estudos para o ENEM!",
    "Olá, {nome}! Vamos estudar? Escolha uma das opções abaixo:",
    "Opa, {nome}! Vamos lá! Como posso te ajudar hoje?"
]


# Aqui você adiciona a função de resposta a "mais questões" ou "mais conteúdo"
@bot.message_handler(func=lambda mensagem: 'tem mais questões' in mensagem.text.lower() or 'tem mais conteúdo' in mensagem.text.lower() or 'tem mais conteudo' in mensagem.text.lower() or 'tem mais questoes' in mensagem.text.lower() or 'manda mais questoes' in mensagem.text.lower() or 'manda mais conteúdo' in mensagem.text.lower() or 'manda mais conteudo' in mensagem.text.lower() or 'manda mais questões' in mensagem.text.lower())
def responder_mais_questoes(mensagem):
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(0.5)
    bot.reply_to(mensagem, "Opa, sim! Claro, posso te ajudar com mais questões!")
    
    # Envia as opções para continuar escolhendo
    enviar_opcoes_continuacao(mensagem)


# Aqui você adiciona a função de resposta a "mais questões" ou "mais conteúdo"
@bot.message_handler(func=lambda mensagem: 'tem mais conteudos' in mensagem.text.lower() or 'tem mais conteúdos' in mensagem.text.lower() or 'tem mais assunto?' in mensagem.text.lower() or 'tem mais coisas' in mensagem.text.lower() or 'há outras coisas' in mensagem.text.lower() or 'so tem isso de assunto' in mensagem.text.lower() or 'so tem isso de assunto?' in mensagem.text.lower() or 'só tem isso de conteúdo' in mensagem.text.lower() or 'só tem isso de conteúdo?' in mensagem.text.lower() or 'só isso' in mensagem.text.lower() or 'tem mais planos para mim' in mensagem.text.lower())
def responder_mais_questoes(mensagem):
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(0.5)
    bot.reply_to(mensagem, "Opa, no momento estamos trabalhando em novos planos de estudos para te ajudar com mais questões e treinamentos!")
    
    # Envia as opções para continuar escolhendo
    enviar_opcoes_continuacao(mensagem)


# Função para enviar uma saudação personalizada
def enviar_saudacao(mensagem):
    nome = mensagem.from_user.first_name
    saudacao = random.choice(saudacoes).format(nome=nome)
    bot.send_chat_action(mensagem.chat.id, 'typing')
    time.sleep(0.5)
    bot.reply_to(mensagem, saudacao)
    
    # Envia as opções iniciais
    enviar_opcoes_iniciais(mensagem)

# Handler para responder com a saudação e a primeira lista de opções
@bot.message_handler(commands=['start', 'iniciar'])
def iniciar_conversa(mensagem):
    enviar_saudacao(mensagem)

# Não há mais necessidade de um handler para "não compreendido", pois o bot vai responder a qualquer saudação
# O bot sempre responderá às mensagens com uma saudação personalizada e com as opções iniciais.

# Inicia o polling para o bot começar a escutar as mensagens
bot.polling()
