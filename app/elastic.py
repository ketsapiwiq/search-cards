from elasticsearch_dsl import Index, Document, Text, Search, Q

class Card(Document):
    title = Text()
    text = Text()

    class Index:
        name = 'cards'
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }
    
    @classmethod
    def get_cards(cls, expression):
        q = Q('multi_match', query=expression, fuzziness="AUTO")
        # q = Q('match_all') | Q('more_like_this', li2ke=expression)
 
        # if(expression == ''):
        # else:
        #     q = q & Q("fuzzy_search", query=expression)

        # s = s.suggest('
        s = Search().query(q)
        s = s.extra(size=300)
        # s[:50]
        response = s.execute()

        cards = []
        for hit in response:
            cards.append({'title':hit.title, 'text':hit.text})


        return {'cards':cards}