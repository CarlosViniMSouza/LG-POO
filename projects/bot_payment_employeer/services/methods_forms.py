from botcity.core import DesktopBot

bot = DesktopBot()

def fillout_windows(employeer):
    if not bot.find( "label-name-employeer", matching=0.97, waiting_time=10000):
        not_found("label-name-employeer") # type: ignore
    bot.click_relative(135, 9)

    bot.kb_type(employeer.get_name())

    if not bot.find( "label-montly-salary", matching=0.97, waiting_time=10000):
        not_found("label-montly-salary") # type: ignore
    bot.click_relative(132, 7)
    
    bot.kb_type(str(employeer.get_montly_salary()))
    
    if not bot.find( "button-add-employeer", matching=0.97, waiting_time=10000):
        not_found("button-add-employeer") # type: ignore
    bot.click()
    
    if not bot.find( "button-process-payment", matching=0.97, waiting_time=10000):
        not_found("button-process-payment") # type: ignore
    bot.click()
    
    if not bot.find( "button-ok", matching=0.97, waiting_time=10000):
        not_found("button-ok") # type: ignore
    bot.click()
    
