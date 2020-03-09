from elasticsearch_dsl import Search

def search(expression):
    s = Search(index="cards")
    if(expression == ''):
        s = s.query("match_all") 
    else:
        s = s.query("simple_query_string", query=expression)
    return s.execute()