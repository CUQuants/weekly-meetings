import yfinance as yf

#ticker = yf.Ticker("MSFT").get_info()

def get_last_sentance(info):
    
    for i in reversed(range(len(info))):
        
        if len(info[i]) > 1:
            last_sentance = info[i]
            break
        
    return last_sentance

def get_summary(ticker_info):
    
    info = ticker_info['longBusinessSummary']
    info = info.split(".")
    name = ticker_info['shortName'].strip(".")
    
    name_period = True
    
    for idx, i in enumerate(info):
        
        if i.strip() == name:
            
            
            first_sentance = str(info[idx].strip() + ". " + info[idx+1].strip() + ". ")
            name_period = False
            
            last_sentance = str(i.strip() + ". " + get_last_sentance(info).strip() + ".")
            print(first_sentance + last_sentance)
            break
            
    if name_period == True:
        
        first_sentance = info[0]
        last_sentance = get_last_sentance(info)
        print(first_sentance.strip() + ".", last_sentance.strip() + ".")
        
        
test = get_summary(yf.Ticker("S").get_info())

