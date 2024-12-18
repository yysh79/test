from utils.my_loger import logging 

def on_button_click(e, model, button):
    logging.info("pppdsdfdsafdsaffs")
    new_color = model.chang_color()
    button.bgcolor= new_color
    button.update()
