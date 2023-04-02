# Vegedible

## User stories & Agile design

I created a number of user stories to guide my planning and design of the booking application.

I made use of the Github issue tracker and created a board view of the stories, split into categories of 'Todo', 'In Progress' and 'Done'.
The board is viewable [here.](https://github.com/users/merlynjwa/projects/1)

## Models

Diagram of the relationship between the two models designed for this application:

![Diagram of the relationship between the two models designed for this application](./docs/images/database/models/database_model_relationship.png)

I designed two models for this application:
* User, which is a subclass of the AbstractUser class from Django's auth library. The model has 5 required fields, username, email, password, first_name and last_name. As I did not work out a way of including the first_name and last_name fields in to the form for the signup page, new users are created with this field being empty.
* Order, which uses the User model as a foreign key for its customer field. The model has a date_and_time field and a table_number.

## Wireframes

### Homepage

#### Mobile

The skeleton of the homepage when displayed on a mobile device:

![Skeleton of the homepage when displayed on a mobile device](./docs/images/wireframes/homepage/mobile/Homepage__Mobile__Wireframes.png)

The first image is when the page is scrolled to the top, the second is when it's scrolled to the bottom of the page.

Skeleton of the header's menu, having been opened on the homepage:

![Skeleton of the homepage, displayed on a mobile device, with the hamburger menu open](./docs/images/wireframes/homepage/mobile/Homepage_with_Open_Menu__Mobile__Wireframes.png)

The skeleton of the menu is the same for all sections of the site.

### Sign Up Page

#### Mobile

The skeleton of the sign up page when it is displayed on a mobile device:

![Skeleton of the signup page, when displayed on a mobile device](./docs/images/wireframes/sign_up/mobile/Sign_Up_Page__Mobile__Wireframes.png)

### Order Booking Page

#### Mobile

Skeleton of the booking page when you are first placing an order:

![Skeleton of the booking page when you are first placing an order](./docs/images/wireframes//order_booking/mobile/Book_an_Order__Mobile__Wireframes.png)

Skeleton of the booking page when you are updating a previously made order, either to change some of the details, or to cancel the order:

![Skeleton of the booking page when you are updating a previously made order, either to change some of the details, or to cancel the order](./docs/images/wireframes/order_booking/mobile/Update_or_Cancel_an_Order__Mobile__Wireframes.png)

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

## Credits

### Google Fonts

I have imported 'Bebas Neue' and 'Comfortaa' from Google Fonts.
These two font families are provided under the [SIL Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)

### Django

Unsurprisingly, this project makes use of software libraries under the Django project.
This software is licensed under the [BSD 3-Clause license](https://github.com/django/django/blob/3.2.18/LICENSE), which is an open-source and free liberties license.

### Bootstrap

I made use of Bootstrap for this project.
This is available under an [MIT License](https://github.com/twbs/bootstrap/blob/v4-dev/LICENSE), which is an open source and free liberties license.

### Python

Again, unsurprisingly, this project makes use of Python.
Python software and documentation is licensed under the [PSF License Agreement](https://docs.python.org/3/license.html#psf-license)
