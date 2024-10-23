from botcity.web import By

def fillout_forms_base(bot, forms):
    while len(bot.find_elements('//*[@id="book-name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="book-name"]', By.XPATH).send_keys(forms.get_title())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="author-name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="author-name"]', By.XPATH).send_keys(forms.get_author())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="code-book"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="code-book"]', By.XPATH).send_keys(forms.get_code())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="submit"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="submit"]', By.XPATH).click()
    bot.wait(1000)