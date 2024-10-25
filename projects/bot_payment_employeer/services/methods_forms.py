from botcity.core import DesktopBot

bot = DesktopBot()

def fillout_employeer_per_hour(employeer):
    if not bot.find( "label-name-hourly", matching=0.97, waiting_time=10000):
        not_found("label-name-hourly") # type: ignore
    bot.click_relative(110, 4)
    
    bot.kb_type(employeer.get_name())

    if not bot.find( "label-hours-worked", matching=0.97, waiting_time=10000):
        not_found("label-hours-worked") # type: ignore
    bot.click_relative(123, 6)
    
    bot.kb_type(str(employeer.get_hours_worked()))
    
    if not bot.find( "label-value-hour", matching=0.97, waiting_time=10000):
        not_found("label-value-hour") # type: ignore
    bot.click_relative(107, 6)
    
    bot.kb_type(str(employeer.get_value_hour()))
    
    if not bot.find( "button-add-hourist", matching=0.97, waiting_time=10000):
        not_found("button-add-hourist") # type: ignore
    bot.click()
    
    if not bot.find( "button-ok-hourly", matching=0.97, waiting_time=10000):
        not_found("button-ok-hourly") # type: ignore
    bot.click()
    

def fillout_employeer_salary(employeer):
    if not bot.find( "label-name-montly", matching=0.97, waiting_time=10000):
        not_found("label-name-montly") # type: ignore
    bot.click_relative(122, 6)
    
    bot.kb_type(employeer.get_name())
    
    if not bot.find( "label-montly-salary", matching=0.97, waiting_time=10000):
        not_found("label-montly-salary") # type: ignore
    bot.click_relative(113, 5)
    
    bot.kb_type(str(employeer.get_montly_salary()))

    if not bot.find( "button-add-montly", matching=0.97, waiting_time=10000):
        not_found("button-add-montly") # type: ignore
    bot.click()
    
    if not bot.find( "button-ok-montly", matching=0.97, waiting_time=10000):
        not_found("button-ok-montly") # type: ignore
    bot.click()

def fillout_employeer_commissioned(employeer):
    if not bot.find( "label-name-commissioned", matching=0.97, waiting_time=10000):
        not_found("label-name-commissioned") # type: ignore
    bot.click_relative(131, 5)
    
    bot.kb_type(employeer.get_name())
    
    if not bot.find( "label-sales", matching=0.97, waiting_time=10000):
        not_found("label-sales") # type: ignore
    bot.click_relative(96, 4)
    
    bot.kb_type(str(employeer.get_sales()))
    
    if not bot.find( "label-commission", matching=0.97, waiting_time=10000):
        not_found("label-commission") # type: ignore
    bot.click_relative(103, 4)
    
    bot.kb_type(str(employeer.get_commision_rate()))
    
    if not bot.find( "button-add-commissioned", matching=0.97, waiting_time=10000):
        not_found("button-add-commissioned") # type: ignore
    bot.click()
    
    if not bot.find( "button-ok-commissioned", matching=0.97, waiting_time=10000):
        not_found("button-ok-commissioned") # type: ignore
    bot.click()
    
    if not bot.find( "button-show-salaries", matching=0.97, waiting_time=10000):
        not_found("button-show-salaries") # type: ignore
    bot.click()
    



