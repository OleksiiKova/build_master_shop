# Table of Contents

<!-- - [Automated Testing](#automated-testing) -->
- [Manual Testing](#manual-testing)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
- [Responsiveness and Device Testing](#responsiveness-and-device-testing)
- [Browser Testing](#browser-testing)
- [Accessibility](#accessibility)
- [Lighthouse Testing](#lighthouse-testing)
- [User Story Testing](#user-story-testing)
- [Bugs](#bugs)

Return back to the [README.md](README.md) file.

<!-- ## Automated Testing

To ensure the robustness and reliability of the application, a comprehensive testing strategy was employed, combining both manual and automated testing methods.

Leveraging Django's built-in testing framework, automated tests were written to cover critical aspects of the application's functionality. This includes tests for views and forms to verify that the application behaves as expected under various conditions.

To run the tests, I executed the following command in the terminal:

`python3 manage.py test`

Total Count of Automated Tests: 41

![screenshot](static/images/readme_images/testing/automated_testing/screen-terminal.png)  

To create the coverage report, I run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

Below are the reports on automated tests.

| App                                   | Screenshot                                   | 
| ------------------------------------- | -------------------------------------------- | 
| Bookings  | ![screenshot](static/images/readme_images/testing/automated_testing/report-bookings.png)   |
| Car rental  | ![screenshot](static/images/readme_images/testing/automated_testing/report-car-rental.png)   |
| Cars  | ![screenshot](static/images/readme_images/testing/automated_testing/report-cars.png)   |
| Offices  | ![screenshot](static/images/readme_images/testing/automated_testing/report-offices.png)   |
| Userprofile  | ![screenshot](static/images/readme_images/testing/automated_testing/report-userprofile.png)   |

[Back To Top](#table-of-contents) -->

## Manual Testing

To enhance quality and increase confidence in the correctness of the application, I conducted manual testing in addition to automated tests. This manual testing targeted areas not covered by the automated tests, ensuring comprehensive validation.


| Page                              | User Action                                                | Expected Result                                                              | Pass/Fail |
|-----------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------|-----------|
| Navigation (Desktop)              |                                                            |                                                                              |           |
|                                   | Click on the "BuildMaster" logo                           | Redirection to Home page                                                     | Pass      |
|                                   | Click on "Home" link in the navbar                        | Redirection to Home page                                                     | Pass      |
|                                   | Click on "Tools" dropdown in the navbar                   | Display a list of tools categories, including Power Tools, Hand Tools, etc.   | Pass      |
|                                   | Click on "Power Tools" in the "Tools" dropdown            | Redirection to Products page with "Power Tools" category selected            | Pass      |
|                                   | Click on "Screws & Nails" in the "Fasteners" dropdown     | Redirection to Products page with "Screws & Nails" category selected         | Pass      |
|                                   | Click on "Safety Equipment" in the navbar                 | Redirection to Products page with "Safety Equipment" category selected       | Pass      |
|                                   | Click on "Workwear" in the navbar                         | Redirection to Products page with "Workwear" category selected               | Pass      |
|                                   | Click on "All Products" link in the navbar                | Redirection to Products page showing all available products                  | Pass      |
|                                   | Click on "My Account" in the navbar (Authenticated user) | Dropdown menu appears with options: "My Profile", "My Reviews", etc.         | Pass      |
|                                   | Click on "Login / Register" in the navbar (Unauthenticated)| Redirection to Login or Register page                                        | Pass      |
|                                   | Click on "My Account" in the mobile menu (Authenticated)  | Dropdown menu appears with options: "My Profile", "My Reviews", etc.         | Pass      |
|                                   | Click on "Login / Register" in the mobile menu (Unauthenticated) | Dropdown menu shows "Register" and "Login" options                           | Pass      |
| Search Section                    |                                                            |                                                                              |           |
|                                   | Enter text in the "Search" input field                    | Search input is accepted. The search icon changes to active.                 | Pass      |
|                                   | Enter nothing in the "Search" input field and click "Search" | A message is displayed: "You didn't enter any search criteria!"              | Pass      |
|                                   | Click on the "Search" button in the desktop search form   | Redirection to the Products page with search results based on query          | Pass      |
|                                   | Click on the "Search" icon in the mobile search form      | Redirection to the Products page with search results based on query          | Pass      |
| Cart                               |                                                            |                                                                              |           |
|                                   | Click on the shopping cart icon                           | Redirection to the "View Cart" page, showing items in the cart if present   | Pass      |
|                                   | Check the cart icon for item count                        | The item count badge on the cart icon displays the correct quantity          | Pass      |
|                                   | Check the cart icon for total cost                        | The total cost is displayed in the cart icon in the format "€0.00" or similar| Pass      |
| Mobile Navigation                 |                                                            |                                                                              |           |
|                                   | Click on the "Search" icon in the mobile menu             | Dropdown search form is displayed with an input field and search button      | Pass      |
|                                   | Click on "My Account" in the mobile menu                  | Dropdown menu appears with options: "Login", "Register", etc.                | Pass      |
|                                   | Click on "View Cart" in the mobile menu                   | Redirection to the "View Cart" page, showing items in the cart if present   | Pass      |
|                                   | Click on "Login / Register" in the mobile menu (Unauthenticated) | Dropdown menu shows "Register" and "Login" options                           | Pass      |
| Footer                            |                                                            |                                                                              |           |
|                                   | Click on "Facebook" link                                   | Opens Facebook page in a new tab                                              | Pass      |
|                                   | Click on "Blog Posts" link                                  | Redirection to Blog Posts page                                                | Pass      |
|                                   | Click on "Contact us" link                                  | Redirection to Contact Us page                                                | Pass      |
|                                   | Click on "Health and Safety Authority" link                 | Opens HSA website in a new tab                                               | Pass      |
|                                   | Click on "Privacy Policy" link                              | Redirection to Privacy Policy page                                           | Pass      |
|                                   | Click on "Terms of Service" link                            | Redirection to Terms of Service page                                         | Pass      |
|                                   | Click on "Subscribe" button in the newsletter form          | Subscription to the newsletter with the provided email                      | Pass      |
|                                   | Submit email address in subscription form                  | Success or error message displayed depending on email validity               | Pass      |
|                                   | View footer at the bottom of the page                      | Footer should always be visible on all pages                                  | Pass      |
|                                   | Test footer responsiveness (desktop to mobile view)        | Footer layout should adapt correctly from desktop to mobile view             | Pass      |
|                                   | Click on the subscribe button in mobile view               | Newsletter form is accessible and functional on mobile                       | Pass      |
| **Home Page**                     |                                                            |                                                                              |           |
| Welcome Section                   |                                                            |                                                                              |           |
|                                   | Click on "Shop Now" button                                 | Redirects to the Products page                                               | Pass      |
| Popular Categories Section        |                                                            |                                                                              |           |
|                                   | Click on "Power Tools" card                                | Redirects to the Products page with the Power Tools category selected        | Pass      |
|                                   | Click on "Workwear" card                                   | Redirects to the Products page with the Workwear category selected           | Pass      |
|                                   | Click on "Safety Equipment" card                          | Redirects to the Products page with the Safety Equipment category selected   | Pass      |
| Blog Posts Section                |                                                            |                                                                              |           |
|                                   | View blog post cards (desktop: 3, tablet: 2, mobile: 1)    | Cards are displayed in the correct layout for each viewport                  | Pass      |
|                                   | Click on a blog post card                                  | Redirects to the correct blog post page                                      | Pass      |
|                                   | Click on "View All Blog Posts" button                     | Redirects to the All Blog Posts page                                         | Pass      |
| General                           |                                                            |                                                                              |           |
|                                   | Check responsiveness (desktop, tablet, mobile)            | Layout adjusts properly across all screen sizes                              | Pass      |
|                                   | Check for broken images or links                          | All images and links load correctly                                          | Pass      |
|                                   | Verify page performance                                    | Page loads quickly and assets are optimized                                  | Pass      |
| **My Profile Page**               |                                                            |                                                                              |           |
|                                   | Click on "Change Password" link                           | Redirects to the Change Password page                                       | Pass      |
| Default Information Section       |                                                            |                                                                              |           |
|                                   | Update profile information and click "Update Information" button | Profile information is successfully updated, with a success message         | Pass      |
|                                   | Leave form fields empty and submit                        | Form submits successfully without errors, as fields are optional       | Pass      |
| Order History Section             |                                                            |                                                                              |           |
|                                   | Check if orders are displayed in a table format           | Order table is displayed with correct headings and data                     | Pass      |
|                                   | Click on an order number link                             | Redirects to the specific order history page                                | Pass      |
|                                   | Check that "Order Date" column displays correct dates     | Dates are formatted correctly and align with order history                  | Pass      |
|                                   | Check "Items" column for detailed order items (desktop)   | Item names, quantities, and variants are displayed in a list                | Pass      |
|                                   | Check "Order Total" column for correct amounts            | Total amounts match order history                                           | Pass      |
|                                   | View order history table on smaller screens               | Table adjusts correctly; "Items" column is hidden as intended               | Pass      |
| General                           |                                                            |                                                                              |           |
|                                   | Verify responsiveness of the page                         | Layout adjusts properly across desktop, tablet, and mobile devices          | Pass      |
| **Products Page**                 |                                                            |                                                                              |           |
|                                   | Verify breadcrumb navigation                               | Breadcrumb links update correctly based on selected categories              | Pass      |
|                                   | Interact with "Sort By" dropdown                           | Dropdown options change the product order on the page                       | Pass      |
|                                   | Select "Sort By" in "Sort By" dropdown                     | Page reloads, displaying the default product order                          | Pass      |
| Product List                      |                                                            |                                                                              |           |
|                                   | View product cards                                         | Cards display product image, name, price, and rating (if available)         | Pass      |
|                                   | Click on a product name or image                           | Redirects to the detailed product page                                      | Pass      |
|                                   | Check "Out of Stock" label visibility                      | Label is displayed only for products with zero stock                        | Pass      |
|                                   | Test responsiveness of product grid                       | Grid adjusts appropriately for various screen sizes                         | Pass      |
|                                   | Verify product rating display                             | Stars align correctly with product rating values                            | Pass      |
|                                   | View price format for products                             | Prices are displayed in the correct currency format (e.g., €xx.xx)          | Pass      |
| Filtering                         |                                                            |                                                                              |           |
|                                   | Navigate to a specific category via breadcrumb            | Filters products to match the selected category                             | Pass      |
|                                   | Test category filtering                                    | Filters update URL with correct query parameters                            | Pass      |
|                                   | Check empty category result                                | Displays "No products found" message when category is empty                 | Pass      |
| General                           |                                                            |                                                                              |           |
|                                   | Verify responsiveness of the page                         | Layout adjusts properly across desktop, tablet, and mobile devices          | Pass      |
|                                   | Check for broken links or images                          | All links and images are functioning properly                               | Pass      |
| **Product Detail Page**           |                                                            |                                                                              |           |
|                                   | View product name and price                                | Product name and price are displayed correctly                              | Pass      |
|                                   | Check breadcrumb navigation                                | Breadcrumbs display correct hierarchy and link to the right categories      | Pass      |
|                                   | Verify product image functionality                         | Image is displayed; clicking on it opens a larger view                      | Pass      |
|                                   | View "Out of Stock" label visibility                       | Label appears only if the product is out of stock                           | Pass      |
|                                   | Add product to Wishlist                                    | Clicking the "Add to Wishlist" button adds the product to the user's wishlist | Pass      |
|   Product Variants                |                                                            |                                                                              |           |
|                                   | View available sizes                                       | Sizes are displayed as clickable buttons                                    | Pass      |
|                                   | Select a size                                              | The selected size is highlighted and details (e.g., SKU) are updated        | Pass      |
|                                   | Verify unavailable sizes                                   | Unavailable sizes are grayed out and cannot be clicked                      | Pass      |
|                                   | Check SKU update                                           | Selected size updates the SKU and associated product details                | Pass      |
|   Quantity Selection              |                                                            |                                                                              |           |
|                                   | Increment quantity                                         | Quantity increases within the allowed range                                 | Pass      |
|                                   | Decrement quantity                                         | Quantity decreases within the allowed range                                 | Pass      |
|                                   | Exceed maximum quantity                                    | Displays validation error or prevents further increase                      | Pass      |
|                                   | Deactivate decrement button when quantity is 1            | The decrement button is disabled when the quantity is 1                      | Pass      |
|   Add to Cart                     |                                                            |                                                                              |           |
|                                   | Add in-stock product to cart                               | Product is added successfully, showing success message | Pass      |
|                                   | Attempt to add out-of-stock product                       | "Out of Stock" button is disabled                                           | Pass      |
|                                   | Add more products than in stock                            | Displays a message indicating only the available quantity can be added      | Pass      |
|   Customer Reviews                |                                                            |                                                                              |           |
|                                   | View customer reviews                                      | Reviews are displayed with username, rating, and comment                    | Pass      |
|                                   | Write a review (logged in)                                 | User can submit a review successfully                                       | Pass      |
|                                   | Edit existing review                                       | User can edit their review, and changes are saved                           | Pass      |
|                                   | Delete existing review                                     | User can delete their review successfully                                   | Pass      |
|                                   | Attempt to write a review (not logged in)                 | Displays prompt to log in                                                   | Pass      |
|   General                         |                                                            |                                                                              |           |
|                                   | Test page responsiveness                                   | Page layout adjusts properly on desktop, tablet, and mobile                 | Pass      |
|                                   | Verify image scaling                                       | Images scale appropriately across devices                                   | Pass      |
|                                   | Verify page performance                                    | Page loads efficiently, and no broken links or errors are present           | Pass      |
|  **Cart Page**                   |                                                            |                                                                              |           |
|                                    | Verify the cart page loads correctly                       | Page displays the correct list of cart items (product image, name, price, etc.) | Pass      |
|                                    | Check for empty cart message                              | Displays "Your basket is empty" if there are no items in the cart             | Pass      |
|                                    | Check the "Continue Shopping" button                       | Button redirects to the products page                                          | Pass      |
|                                    | Check the "Checkout Now" button                           | Button redirects to the checkout page                                          | Pass      |
|                                    | Verify cart total calculation                              | Total price of items is displayed correctly, including taxes and delivery     | Pass      |
|                                    | Verify delivery cost display                              | Correct delivery cost is displayed based on conditions (standard or free)     | Pass      |
|  Item Display                      |                                                            |                                                                              |           |
|                                    | Verify product details on cart                            | Displays correct product name, image, SKU, and size (if applicable)           | Pass      |
|                                    | Verify item image visibility                              | Product image is displayed correctly for each item in the cart                | Pass      |
|                                    | Check "Remove" button functionality                       | "Remove" button removes the item from the cart and updates the page            | Pass      |
|   Quantity Update                  |                                                            |                                                                              |           |
|                                    | Test quantity update form                                 | Input field allows quantity change, and updates cart totals accordingly       | Pass      |
|                                    | Verify quantity increase and decrease buttons work         | Increase and decrease buttons adjust the item quantity and total price       | Pass      |
|                                    | Verify "Update" button functionality                      | Clicking the "Update" button updates the cart with new quantities             | Pass      |
|   Cart Total                       |                                                            |                                                                              |           |
|                                    | Verify cart total is correct after quantity change         | Cart total updates correctly after changing the quantity of any item          | Pass      |
|                                    | Verify Grand Total calculation                            | Grand total, including delivery, is correct after quantity or removal changes | Pass      |
|                                    | Test free delivery condition                              | Displays the free delivery message when the total exceeds the threshold      | Pass      |
|   **Chekout Page**                 |                                                            |                                                                              |           |
|                                    | Verify checkout page loads correctly                       | The page should load the checkout form with correct sections for order summary, delivery, and payment | Pass      |
|                                    | Verify order summary visibility                            | Displays correct order summary including item name, SKU, quantity, and price | Pass      |
|                                    | Check that the "Adjust Cart" button works                  | Redirects to the cart page when clicked                                        | Pass      |
|   Order Summary                    |                                                            |                                                                              |           |
|                                    | Verify the product details in the order summary            | Displays the product image, name, size, SKU, quantity, and price per item    | Pass      |
|                                    | Check cart totals (Subtotal, Delivery, Grand Total)        | The correct subtotal, delivery cost, and grand total are displayed            | Pass      |
|                                    | Verify the grand total calculation                         | Grand total, including taxes and delivery, is accurate                        | Pass      |
|   Form Fields (Details)            |                                                            |                                                                              |           |
|                                    | Verify form fields for full name, email, and phone number  | Correct labels, field types, and error handling for each field                | Pass      |
|                                    | Verify form field validations                              | All required fields should validate correctly (e.g., email format, phone number format) | Pass      |
| Form Fields (Delivery)             |                                                            |                                                                              |           |
|                                    | Verify form fields for address details                     | Correct labels and fields for street address, city, country, and postcode    | Pass      |
|                                    | Verify "Save this delivery information" checkbox visibility | Checkbox allows the user to save their address if authenticated              | Pass      |
|                                    | Check the links for account creation or login              | Links should redirect to the signup or login page if the user is not logged in | Pass      |
| Payment Section                    |                                                            |                                                                              |           |
|                                    | Verify the Stripe payment section loads                    | The card input section should appear correctly with no errors                 | Pass      |
|                                    | Verify error messages for invalid payment details          | Display appropriate error message if the user enters invalid payment details  | Pass      |
| **My Reviews Page**                |                                                            |                                                                              |           |
|                                    | Verify page loads correctly                               | Page loads with the title "Your Reviews" and list of reviews if available     | Pass      |
|                                    | Verify "No reviews" message appears when there are no reviews | "You have not written any reviews yet." message should display if no reviews exist | Pass      |
|   Reviews List                     |                                                            |                                                                              |           |
|                                    | Verify review title (product name) visibility              | Product name is displayed correctly for each review                           | Pass      |
|                                    | Verify review rating stars                                 | Stars align correctly according to the rating value                           | Pass      |
|                                    | Verify review creation date                               | Date of review creation is displayed in the correct format (e.g., "M j, Y, g:i A") | Pass      |
|                                    | Verify review update date visibility                      | If a review is updated, display the correct "updated on" date                 | Pass      |
|                                    | Verify comment visibility                                 | Review comment text is displayed correctly                                    | Pass      |
|   Review Actions                   |                                                            |                                                                              |           |
|                                    | Verify "Edit" link functionality                           | Clicking "Edit" redirects to the review editing page                          | Pass      |
|                                    | Verify "Delete" link functionality                         | Clicking "Delete" redirects to the review deletion page                       | Pass      |
|                                    | Verify review deletion confirmation                       | Deleting a review should prompt a confirmation and update the page             | Pass      |
| **My Wishlist Page**               |                                                            |                                                                              |           |
|                                     | Verify page loads correctly                                | Page loads with the title "Your Wishlist" and displays items if available     | Pass      |
|                                     | Verify "Empty Wishlist" message appears if no items exist   | "Your wishlist is empty." message should display if there are no items        | Pass      |
|                                     | Verify product image visibility                            | Product image is displayed for each item                                      | Pass      |
|                                     | Verify product name and price visibility                   | Product name and price are displayed for each item                            | Pass      |
|                                     | Verify "View Product" button functionality                 | Clicking "View Product" redirects to the product detail page                  | Pass      |
|                                     | Verify "Remove" button functionality                       | Clicking "Remove" removes the item from the wishlist                          | Pass      |
|                                     | Verify card layout and responsiveness                      | Cards for products should be aligned properly and adjust to screen size      | Pass      |

[Back To Top](#table-of-contents)

## Code Validation

### HTML

All HTML pages were validated using the W3C HTML Validator, and no errors were detected.

| Page                | Result                |
|---------------------|-----------------------|
| Home                | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2F) |
| My Profile        |  [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fprofile%2F) |
| My Reviews        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fprofile%2Fuser-reviews%2F) |
| My Wishlist        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fprofile%2Fwishlist%2F) |
| Products        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fproducts%2F) |
| Product Detail        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fproducts%2Fbm-8220111%2F) |
| Cart        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fcart%2F) |
| Checkout        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fcheckout%2F) |
| Checkout Success        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fcheckout%2Fcheckout_success%2FORD-BB6DVUSS) |
| Add a Product        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fadd%2F) |
| Edit a Product       | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fproducts%2Fedit%2Fbm-8777016%2F) |
| Delete a Product        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fproducts%2Fdelete%2Fbm-8777016%2F) |
| Add a Post        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fblog%2Fadd_blog_post%2F) |
| Edit a Post        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fblog%2Fedit%2Fessential-hand-tools-choosing-the-right-ones-for-y%2F) |
| Delete a Post        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fblog%2Fdelete%2Fhow-to-choose-a-drill-corded-vs-battery-powered%2F) |
| Contact Us        | [✅ No errors or warnings]() |
| All Blog Posts        | [✅ No errors or warnings](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbuild-master-shop-84761d123763.herokuapp.com%2Fblog%2F) |
| Contact Us        | [✅ No errors or warnings]() |
| Contact Us        | [✅ No errors or warnings]() |
| Contact Us        | [✅ No errors or warnings]() |
| Contact Us        | [✅ No errors or warnings]() |
| Contact Us        | [✅ No errors or warnings]() |



