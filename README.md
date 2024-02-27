# fintech_app_RajaKodumuru

1) I am successfully and able to retrieve the job description page, but after testing the code by sending 3-4 url's automatically Linkedin security system caught it and denied my request, so right now I am not able to fetch the data using BeautifulSoup.
2) Linkedin Security System doesn't allows us to scrap the data and it detects our pc details as well.
3) To scrap Linkedin Profiles and job description page we definitely need to use an api key, without api when i tried it didn't work, Linkedin profile page directly denied.
4) Scrapping using Chrome Driver is not efficient, and we need to downgrade the browser, each and every user have their browser updated in their mobiles and it is not efficient technique to use
5) I had scrapped Profiles and job description page using ProxyCurl API, it is successful.
6) I had been writing code using LangChain, GPT3.5 API key with ChatOpenAI, I have tested multiple ways but this is the efficient one.

**Code Explanation**
1) The Flask API takes Candidate Profile Url and Job Description Page Url as Input.
2) It gives the output to upgrade the necessary skills and suggests to gain required number of enough experience if there is any gap between the actual and required.
3) Here we are using ProxyCurl two end points, one for scrapping profiles and one to scrap job description pages.
4) both the Linkedin Profiles and job description pages data are scrapped in the json format.
5) I had retrieved all the skills of the candidate and made a string begining with a prompt.
6) Retrieved experience from the job description page and assigned meaningful range of numerical experience and mapped it with candidate profile experience by calculating the candidate experience using python's datetime.
7) after that inserted all the text to a pdf file and did text splitting, and embedding.
8) Stored texts and embeddings into Chroma Vector DB.
9) Used LangChain Chat Model, ChatOpenAI, sent a prompt to retrieve desired ouput.
10) AT last successful in getting the output.
