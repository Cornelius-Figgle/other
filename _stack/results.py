# somewhere near the top of your code (global namespace)
previous_results = {}  # creates the dictionary

def send_to_telegram(message):

    apiToken = 'xxxxx'
    chatID = '-xxxx'
    bot = telebot.TeleBot(apiToken)

    if placa and fabricante_1 in marca:
        # if the results are different
        if previous_results['marca'] != marca or previous_results['fabricante_1'] != fabricante_1 or previous_results['valor_preco_avista'] != valor_preco_avista or previous_results['loja'] != loja or previous_results['url_completa'] != url_completa:
            # updates dictionary 
            previous_results['marca'] = marca
            previous_results['fabricante_1'] = fabricante_1
            previous_results['valor_preco_avista'] = valor_preco_avista
            previous_results['loja'] = loja
            previous_results['url_completa'] = url_completa

            # sends message to Telegram
            bot.send_message(
                chat_id=chatID, text=f"<b>Modelo:</b> {marca} \n<b>Fabricante:</b> {fabricante_1}\n<b>Preço a vista:</b> R$ {valor_preco_avista} \n<b>Preço a prazo:</b> R$ {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<b>Link Produto:</b> {url_completa}", parse_mode='HTML')
        else:
            pass
            # could log a "found same item" or something here
            # if you wanted to

# ---------------------------------------------------------------------

# somewhere near the top of your code (global namespace)
previous_results = {}  # creates the dictionary

def send_to_telegram(message):

    apiToken = 'xxxxx'
    chatID = '-xxxx'
    bot = telebot.TeleBot(apiToken)

    if placa and fabricante_1 in marca:
        # if the results are different
        if (previous_results['marca'] != marca
            or previous_results['fabricante_1'] != fabricante_1
            or previous_results['valor_preco_avista'] != valor_preco_avista
            or previous_results['loja'] != loja
            or previous_results['url_completa'] != url_completa):

            # updates dictionary 
            previous_results['marca'] = marca
            previous_results['fabricante_1'] = fabricante_1
            previous_results['valor_preco_avista'] = valor_preco_avista
            previous_results['loja'] = loja
            previous_results['url_completa'] = url_completa

            # sends message to Telegram
            bot.send_message(
                chat_id=chatID,
                text=f"<b>Modelo:</b> {marca} \n<b>Fabricante:</b> {fabricante_1}\n<b>Preço a vista:</b> R$ {valor_preco_avista} \n<b>Preço a prazo:</b> R$ {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<b>Link Produto:</b> {url_completa}",
                parse_mode='HTML'
            )
        else:
            pass
            # could log a "found same item" or something here
            # if you wanted to

# ---------------------------------------------------------------------

# somewhere near the top of your code (global namespace)
previous_results = {}  # creates the dictionary

def send_to_telegram(message):

    apiToken = 'xxxxx'
    chatID = '-xxxx'
    bot = telebot.TeleBot(apiToken)

    if placa and fabricante_1 in marca:
        # clears working dictionary
        current_results = {}

        # add values to dictionary
        for key, value in previous_results.items():
            current_results[key] = exec(key)

        # loop over results in dictionary
        for key, value in current_results.items():
            if value != previous_results[key]:
                # if value different, update dictionary
                previous_results[key] = value
            else:
                pass
                # could log a "found same item" or something here if you wanted to

        # sends message to Telegram
        bot.send_message(
            chat_id=chatID,
            text=f"<b>Modelo:</b> {marca} \n<b>Fabricante:</b> {fabricante_1}\n<b>Preço a vista:</b> R$ {valor_preco_avista} \n<b>Preço a prazo:</b> R$ {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<b>Link Produto:</b> {url_completa}",
            parse_mode='HTML'
        )
        
# ---------------------------------------------------------------------

# somewhere near the top of your code (global namespace)
previous_results = []  # creates the list of dictionaries

def send_to_telegram(message):

    apiToken = 'xxxxx'
    chatID = '-xxxx'
    bot = telebot.TeleBot(apiToken)

    if placa and fabricante_1 in marca:
        # clears working dictionary
        current_results = {}
        working_results = {}

        # loop over results in dictionary
        for key, value in current_results.items():
            if value != previous_results[key]:
                # if value different, update dictionary
                working_results[key] = value
            else:
                pass
                # could log a "found same item" or something here if you wanted to

        # sends message to Telegram
        bot.send_message(
            chat_id=chatID,
            text=f"<b>Modelo:</b> {marca} \n<b>Fabricante:</b> {fabricante_1}\n<b>Preço a vista:</b> R$ {valor_preco_avista} \n<b>Preço a prazo:</b> R$ {valor_preco_prazo} \n<b>Loja:</b> {loja} \n\n<b>Link Produto:</b> {url_completa}",
            parse_mode='HTML'
        )