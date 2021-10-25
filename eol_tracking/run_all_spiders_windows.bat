echo "Running all spiders"
scrapy crawl google_apache -o google_apache.json
scrapy crawl google_centos -o google_centos.json
scrapy crawl google_iis -o google_iis.json
scrapy crawl google_informatica -o google_informatica.json
scrapy crawl google_oracle -o google_oracle.json
