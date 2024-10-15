from botcity.plugins.http import BotHttpPlugin
from botcity.web import WebBot, Browser, By

def fillout_forms_base(bot, forms):
    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(forms.show_infos_name())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="email"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(forms.show_infos_email())
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="password"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="password"]', By.XPATH).send_keys(forms.show_infos_password())
    bot.wait(1000)

    bot.enter()

def fillout_forms_contact(bot, forms):
    while len(bot.find_elements('//*[@id="contact"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="contact"]', By.XPATH).send_keys(forms.show_infos_contact())
    bot.wait(1000)

    bot.enter()

def fillout_forms_login(bot, forms):
    while len(bot.find_elements('//*[@id="login"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="login"]', By.XPATH).send_keys(forms.show_infos_login())
    bot.wait(1000)

    bot.enter()

def save_forms(forms_complete):
    # Open a file in append mode
    file = open(r"C:\Users\matutino\Documents\projects\lg-poo\projects\bot_multiples_forms\resources\forms_complete.txt", "a")

    # Append some text to the file
    file.write("Name: " + forms_complete.show_infos_name() + "\n")
    file.write("Email: " + forms_complete.show_infos_email() + "\n")
    file.write("Password: " + forms_complete.show_infos_password() + "\n")
    file.write("Contact: " + forms_complete.show_infos_contact() + "\n")
    file.write("Login: " + forms_complete.show_infos_login() + "\n")

    # Close the file
    file.close()
