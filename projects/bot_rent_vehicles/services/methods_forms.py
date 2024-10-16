from botcity.web import By

def fillout_forms_base(bot, forms):
    while len(bot.find_elements('//*[@id="name"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="name"]', By.XPATH).send_keys(forms.name)
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="year"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="year"]', By.XPATH).send_keys(forms.year)
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="dailyvalue"]', By.XPATH))<1:
        bot.wait(1000)
    
    bot.find_element('//*[@id="dailyvalue"]', By.XPATH).send_keys(forms.daily_value)
    bot.wait(1000)

    # Go to 'Car' Forms
    while len(bot.find_elements('//*[@id="submitcar"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="submitcar"]', By.XPATH).click()
    bot.wait(1000)

    # Go to 'Motocycle' Forms
    while len(bot.find_elements('//*[@id="submitbike"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="submitbike"]', By.XPATH).click()
    bot.wait(1000)

def fillout_forms_car(bot, forms):
    while len(bot.find_elements('//*[@id="gasoline"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="gasoline"]', By.XPATH).send_keys(forms.type_gasoline)
    bot.wait(1000)

    # Submit Forms
    while len(bot.find_elements('//*[@id="finish"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="finish"]', By.XPATH).click()
    bot.wait(1000)

def fillout_forms_motocycle(bot, forms):
    while len(bot.find_elements('//*[@id="cylinder"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="cylinder"]', By.XPATH).send_keys(forms.cc)
    bot.wait(1000)

    # Submit Forms
    while len(bot.find_elements('//*[@id="finish"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="finish"]', By.XPATH).click()
    bot.wait(1000)

def save_forms(forms):
    # path_home = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_rent_vehicles\resources\forms_vehicles.txt"

    path_lab = r"C:\Users\matutino\Documents\projects\lg-poo\projects\bot_rent_vehicles\resources\forms_vehicles.txt"

    file = open(path_lab, "a")

    file.write(f"Name: {forms.name} \n")
    file.write(f"Year: {forms.year} \n")
    file.write(f"Daily Value: {forms.daily_value} \n")
    # file.write(f"Type Gas: {forms.type_gasoline} \n\n") # to 'Car'
    file.write(f"Cylinders: {forms.cc} \n\n") # to 'Motocycle'

    file.close()
