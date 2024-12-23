import scrapy

# spider class
class UnivspiderSpider(scrapy.Spider):
    name = "univspider"
    allowed_domains = ["www.indiastudychannel.com"] #all the allowed domains
    start_urls = ["https://www.indiastudychannel.com/universities/state-13-gujarat"] # start to scrape from this url

    def parse(self, response):
        

        queries=response.xpath("//span[@id='ContentPlaceHolder1_lblUniversities']/table[1]/descendant::a/@href")
        #this xpath gives list of 20 links present in the first page
        # we will loop through each url to extract content inside the page 
        for query in queries:
            
            relative_univ_url=query.get()

            univ_url='https://www.indiastudychannel.com'+relative_univ_url  
            yield response.follow(univ_url,callback=self.parse_univ_page)
        
        # it moves to the next page using the below xpath
        next_page=response.xpath("//span[@id='ContentPlaceHolder1_lblUniversities']/table[2]//descendant::a[position()=1]/@href").get()

        '''for query in range(0,len(next_page)-1):
            link=query.get()
            next_page_url='https://www.indiastudychannel.com'+link
            yield response.follow(next_page_url,self.parse)'''
        
        
        if next_page is not None:
            next_page_url='https://www.indiastudychannel.com'+next_page
            yield response.follow(next_page_url,self.parse)
        next_page_3="/universities/index.aspx?stateid=13&PageNumber=3"
        next_page_url='https://www.indiastudychannel.com'+ next_page_3
        yield response.follow(next_page_url,self.parse)
        

    def parse_univ_page(self,response):
        yield{
            'university_name':response.xpath("//h1/text()").get(),
            'desc': response.xpath("//div[@id='content_center']/child::b/text()").get(),
            'Address':response.xpath("normalize-space(//td/span[@id='ContentPlaceHolder1_lblAddress'])").get(),
            'City':response.xpath("normalize-space(//td/span[@id='ContentPlaceHolder1_lblCity'])").get(),
            'State':response.xpath("normalize-space(//td/span[@id='ContentPlaceHolder1_lblState'])").get(),
            'Phone':response.xpath("normalize-space(//td/span[@id='ContentPlaceHolder1_lblPhoneNumber1'])").get(),
            'Email':response.xpath("normalize-space(//td/span[@id='ContentPlaceHolder1_lblEmail'])").get(),

        }
