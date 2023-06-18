from pymongo import MongoClient


client = MongoClient('mongodb+srv://vedan987:Vedanshu1502@cluster-books.jailwop.mongodb.net/?retryWrites=true&w=majority')
db = client['Books-Data']
collection = db['Inventory']


data_books = [
    {
        'name' : 'Harry Potter and the Sorcerer\'s Stone',
        'publish_date' : '',
        'publisher' : 'Perfection Learning',
        'Author' : 'J.K. Rowling',
        'cost' : 250,
        'Category': ['Thriller', 'Mystery', 'Fantasy'],
        'Summary': 'This story is filled with dark comedy and crafted with a quality of writing that has garnered J.K. Rowling top awards in her country and ours. Harry Potter spent ten long years living with his aunt and uncle and stupid cousin, Dudley. Fortunately, Harry has a destiny that he was born to fulfill. One that will rocket him out of his dull life and into a unique experience at the Hogworts School of Witchcraft and Wizardry.'
    },
    {
        'name' : 'Power of Your Subconcious mind',
        'publish_date' : '1 December 2015',
        'publisher' : 'Amazing Reads',
        'Author' : 'Joseph Murphy',
        'cost' : 300,
        'Category': ['Mental Health'],
        'Summary': 'Did you know that your mind has a \'mind\' of its own? Yes! Without even realizing, our mind is often governed by another entity which is called the sub-conscious mind. This book can bring to your notice the innate power that the sub-conscious holds. We have some traits which seem like habits, but in reality these are those traits which are directly controlled by the sub-conscious mind, vis-à-vis your habits or your routine can be changed if you can control and direct your sub-conscious mind positively. To be able to control this \'mind power\' and use it to improve the quality of your life is no walk in the park. This is where this book acts as a guide and allows you to decipher the depths of the sub-conscious. In this book, \'The power of your subconscious mind\', the author fuses his spiritual wisdom and scientific research to bring to light how the sub-conscious mind can be a major influence on our daily lives. Once you understand your subconscious mind, you can also control or get rid of the various phobias that you may have in turn opening a brand new world of positive energy.'
    },
    {
        'name': 'The Maze Runner',
        'publish_date' : '22 September 2014',
        'publisher' : 'Scholastic',
        'Author' : 'James Dashner', 
        'cost' : 290,
        'Category' : ['Sci-Fi', 'Mystery'],
        'Summary' : 'When Thomas wakes up in the lift, the only thing he can remember is his name. He\'s surrounded by strangers—boys whose memories are also gone. Outside the towering stone walls that surround them is a limitless, ever-changing maze. It\'s the only way out—and no one\'s ever made it through alive. Then a girl arrives. The first girl ever. And the message she delivers is terrifying: Remember. Survive. Run.'
    },
    {
        'name' : 'Sherlock Holmes',
        'publish_date' : '10 January 2017',
        'publisher' : 'Fingerprint! Publishing',
        'Author' : 'Arthur Conan Doyle', 
        'cost' : 380,
        'Category' : ['Thriller', 'Mystery'],
        'Summary' : 'There\'s the scarlet thread of murder running through the colourless skein of life and our duty is to unravel it and isolate it and expose every inch of it. Sherlock Holmes Consulting Detective 221B Baker Street London.This is where begins a historical partnership between Dr. Watson the archetypal gentleman from the Victorian era and the eccentric, legendary sleuth, Sherlock Holmes. Join them as they gather clues, ranging from bloodstains and footprints to cigarette ash and wedding rings and arrive at unusual and surprising conclusions. This book is a collection of the four novels written by Sir Arthur Conan Doyle: A Study in Scarlet (1887), The Sign of the Four (1890), The Hound of the Baskervilles (1902) and The Valley of Fear (1915). Featuring the timeless detective Sherlock Holmes, these novels have been successfully engrossing readers for more than a century now.'
    },
    {
        'name' : 'The Fault in Our Stars',
        'publish_date' : '3 January 2013',
        'publisher' : 'Penguin Books Ltd',
        'Author' : 'John Green', 
        'cost' : 180,
        'Category' : ['Romance'],
        'Summary' : 'Despite the tumour-shrinking medical miracle that has bought her a few years, Hazel has never been anything but terminal, her final chapter inscribed upon diagnosis.'
    }
]

result = collection.insert_many(data_books)

document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()