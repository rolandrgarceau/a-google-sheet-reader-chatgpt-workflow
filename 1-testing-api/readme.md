### 1-testing-api

After the fun with authentication, we can make requests and get responses of actual data. A good point that chatGPT offers is the fragility of handling simple list comprehensions, so error checking can be written into the later steps after we can fr'agile'ly accomplish the mission- convert and plot addresses and send that map to an endpoint for retrieval by another process/app/service/user/whatever.

Think about mocks and fixtures that may be used for future functional, unit, and other testing devised to meet current set of requirements. 

Create appropriate documentation that may reflect time/ series data. This will build on mission/strategy involved. Remember this is inevitably going to be 3D plots with something like cartopy (Geodataframes most likely). 

Here the distributed monolith may die. The project is to be able to download sheet data from workspaces to work with locally. 

What constitutes done? Is the downloaded information in a format usable for the next process? What is that, btw? Have we properly accounted for empty data or made appropriations for how it will be handled? 

It may be archaic to try and do this on the fly, but there are libraries that will wash the data for us, we just need to decide how we want that done. 

### Next steps

1-xxx is the authentication and retrieval step, so we still need to define in step 2-xxx the way in which we use the data.

End case success is measured byt the ability to transform addresses to coordinates. So the next logical step is to feed another service some cell information that will do the conversion to GPS coordinates, capture them in another location, and then use them to run a jupyter lab .ipynb file for mapping customers for marketing purposes 

It may possibly help the business CRM by adding a hidden column/field with these coordinates and populating them into the intake form for future development. How will the team handle this feature?