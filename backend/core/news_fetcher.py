
import feedparser
import requests
from datetime import datetime
import time

class NewsFetcher:
    """Fetch stock news from various sources"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_news(self, ticker, limit=10):
        """Get news for a specific stock ticker"""
        try:
            # Clean ticker - remove .KA or other suffixes for news search
            search_ticker = ticker.split('.')[0]
            
            # Google News RSS feed
            rss_url = f"https://news.google.com/rss/search?q={search_ticker}+stock+PSX+Pakistan&hl=en-PK&gl=PK&ceid=PK:en"
            
            feed = feedparser.parse(rss_url)
            
            news_items = []
            for entry in feed.entries[:limit]:
                # Extract basic info
                published = entry.get('published', '')
                try:
                    # Try to parse and reformat date
                    dt = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %Z')
                    published = dt.strftime('%Y-%m-%d')
                except:
                    pass
                
                news_items.append({
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': published,
                    'source': entry.get('source', {}).get('title', 'Google News'),
                    'summary': entry.get('summary', '')
                })
            
            # If no news found for specific ticker, get general PSX news
            if not news_items:
                return self.get_general_market_news(limit)
                
            return news_items
            
        except Exception as e:
            print(f"Error fetching news for {ticker}: {e}")
            return []

    def get_general_market_news(self, limit=10):
        """Get general Pakistan market news"""
        try:
            rss_url = "https://news.google.com/rss/search?q=PSX+Pakistan+Stock+Exchange&hl=en-PK&gl=PK&ceid=PK:en"
            feed = feedparser.parse(rss_url)
            
            news_items = []
            for entry in feed.entries[:limit]:
                published = entry.get('published', '')
                try:
                    dt = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %Z')
                    published = dt.strftime('%Y-%m-%d')
                except:
                    pass
                    
                news_items.append({
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'published': published,
                    'source': entry.get('source', {}).get('title', 'Google News'),
                    'summary': entry.get('summary', '')
                })
            return news_items
        except Exception as e:
            print(f"Error fetching general news: {e}")
            return []
