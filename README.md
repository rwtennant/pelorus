# pelorus
Pelorus is an application to help you understand the nature of the data in large and/or complex data files.  In past lives I have come across data sources that are complex in nature and have been challenged to understand the data fields and values in those fields. The lack of understanding limited my ability to use the data from those sources. Pelorus ingests data files and produces information and statistics about the fields in those files.

## Why did I build Pelorus?
This was primarily a side project to help me revisit development and delivery projects.  I've had to learn and explore Python, Django, SQLite, among other concepts and tools and the process helps me as a product manager to, at least partly, walk a few miles in a developers shoes. And, I like building things.

## Why did I name it Pelorus?
I actually found the name first and it sounded like a good project codename, so I went with it. It turns out a [Pelorus](https://en.wikipedia.org/wiki/Pelorus_(instrument)) is a sort of compass used in marine navigation - so it provides direction. Not a terrible name, even if it wasn't intentional.

## What does it do?
Pelorus allows you to upload a structured csv file (currently csv is the only format supported) and it will automatically calculate and present information about each field in that file.  The currently supported information includes:
* Type of data (e.g. Integer, Float, String, etc)
* Number of blank values
* Number of unique values
* The variability of the values (see below for more information on how Variability is currently calculated)
* For numeric fields
  * max
  * min
  * average
  * standard deviation
![Uploaded Datasets](https://postimg.cc/p5ry0s3K][img]https://i.postimg.cc/p5ry0s3K/Pelorus-Screenshot-Landing-Page.png) ![Dataset Field Information](https://postimg.cc/R6XNQkpM][img]https://i.postimg.cc/R6XNQkpM/Pelorus-Screenshot-File-Detail.png)
  
## What's next for Pelorus?
Plenty of thoughts of how I can continue to extend and make Pelorus better... here are a few ideas:
* Deploy it as a SaaS offering
* Make it multi-tenant
* Add the ability to drill into a field and see and explore the its values
* Look at relationships between fields - identify those whose values are highly correlated, for example

## A note on measuring variability of a field
I wanted a way to quickly look at a field and understand how distributed its values are.  Some fields are highly concentrated, where one or two values dominate, whereas others are more evenly distributed. You may know,for example, that a field has 5 unique values (a, b, c, d, and e), but you can't tell from that one number that 99% of the rows are populated with value d. The Variability index provides at least some information about how well distributed a field's values are - the closer to 1, the more evenly distributed.

