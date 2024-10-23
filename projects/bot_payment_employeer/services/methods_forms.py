from botcity.core import DesktopBot, Backend

def fillout_windows(bot):
    if not bot.find( "window-signup", matching=0.97, waiting_time=10000):
        not_found("window-signup")
    
    if not bot.find( "label-name", matching=0.97, waiting_time=10000):
        not_found("label-name")

    if not bot.find( "fillout-name", matching=0.97, waiting_time=10000):
        not_found("fillout-name")
    bot.click_relative(26, 16)
    
    bot.kb_type("Fulano")
    
    if not bot.find( "label-salary", matching=0.97, waiting_time=10000):
        not_found("label-salary")
        
    if not bot.find( "fillout-salary", matching=0.97, waiting_time=10000):
        not_found("fillout-salary")
    bot.click_relative(34, 17)
    
    bot.kb_type("Salario")
    
    if not bot.find( "button-add", matching=0.97, waiting_time=10000):
        not_found("button-add")
    bot.click()
    
    if not bot.find( "button-process", matching=0.97, waiting_time=10000):
        not_found("button-process")
    bot.click()

