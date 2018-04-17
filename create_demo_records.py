from minicms.wsgi import *
from news.models import Column, Article
 
 
def main():
    columns_urls = [
      ('sports_news', 'sports'),
      ('society_news', 'society'),
      ('tech_news', 'tech'),
    ]
 
    for column_name, url in columns_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]

        for i in range(1, 11):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name, i),
                slug='article_{}'.format(i),
                content='Details： {} {}'.format(column_name, i)
            )[0]
 
            article.column.add(c)
 
 
if __name__ == '__main__':
    main()
    print("Done!")