# JB Wildlife Prints

An online webshop for wildlife prints from photographer Joris Bomert.

## Development 
---------------
- This sites main purpose is to advertise and sell JB's photos to customers that are looking to buy beautiful prints of wild animals.  
- It's a B2C site that sells prints as a product to consumer, with a single payment.
- Payment method, card, or Swish( sweden only). Swish is a mobile app that's extremely popular in sweden, and every buissiness have it as payment option.
- The site will include a card payment method(stripe) and a shopping cart, a filter image function, high quality images, and in the future a rating and comment system.
- I have planned both swedish and english keywords, and these were suggested by the search engine.
    - Short-tail keywords:
        - Wildlife, wildlife in sweden, wildlife prints. Djur, natur, tavlor, foto.
    - Long-tail keywords :
        - Wildlife prints for sale, common wildlife in sweden, nature photography online shop. Stora tavlor djur, posters djur och natur. Köpa fotografier online. 

    - Keywords that I will use, based on wordtracker.com:
        - Wildlife photography(4.300), sweden wildlife(90), wildlife pictures(570), wildlife paintings online for sale(80), tavlor med naturmotiv(5)

- The site will link to following sites to increase SEO validation:
    - Svenska Rovdjursföreningen, a swedish wildlife magazine that often publishes JB's photographs. 
    - Canon, the company whose products is used by JB to produce these beautiful photos and prints. 
- The link to this site will be published on both Instagram and the Facebook business page

### Users
- This sites user focus are people who appreciate wildlife, and would like to purchase a print of their choise from our webshop. 
- The best way to reach my users is through facebook and instagram, as there is hashtags and facebook groups to ensure that it's the correct user group. These are also the best places for users to view wildlife content, as there is algorithm that ensures that the users only see what they are interested in.
- It's not difficult to find a web store that sells mass produced prints of wildlife. What is offered on this website however, is a chanse to buy prints directly from a expert photographer. These prints are not part of a mass production, they are printed in limited ammount to keep each image's unique value.
- Delivering this content will be tough, as the competition is high. The best way for us to achieve this without a commercial budget, is through social media, and by building a network.

### Sales 
- Art such as these photographs, is not something that should be put on weekly sales, as it lowers the unique value of treating/displaying it as a mass production. Exeption would be for the hollidays, as it is only once per year, and for a special occasion. 

### Goal
- The goal of this buisiness is to create a site where users can easily and secure make a purchase of the unique prints from JB's collection. The intent is to have a fully functioning, good looking, trustworthy webstore. 
- Paid ads is not a priority as of this moment. Using free social platforms, and advertisement through social network will be good enough for now.

### SEO 
- To create the feeling of expertise and authoritativeness to users, I would like to display the prints in a real world enviroment. There are websites that generates a photo in a livingroom etc. This is not MVP however, but it is certainly important to implement. 
- Another important feauture for trustworthiness, is ratings and user comments. Not either MVP, but important for future.
- Purchasing a custom domain will increase trust and is important in the future.
- A picture is worth a thousand words. I believe using less text, and instead focus on quality images and clear subtle navigation is going to be the best approach for this site.

### Mockup
- It was first planned to be published in swedish on the frontend, hence why some mockups are written in swedish and some in english.
- It's very possible that the end product won't look exactly like the mockup due to technical issues or increased UX

![Flowchart](media/flowchart.jpg)
- High quality landing page, clear purpose of the site is in the hero title section. To keep the image clean, I have not added a typical navigation bar. Instead there is two buttons, one for contact page and one directly to the webshop. 
- 3 reasons section where I present to the user what can be expected in terms of quality and service. As well as a section for the photographer JB to introduce himself to the user. 

![Landing page](media/mocklandingpage.jpg)
- Bottom section of page will be same across all pages, a option for users to sign up for a newsletter, and a footer with social links and a nav element to the other pages. Once again, I have on purpose not added a typical navigation bar on top of the page, but instead, users can reach the pages from the footer on every page. 

- On mobile devices, the navigation is collapsed, to keep the hero image clean and for improved UX. The user can navigate to all pages from this dropdown as well.
- 3 reasons section is now below a image carousel, this to make it more clear to visitors on mobile devices what the purpose of the site is - photographs of wildlife.

![Landing page mobile](media/mockupmobile.landing1.jpg)
- The webshop page contains a gallery of high quality images. If the user has not chosen a filter, all available prints are shown. Two filter options, mamals and birds. Later on in production, more filters could be added, such as filter by seasons. 
- The shopping bag icon :
    - If user has added a product to cart, this icon will be accessible on all pages.

![Webshop](media/mockupwebshop.jpg)
- If user selects a image, they get sent to a photo preview window. It has:
    - A larger preview of the photo
    - Next and previus arrows - this will display other photos of the same animal species, so that the user don't have to go back to select another yet similar product. 
    - Size options and responsive pricing. User selects which print size they would like, and the price updates accordingly.

![Webshop mobile](media/mockupmobile.webshop2.jpg)

- Checkout page contains a smaller preview of the product/s, ammount, shipping cost and total cost. Users can edit ammount or delete item on this page. To continue, user has to sign up/ sign in. This requirement is described next to the Continue button, so that the user knows that it is required before they press Continue.
- The authentitaction is planned to be handled inside a modal.

![Checkout page](media/mockup.checkout.jpg)

- Once user have gone through the authentication steps, they can now fill in the required fields for shipping and credit card details.
- If the user(sweden only) wishes to pay with Swish as mentioned earlier, they would have to contact JB, as Swish connects to a phone number. For privacy, I do not put JB's phone number on this page. This is explained to the user on the page.
- When all the required fields have correct value, user can click Purchase button. A confirmation email is sent to the user. 


## Deployment
---------------

- The site was deployed by:
    - Setting up a external database on ElephantSQL.com
    - On Heroku.com, create a new app and connect it to the ElephantSQL database by adding the database url to heroku's config vars
    - Underneath Deploy on heroku, selecting deployment method: GitHub
    - Connect repository from GitHub
    - Choose main branch, then Deploy Branch


## Credits
---------------

### Content
- For mockup, 'moqups.com' was used. This page offered 400 objects for free, but for future I would concider purchase upgraded plan, as it's easy to use and learn, and offers great tools for project planning.
- All photos used on this page is by photographer Joris Bomert, with his permission naturally, as it is a webstore for his products.