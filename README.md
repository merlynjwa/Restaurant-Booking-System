# Vegedible

## Wireframes

### Mobile

#### Homepage

The skeleton of the homepage when displayed on a mobile device:
![Skeleton of the homepage when displayed on a mobile device](./docs/images/wireframes/mobile/Homepage__Mobile__Wireframes.png)

The first image is when the page is scrolled to the top, the second is when it's scrolled to the bottom of the page.

Skeleton of the header's menu, having been opened on the homepage:
![Skeleton of the homepage, displayed on a mobile device, with the hamburger menu open](./docs/images/wireframes/mobile/Homepage_with_Open_Menu__Mobile__Wireframes.png)

The skeleton of the menu is the same for all sections of the site.

#### Sign Up Page

The skeleton of the sign up page when it is displayed on a mobile device:
![Skeleton of the signup page, when displayed on a mobile device](./docs/images/wireframes/mobile/Sign_Up_Page__Mobile__Wireframes.png)

#### Order Booking Page

Skeleton of the booking page when you are first placing an order:

![Skeleton of the booking page when you are first placing an order](./docs/images/wireframes/mobile/Book_an_Order__Mobile__Wireframes.png)

Skeleton of the booking page when you are updating a previously made order, either to change some of the details, or to cancel the order:

![Skeleton of the booking page when you are updating a previously made order, either to change some of the details, or to cancel the order](./docs/images/wireframes/mobile/Update_or_Cancel_an_Order__Mobile__Wireframes.png)

## Models

### Customer

The customer model contains two fields:
* Email
* Name

The email field serves as the primary key of the 'Customer' table.
My reasoning for this choice is that there could be multiple customers with the same name, but they should each have a unique email address.

### Order

The order model contains the following fields:
* Customer
* Date & Time
* Table number

The customer field is a foreign key to the customer model, allowing each order to be associated with one customer.

The table number has to be unique for each date & time value.
The table number is also restricted to only accept integer values from 1 to 10.
