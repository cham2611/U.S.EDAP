from SPXCrawler import SPXCrawler
#'https://finance.yahoo.com/quote/BTC-USD/history/?frequency=1mo&period1=1410912000&period2=1720760848' # 비트코인

url = 'https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1mo&period1=-1325583000&period2=1720675400'

ex_url = SPXCrawler()
result=ex_url.example_url(url,'USD')
result

