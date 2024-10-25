from botcity.web import By

def fillout_forms_base(bot, forms):
    bot.browse("http://127.0.0.1:3000/projects/bot_forms_poli/web/forms_base.html")

    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(forms.get_name())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="login"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(forms.get_login())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="email"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(forms.get_email())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="password"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="password"]', By.XPATH).send_keys(forms.get_password())
    bot.wait(1000)

def fillout_forms_cadastro(bot, forms):
    bot.browse("http://127.0.0.1:3000/projects/bot_forms_poli/web/forms_cadastro.html")

    while len(bot.find_elements('//*[@id="login"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(forms.get_login())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="password"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="password"]', By.XPATH).send_keys(forms.get_password())
    bot.wait(1000)

def fillout_forms_atualizar(bot, forms):
    bot.browse("http://127.0.0.1:3000/projects/bot_forms_poli/web/forms_atualizar.html")

    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(forms.get_name())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="login"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(forms.get_login())
    bot.wait(1000)
