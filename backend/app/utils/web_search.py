from duckduckgo_search import DDGS

class WebSearchTool:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query, max_results=3):
        try:
            results = []
            for r in self.ddgs.text(query, max_results=max_results):
                results.append(f"Title: {r['title']}\nContent: {r['body']}")
            return '\n\n'.join(results)
        except Exception:
            return ''