<!-- All HTML pages were validated using the [W3C HTML Validator](https://validator.w3.org/), and no errors were detected.
| Page                                                                                                                                     | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>Home</summary><img src="static/images/readme_images/testing/html_validations/home.png"></details>                      | <mark>PASS</mark>   |
| <details><summary>Booking</summary><img src="static/images/readme_images/testing/html_validations/booking.png"></details>                | <mark>PASS</mark>   |
| <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/html_validations/booking-form.png"></details>      | <mark>PASS</mark>   |
| <details><summary>Locations</summary><img src="static/images/readme_images/testing/html_validations/locations.png"></details>            | <mark>PASS</mark>   |
| <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/html_validations/contact-us.png"></details>          | <mark>PASS</mark>   |
| <details><summary>My profile</summary><img src="static/images/readme_images/testing/html_validations/my-profile.png"></details>          | <mark>PASS</mark>   |
| <details><summary>My bookings</summary><img src="static/images/readme_images/testing/html_validations/my-bookings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/html_validations/edit-booking.png"></details>      | <mark>PASS</mark>   |
| <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/html_validations/delete-booking.png"></details>  | <mark>PASS</mark>   |
| <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/html_validations/leave-review.png"></details>      | <mark>PASS</mark>   |
| <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/html_validations/all-reviews.png"></details>        | <mark>PASS</mark>   |
| <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/html_validations/my-reviews.png"></details>          | <mark>PASS</mark>   |
| <details><summary>Edit Review</summary><img src="static/images/readme_images/testing/html_validations/edit-review.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Delete Review</summary><img src="static/images/readme_images/testing/html_validations/delete-review.png"></details>    | <mark>PASS</mark>   |
| <details><summary>Sign In</summary><img src="static/images/readme_images/testing/html_validations/login.png"></details>                  | <mark>PASS</mark>   |
| <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/html_validations/signup.png"></details>                 | <mark>PASS</mark>   |
| <details><summary>Log Out</summary><img src="static/images/readme_images/testing/html_validations/logout.png"></details>                 | <mark>PASS</mark>   |
| <details><summary>Reset Password</summary><img src="static/images/readme_images/testing/html_validations/password-reset.png"></details>  | <mark>PASS</mark>   |
| <details><summary>Change Password</summary><img src="static/images/readme_images/testing/html_validations/change-password.png"></details>| <mark>PASS</mark>   | -->

### CSS

During the CSS validation process for this project, a couple of issues were identified that are related to the external CSS resource provided by Leaflet. Specifically:

- Mix-blend-mode Value: The plus-lighter value used in the Leaflet CSS file is not recognized as a valid mix-blend-mode value.
- Behavior Property: The behavior property with the value url(#default#VML) is not supported.
These issues are due to the external Leaflet CSS file hosted at https://unpkg.com/leaflet@1.9.4/dist/leaflet.css, and not from the custom CSS within this project. As such, they cannot be resolved directly within this project.

If you encounter validation issues or errors related to these external resources, please be aware that they originate from the external library and not from the project's own CSS.

![](static/images/readme_images/testing/css_validations.png)

### JavaScript

| File JS                                                                                                                                              | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>script.js</summary><img src="static/images/readme_images/testing/js_validations/main-script.png"></details>        | <mark>PASS</mark>   |
| <details><summary>rating.js</summary><img src="static/images/readme_images/testing/js_validations/rating-script.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the Home Page</summary><img src="static/images/readme_images/testing/js_validations/home.png"></details>               | <mark>PASS</mark>   |
| <details><summary>Embedded within the Locations Page</summary><img src="static/images/readme_images/testing/js_validations/locations.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the My Bookings Page</summary><img src="static/images/readme_images/testing/js_validations/my-bookings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>Embedded within the Edit Review Page</summary><img src="static/images/readme_images/testing/js_validations/edit-review.png"></details>        | <mark>PASS</mark>   |


Some of the JavaScript files in this project include Django template variables. When these files are validated using JSHint or similar tools, errors may occur due to the validator not recognizing these Django variables.
For instance, you might encounter errors like:
- 2	Expected '}' to match '{' from line 2 and instead saw '{'.
- 2	Missing semicolon.
- 2	Expected an assignment or function call and instead saw an expression.
- 2	Missing semicolon.
- 2	Unrecoverable syntax error. (2% scanned).

This error occurs because the validator doesn't interpret the Django template syntax correctly. When the Django variables are removed, the validation errors disappear.

| File JS                                                                                                                                              | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>Embedded within the Booking-form Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-booking-form.png"></details>        | <mark>ERROR</mark>   |
| <details><summary>Embedded within the Car Search Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-car-search.png"></details>        | <mark>ERROR</mark>   |
| <details><summary>Embedded within the Edit Booking Page</summary><img src="static/images/readme_images/testing/js_validations/has-variable-edit-booking.png"></details>        | <mark>ERROR</mark>   |

### Python

All Python files were processed using the [CI Python Linter](https://pep8ci.herokuapp.com/), and no errors were found.

#### Bookings app

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>cron.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/cron.png"></details>        | <mark>PASS</mark>   |
| <details><summary>forms.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_forms.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/test-forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/bookings_app/views.png"></details>        | <mark>PASS</mark>   |

#### Cars app
| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/car_app/views.png"></details>        | <mark>PASS</mark>   |

#### Offices app
| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/offices_app/views.png"></details>        | <mark>PASS</mark>   |

#### Userprofile app

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>admin.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/admin.png"></details>        | <mark>PASS</mark>   |
| <details><summary>apps.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/apps.png"></details>        | <mark>PASS</mark>   |
| <details><summary>forms.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>models.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/models.png"></details>        | <mark>PASS</mark>   |
| <details><summary>signal.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/signal.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_data.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-data.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_forms.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-forms.png"></details>        | <mark>PASS</mark>   |
| <details><summary>test_views.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/test-views.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>views.py</summary><img src="static/images/readme_images/testing/python_validations/userprofile_app/views.png"></details>        | <mark>PASS</mark>   |

#### Car rental project

| Python File                                                                                                                                               | Result              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| <details><summary>asgi.py</summary><img src="static/images/readme_images/testing/python_validations/project/asgi.png"></details>        | <mark>PASS</mark>   |
| <details><summary>settings.py</summary><img src="static/images/readme_images/testing/python_validations/project/settings.png"></details>        | <mark>PASS</mark>   |
| <details><summary>urls.py</summary><img src="static/images/readme_images/testing/python_validations/project/urls.png"></details>        | <mark>PASS</mark>   |
| <details><summary>wsgi.py</summary><img src="static/images/readme_images/testing/python_validations/project/wsgi.png"></details>        | <mark>PASS</mark>   |

[Back To Top](#table-of-contents)

## Responsiveness and Device Testing

Throughout the development process, the website was rigorously tested across a range of devices, including desktops, laptops, smartphones, and tablets. This testing ensured that the website displayed correctly on screens of various sizes and orientations, both portrait and landscape. Additionally, the responsive design was validated using Google Chrome's Developer Tools to confirm that the layout remained structurally sound and adaptable across different screen dimensions. No issues were noted, affirming that the site functions as expected across diverse environments.

[Back To Top](#table-of-contents)

## Browser Testing

The website was tested across Google Chrome, Safari, and Microsoft Edge, and no issues were found.

[Back To Top](#table-of-contents)

## Accessibility

Using the Wave Accessibility tool for continuous development and final testing involves the following checks:

- Ensure all forms are equipped with proper labels or aria-labels.
- Verify that color contrast ratios comply with the WCAG 2.1 Contrast Guidelines.
- Check that heading levels are correctly used to represent content hierarchy.
- Confirm that content is structured within landmarks to facilitate navigation with assistive technology.
- Provide descriptive alternative text or titles for non-text elements.
- Set the lang attribute for HTML pages.
- Implement ARIA properties following WCAG 2.1 best practices.
- Adhere to established coding standards for WCAG 2.1 compliance.

[Back To Top](#table-of-contents)

## Lighthouse Testing

Lighthouse validation was run on all pages (both mobile and desktop) in order to check performance, accessibility, best practices and CEO.

| Page            | Performance | Accessibility | Best Practices | SEO | Screenshot                                                                                                                  |
| --------------- | :---------: | :-----------: | :------------: | :-: | --------------------------------------------------------------------------------------------------------------------------- |
|                 |             |               |                |     |
| **Desktop**     |             |               |                |     |
| Home            |     99      |      100      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/desktop/home.png"></details>                    |
| Booking            |     100      |      100      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking.png"></details>                    |
| Locations            |     98      |      100      |      100       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/desktop/locations.png"></details>                    |
| Contact Us            |     100      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/desktop/contact-us.png"></details>                    |
| Booking Form            |     99      |      100      |      100       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/desktop/booking-form.png"></details>                    |
| Edit Booking            |     100      |      100      |      100       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-booking.png"></details>                    |
| Delete Booking            |     100      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-booking.png"></details>                    |
| All Reviews            |     100      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/all-reviews.png"></details>                    |
| Leave Review            |     100      |      100      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/desktop/leave-review.png"></details>                    |
| Edit Review            |     100      |      100      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/edit-review.png"></details>                    |
| Delete Review            |     100      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/desktop/delete-review.png"></details>                    |
| My Profile            |     100      |      100      |      100       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-profile.png"></details>                    |
| My Bookings            |     99      |      91      |      100       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-bookings.png"></details>                    |
| My Reviews            |     99      |      96      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/desktop/my-reviews.png"></details>                    |
| Sign In            |     100      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-in.png"></details>                    |
| Sign Up            |     100      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-up.png"></details>                    |
| Sign Out            |     100      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/desktop/sign-out.png"></details>                    |
|                 |             |               |                |     |
| **Mobile**      |             |               |                |     |
| Home            |     95      |      100      |      100       | 100 | <details><summary>Home</summary><img src="static/images/readme_images/testing/lighthouse/mobile/home.png"></details>                    |
| Booking            |     96      |      100      |      100       | 100 | <details><summary>Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking.png"></details>                    |
| Locations            |     76      |      100      |      96       | 100 | <details><summary>Locations</summary><img src="static/images/readme_images/testing/lighthouse/mobile/locations.png"></details>                    |
| Contact Us            |     95      |      100      |      100       | 100 | <details><summary>Contact Us</summary><img src="static/images/readme_images/testing/lighthouse/mobile/contact-us.png"></details>                    |
| Booking Form            |     93      |      100      |      100       | 100 | <details><summary>Booking Form</summary><img src="static/images/readme_images/testing/lighthouse/mobile/booking-form.png"></details>                    |
| Edit Booking            |     95      |      100      |      100       | 100 | <details><summary>Edit Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-booking.png"></details>                    |
| Delete Booking            |     95      |      100      |      100       | 100 | <details><summary>Delete Booking</summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-booking.png"></details>                    |
| All Reviews            |     94      |      100      |      100       | 100 | <details><summary>All Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/all-reviews.png"></details>                    |
| Leave Review            |     96      |      100      |      100       | 100 | <details><summary>Leave Review</summary><img src="static/images/readme_images/testing/lighthouse/mobile/leave-review.png"></details>                    |
| Edit Review            |     96      |      100      |      100       | 100 | <details><summary>Edit Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/edit-review.png"></details>                    |
| Delete Review            |     95      |      100      |      100       | 100 | <details><summary>Delete Review </summary><img src="static/images/readme_images/testing/lighthouse/mobile/delete-review.png"></details>                    |
| My Profile            |     95      |      100      |      100       | 100 | <details><summary>My Profile</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-profile.png"></details>                    |
| My Bookings            |     90      |      90      |      100       | 100 | <details><summary>My Bookings</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-bookings.png"></details>                    |
| My Reviews            |     93      |      95      |      100       | 100 | <details><summary>My Reviews</summary><img src="static/images/readme_images/testing/lighthouse/mobile/my-reviews.png"></details>                    |
| Sign In            |     95      |      100      |      100       | 100 | <details><summary>Sign In</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-in.png"></details>                    |
| Sign Up            |     95      |      100      |      100       | 100 | <details><summary>Sign Up</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-up.png"></details>                    |
| Sign Out            |     95      |      100      |      100       | 100 | <details><summary>Sign Out</summary><img src="static/images/readme_images/testing/lighthouse/mobile/sign-out.png"></details>                    |

[Back To Top](#table-of-contents)

## User Story Testing

| User Story                                                                                                                                                                                                                        | Screenshot                                                                                                                                                                                              | 
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| As a new user I can create an account so that I can access the rental services.  | ![screenshot](static/images/readme_images/testing/user_stories/create-account.png)                                                                                                                                                                    | 
| As a registered user I can log in to my account so that I can view and manage my rentals.  | ![screenshot](static/images/readme_images/testing/user_stories/sign-in.png)                                                                                                                                                           | 
| As a registered user I can view and update my profile information so that my personal data is accurate and up-to-date.  | ![screenshot](static/images/readme_images/testing/user_stories/my-profile.png)                                                                                                                                                                 | 
| As a user I can search for available cars so that I can find a car that fits my needs.  | ![screenshot](static/images/readme_images/testing/user_stories/car-search.png)                                                                                                                                                                    | 
| As a user I can filter cars by type, price so that I can narrow down my search to the most suitable options.  | ![screenshot](static/images/readme_images/testing/user_stories/car-filter.png)                                                                                                                                                                 | 
| As a user I can view detailed information about a car so that I can make an informed decision before booking.  | ![screenshot](static/images/readme_images/testing/user_stories/detail-info.png)                                                                                                                                                           |
| As a user I can book a car for a specified period so that I can rent it for the time I need.  | ![screenshot](static/images/readme_images/testing/user_stories/book-car.png)                                                                                                                                                                   | 
| As a registered user I can view my current and past bookings so that I can keep track of my rental history.  | ![screenshot](static/images/readme_images/testing/user_stories/my-bookings.png)                                                                                                                                                                 | 
| As a registered user I can cancel an upcoming booking so that I can change my plans if necessary.  | ![screenshot](static/images/readme_images/testing/user_stories/delete-booking.png)                                                                                                                                                               | 
| As a user I can contact customer support so that I can get help with any issues or questions regarding my rental.  | ![screenshot](static/images/readme_images/testing/user_stories/contact-us.png)                                                                                                                                                     |
| As an admin I can add, update, or remove cars from the inventory so that the list of available cars is accurate.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-add-car.png)                                                                                                                                                                   | 
| As an admin I can manage user accounts so that I can maintain the integrity of the platform.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-users.png)                                                                                                                                                                    | 
| As a user I can leave a review and rating for a car I rented so that I can share my experience with other users.  | ![screenshot](static/images/readme_images/testing/user_stories/leave-review.png)                                                                                                                                                                   | 
| As a user I can view reviews and ratings left by other users so that I can make an informed decision before renting a car.  | ![screenshot](static/images/readme_images/testing/user_stories/customer-reviews.png)                                                                                                                                                                | 
| As a Site Owner I can store customer support form in the database so that I can review them.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-messages.png)                                                                                                                                                                     | 
| As a Site Owner I can mark user requests as "read" so that I can see how many I still need to process.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-messages-read.png)                                                                                                                                                               | 
| As a user I can view the location of each office on a Map so that I can easily find and navigate to the office.  | ![screenshot](static/images/readme_images/testing/user_stories/locations.png)                                                                                                                                                                   | 
| As an admin I can add and update the office locations on Google so that users can see the accurate location of each office.  | ![screenshot](static/images/readme_images/testing/user_stories/admin-offices.png)                                                                                                                                                                 | 
| As a user I can read and accept the terms and conditions before confirming my booking so that I am aware of the rental policies and my responsibilities.  | ![screenshot](static/images/readme_images/testing/user_stories/terms.png)                                                                                                                                                                     | 
| As a user who has forgotten their password, I can be able to reset my password, so that I can regain access to my account.  | ![screenshot](static/images/readme_images/testing/user_stories/reset-password.png)                                                                                                                                                                     |
| As a newly registered user I can verify my email address, so that I can complete my registration and access my account.  | ![screenshot](static/images/readme_images/testing/user_stories/verification-email.png)                                                                                                                                                                     |

[Back To Top](#table-of-contents)

## Bugs

All known bugs and issues have been thoroughly addressed and resolved. The application is currently functioning as intended, with no outstanding errors reported.

[Back To Top](#table-of-contents)