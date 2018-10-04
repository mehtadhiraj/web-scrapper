import logging

try:  
    base_dir = os.path.dirname(__file__)+'/logs/'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    start_date_time= str(datetime.now())
    log_session = start_date_time.split(' ')
    log_session = log_session[0]
    log_session = log_session.replace('-', '')
    #print(log_session)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    
    file_handler = logging.FileHandler('logs/scraper_'+log_session+'.log')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
except Exception as e:
    print(e)
           