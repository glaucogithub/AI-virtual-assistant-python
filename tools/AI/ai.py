try :
    from tools.assistant import ask_question
    from tools.AI.data import data , youtube , wiki , google , youtube_play , goto_keys  
    from tools.AI.data import install_keys , calc_keys
    from tools.wiki_search import wiki_search 
    from settings.logs import *
    from tools.browser.search import *
    from tools.browser.goto import find_goto_address
    from system.install import install , command 
    from system.screen_text import command_sep
    from tools.string_processing import is_matched
    from tools.json_manager import JsonManager
    from tools.calculation import google_calculation
    from tools.run_program import if_run_type
except Exception as e:
    print(e)

def check(msg,mp):
    logger.debug('check->' + msg)
    for word in mp :
        if is_matched(word,msg):
            return True
    return False


def rep(msg,mp):
    for word in mp :
        if word in msg:
            return msg.replace(word,'').strip().capitalize()
    return msg.strip().capitalize()

def ai(msg,orginal_path) :
    """ Little ai for reacting to the msg.
        Written by Saurav-Paul"""
    logger.debug('Processing with ai')
    reply = "I don't know what to do, sir ."
    if if_run_type(msg):
        return 'Good luck sir.'
    else :
        try :
            for line in data :
                if is_matched(msg,line):
                    reply = data[line]
                    return reply
            # logger.info('Not found in common data')
            # from history
            try :
                f = orginal_path+'/tools/AI/learnt.json'
                history = JsonManager.json_read(f)
                for line in history:
                    if is_matched(msg,line,95):
                        logging.info('Found in learnt.json')
                        return history[line]

            except :
                logging.error("Can't read history file")

            if check(msg,youtube_play):
                msg = rep(msg,youtube_play)
                logger.info(msg)
                find_goto_address(msg)
                reply = 'Enjoy sir. :D'
            elif check(msg,goto_keys):
                msg = rep(msg,goto_keys)
                find_goto_address(msg)
                reply = 'check browser'
            elif check(msg,youtube):
                msg = rep(msg,youtube)
                search_youtube(msg)
                reply = 'check browser.'
            elif check(msg,wiki):
                msg = rep(msg,wiki)
                search_wiki(msg)
                reply = 'check browser.'
            elif check(msg,google):
                msg = rep(msg,google)
                search_google(msg)
                reply = 'check browser.'
            elif check(msg,install_keys):
                msg = rep(msg,install_keys)
                reply = install(msg)
            elif check(msg,calc_keys):
                msg = rep(msg,calc_keys)
                reply = google_calculation(msg)
                if reply == "sorry":
                    search_google(msg)
                    reply = "check browser"
            else :
                if 'cmd:' in msg:
                    msg = rep(msg,{'cmd:'})
                    command_sep()
                    command(msg.lower())
                    command_sep()
                    reply = 'done sir'
                else :
                    reply = ask_question(msg)
                    if 'check browser' not in reply:
                        logger.info('reply -> ' + reply)
                        learn = input('.......Press y to learn it.....')
                        if learn.lower() == 'y':
                            try :
                                history.update({msg:reply})
                                JsonManager.json_write(f,history)
                                logger.info('Learnt')
                            except Exception as e:
                                logger.info("Exception while writing learnt : "+e)
            return reply
        except :
            logger.info('Getting some error in ai')
            return reply

