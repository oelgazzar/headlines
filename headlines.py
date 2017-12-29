from flask import Flask
import feedparser

app = Flask(__name__)

pubs = {"bbc"		: "http://feeds.bbci.co.uk/news/rss.xml",
		"cnn"		: "http://rss.cnn.com/rss/edition.rss",
		"fox"		: "http://feeds.foxnews.com/foxnews/latest",
		"iol"		: "http://rss.iol.io/iol/all-content-feed"
		}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
	url = pubs[publication]
	res_dict = feedparser.parse(url)
	first_article = res_dict["entries"][0]
	html = """<h1>{} Headings</h1>
		<b>{title}</b>
		<i>{published}</i>
		<p>{summary}</p>""".format(publication.upper(), **first_article)
	return html
	
if __name__ == "__main__":
	app.run(debug=True)
