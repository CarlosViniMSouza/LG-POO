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

def select_check_ratio_car(bot):
    # Go to 'Car' Forms
    while len(bot.find_elements('//*[@id="checkGasoline"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="checkGasoline"]', By.XPATH).click()
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="submit"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="submit"]', By.XPATH).click()
    bot.wait(1000)

def select_check_ratio_motorcycle(bot):
    # Go to 'Motocycle' Forms
    while len(bot.find_elements('//*[@id="checkCylinder"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="checkCylinder"]', By.XPATH).click()
    bot.wait(1000)

    while len(bot.find_elements('//*[@id="submit"]', By.XPATH))<1:
        bot.wait(2000)

    bot.find_element('//*[@id="submit"]', By.XPATH).click()
    bot.wait(1000)

def fillout_forms_car(bot, forms):
    while len(bot.find_elements('//*[@id="gasoline"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="gasoline"]', By.XPATH).send_keys(forms.type_gasoline)
    bot.wait(1000)

def fillout_forms_motocycle(bot, forms):
    while len(bot.find_elements('//*[@id="cylinder"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="cylinder"]', By.XPATH).send_keys(forms.cc)
    bot.wait(1000)

def submit_vehicle_calc_rent(bot):
    # Add Vehicle
    while len(bot.find_elements('//*[@id="addVehicle"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="addVehicle"]', By.XPATH).click()
    bot.wait(1000)

    # Calculate Rent
    while len(bot.find_elements('//*[@id="calcRent"]', By.XPATH))<1:
        bot.wait(1000)

    bot.find_element('//*[@id="calcRent"]', By.XPATH).click()
    bot.wait(1000)

def save_forms_car(forms):
    # path_home = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_rent_vehicles\resources\forms_vehicles.txt"

    path_lab = r"C:\Users\matutino\Documents\projects\lg-poo\projects\bot_rent_vehicles\resources\forms_car.txt"

    file = open(path_lab, "a")

    file.write(f"Name: {forms.name} \n")
    file.write(f"Year: {forms.year} \n")
    file.write(f"Daily Value: {forms.daily_value} \n")
    file.write(f"Type Gas: {forms.type_gasoline} \n") # to 'Car'
    file.write(f"Rent calculated (without discount): R${forms.calc_total_rental(7, 0)} \n")
    file.write(f"Rent calculated (with 10% discount): R${forms.calc_total_rental(7, 0.1)}")

    file.close()

def save_forms_motorcycle(forms):
        # path_home = r"C:\Users\CarlosViniMSouza\Documents\Projects\LG-POO\projects\bot_rent_vehicles\resources\forms_vehicles.txt"

    path_lab = r"C:\Users\matutino\Documents\projects\lg-poo\projects\bot_rent_vehicles\resources\forms_motorcycle.txt"

    file = open(path_lab, "a")

    file.write(f"Name: {forms.name} \n")
    file.write(f"Year: {forms.year} \n")
    file.write(f"Daily Value: {forms.daily_value} \n")
    file.write(f"Cylinders Cap: {forms.cc} \n") # to 'Motocycle'
    file.write(f"Rent calculated (without discount): R${forms.calc_total_rental(7, 0)} \n")
    file.write(f"Rent calculated (with 10% discount): R${forms.calc_total_rental(7, 0.1)}")

    file.close()
