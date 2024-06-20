import telebot
TOKEN = '7362652950:AAHalGrS1vq1fq19nhAhKVS-ied--2cUHaM'
LINK_LIBERAR_ACESSO = 'https://bit.ly/LiberarAcessoVip'
ADMIN_CHAT_ID = '@IgorArgent'

bot = telebot.TeleBot(TOKEN)

# Mensagem de boas-vindas que será usada para responder
WELCOME_MESSAGE = (
    'Olá! seja bem vindo ao Pro Tipster.' +  'Use o comando /LiberarAcesso para Liberar o seu acesso ao grupo vip.'
)

# Função que será chamada quando o comando /start for enviado
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, WELCOME_MESSAGE)

# Função que será chamada quando o comando /criarconta for enviado
@bot.message_handler(commands=['LiberarAcesso'])
def LiberarAcesso(message):
    mensagem = (
        "Para Liberar o seu acesso, por favor, siga as instruções abaixo:\n\n"
        "1. Acesse o seguinte link: {}\n\n"
        "2. Preencha os dados necessários.\n\n"
        "3. Confirme seu cadastro, e faça um depósito mínimo de R$30,00. pra que a conta seja considerada uma CONTA ATIVA\n\n"  
        "Após criar a conta, mande o comprovante para @IgorArgent para receber acesso ao grupo VIP.\n"
    ).format(LINK_LIBERAR_ACESSO)

    bot.reply_to(message, mensagem)



# Função que será chamada para todas as outras mensagens
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, WELCOME_MESSAGE)

# Iniciar o bot e manter funcionando
bot.polling(none_stop=True, interval=0)
