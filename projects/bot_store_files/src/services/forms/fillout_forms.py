from botcity.web import By

def fillout_forms(bot, forms):
    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(forms.get_name())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="price"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="price"]', By.XPATH).send_keys(str(forms.get_price()))
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="category"]', By.XPATH))<1:
        bot.wait(1000)
    
    bot.find_element('//*[@id="category"]', By.XPATH).send_keys(forms.get_category())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="submit"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="submit"]', By.XPATH).click()
    bot.wait(1000)
