
def get_ing():
    
    from recipe_scrapers import scrape_me
    a = input("Insert a link for a recipe. Make sure it's in the verified website list")
    scrape_me = scrape_me(a)
    x= (scrape_me.ingredients())
    from pprint import pprint

    pprint (x)

get_ing()
    
                          
