from consuner.consumer import get_msg
from logic.validation import validate_error
from producer.producer import publish_event

def main():
    while True:

        msg = get_msg()
        if not msg: 
            continue 

        #add
        msg_error = validate_error(msg)

        if msg_error: 
            msg['reason'] = msg_error






    
