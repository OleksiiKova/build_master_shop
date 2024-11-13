# Build Master Shop

Build Master Shop is a full-featured e-commerce web application specializing in the sale of tools and workwear. Built with Django, this project demonstrates a modern, responsive shopping platform with a user-friendly interface for browsing, selecting, and purchasing products.

### [Link to the Build Master live website](https://build-master-shop-84761d123763.herokuapp.com/)

![](static/images/readme_images/am-i-responsive.png)

## Table of Contents

- [Overview](#overview)
- [Agile Methodology](#agile-methodology)
- [UX](#ux)
   * [Strategy](#strategy)
   * [Scope](#scope)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
- [Existing Features](#existing-features)
   * [Account Management](#account-management)
   * [CRUD Functionality](#crud-functionality)



## Overview
Build Master Shop is a web application developed using Django, designed as an online store specializing in tools and workwear. The platform allows users to browse a comprehensive selection of high-quality tools and workwear, add items to their cart, and complete purchases with ease. This project was created as part of my portfolio to showcase my proficiency in e-commerce web development.

#### First-Time User
- Tool Seeker: A user looking for specific tools or workwear, whether for professional or personal use, who values reliable and high-quality products.
- Information Seeker: A customer who wants detailed information about tools and workwear, including product descriptions, prices, and specifications.
- Online Shopper: A user who prefers the convenience of online shopping, allowing them to explore products and complete purchases from home.

#### Returning User
- Order History Reviewer: A returning customer who wants to view past purchases for record-keeping or reordering.
- Quick Buyer: A returning user with an account who wishes to make purchases efficiently, without having to re-enter their information.
- New Arrivals Explorer: A returning customer who checks the site regularly to discover the latest tools, workwear, and promotions.

[Back To Top](#table-of-contents)

## Agile Methodology
This project followed Agile principles, utilizing GitHub Issues to document and manage User Stories effectively. Each User Story was associated with clear Acceptance Criteria and broken down into smaller tasks, which allowed for flexible adjustments and ensured that the development process stayed aligned with project goals. You can view the issues for this project [here](https://github.com/OleksiiKova/build_master_shop/issues).

A Kanban Board was employed to visualize and streamline the workflow, using columns such as Backlog, To Do, In Progress, and Done. This structure provided a straightforward way to track task progress and adjust priorities as needed. The board layout supported a flexible, iterative approach, making it easier to implement new features and address feedback throughout development.

[Kanban view](https://github.com/users/OleksiiKova/projects/4/views/1)

<details><summary>Click to view a screenshot of the Kanban view</summary><img src="static/images/readme_images/kanban-1.png"></details> <br>
In addition to the Kanban Board, GitHub's Table view was used for a more organized, high-level overview of the project. This view allowed me to see all tasks, priorities, and their statuses at a glance, ensuring efficient planning and resource allocation.

[Table view](https://github.com/users/OleksiiKova/projects/4/views/4)

<details><summary>Click to view a screenshot of the Table view</summary><img src="static/images/readme_images/kanban-2.png"></details> <br>
I structured the project around Epics and User Stories, dividing the development into manageable chunks. Each Epic corresponded to a core feature of the "Build Master Shop" platform, such as user management, card and orders, or reviews and rating. This structure ensured that each feature was user-centric and aligned with real-world needs.

#### Epics:
1. [EPIC: Product Management](https://github.com/OleksiiKova/build_master_shop/issues/7)
2. [EPIC: User Management](https://github.com/OleksiiKova/build_master_shop/issues/3)
3. [EPIC: Reviews & Ratings](https://github.com/OleksiiKova/build_master_shop/issues/19)
4. [EPIC: Customer Support](https://github.com/OleksiiKova/build_master_shop/issues/25)
5. [EPIC: Cart & Orders](https://github.com/OleksiiKova/build_master_shop/issues/14)

The MoSCoW Method of Prioritization was employed to categorize each User Story into Must Have, Should Have, or Could Have priorities. Some features were labeled as Won't Have and deferred to the Backlog for potential future development. This approach helped to maintain a strong focus on the Minimum Viable Product (MVP), ensuring that essential features, such as product catalog browsing, user authentication, and checkout, were prioritized.

Overall, implementing Agile Methodology, combined with the MoSCoW prioritization technique, proved highly effective. This approach kept development organized and facilitated better time management by ensuring that the most valuable features were addressed first. While I did not set rigid timeframes for each iteration, moving tasks from To Do to Done was both motivating and provided a tangible sense of progress.

[Back To Top](#table-of-contents)

## UX

### Strategy
Build Master Shop aims to deliver a seamless and enjoyable shopping experience for customers seeking high-quality tools and workwear. The website’s primary features include a comprehensive product catalog, easy-to-navigate categories, and a streamlined checkout process. Additionally, the site highlights the brand's commitment to quality and customer satisfaction, with detailed product descriptions and usage guides for each item. A "Why Choose Us" section emphasizes the advantages of purchasing through Build Master Shop, building trust with customers and setting the brand apart in the market.

### Scope
Functional Specifications: Key functionalities include user registration and authentication, product inventory management by administrators, a personalized profile for customers, and a shopping cart for managing selected products. Customers can search, filter, and sort through the product catalog to find specific items, with options to read and leave product reviews. Additional features include viewing order history, tracking current orders, and accessing customer support for inquiries or assistance with purchases.

Content Requirements: Engaging content will include product descriptions, usage tips, brand information to help customers make informed purchasing decisions. Each product listing will contain detailed specifications, designed to support both professionals and DIY enthusiasts in selecting the right tools and workwear.

### Structure
The site structure is designed to guide users intuitively from browsing products to completing purchases. The information architecture is organized to provide a logical and seamless user flow, with easily accessible pages for the home, product categories, cart, and checkout, enhancing overall usability.

The navbar displays the Build Master Shop logo consistently across all pages and devices, reinforcing brand identity. Optimized for mobile users, the navbar features a responsive toggler that collapses the menu for a cleaner view on smaller screens. Links to essential pages, including Home and Products Categories are prominently displayed. For logged-in users, a profile icon provides access to personalized options such as my profile (include default delivery information and order history), my reviews, and my wishlist. New visitors or users not yet signed in will see links to Login and Register, ensuring a smooth onboarding experience.

Call to Action (CTA) Placement: Key CTAs are strategically placed to drive conversions. For instance, on the Home page, the "Shop Now" button is prominently displayed, encouraging users to begin browsing immediately. On product pages, the "Add to Cart" button is clearly highlighted to facilitate quick actions. On the blog page, the "Shop Now" button is also available, allowing readers to transition seamlessly from reading informative articles to browsing related products. This design ensures that critical CTAs are easily visible, enhancing user engagement and promoting conversions.

The footer of the Build Master Shop website offers users easy access to essential information, including contact details (phone and email), policy links, and social media channels. The Contact Information section provides users with a phone number and email address for quick support. The Stay Connected area includes a link to our Facebook page, allowing customers to stay updated and engaged with the brand on social media. For easy navigation, the Our Links section contains direct links to key pages like the Blog and Contact Us pages, giving users quick access to content and support resources. There’s also a Useful Links section, featuring external resources like the Health and Safety Authority (HSA), which provides additional industry-related information. The Policies section includes links to our Privacy Policy and Terms of Service, promoting transparency and ensuring users can conveniently access important legal information. Finally, a Subscribe form allows users to sign up for updates, offering an opportunity to stay informed about new products, promotions, and company news. This organized and informative footer supports user convenience and trust, enhancing their overall experience on the site.

#### Wireframes

The website is designed to be clear and simple. To create the wireframe I used Balsamiq software. During the design phase, some elements were modified to enhance the user experience.
PDF file with my wireframe you cand find [here](static/images/readme_images/car_rental.pdf).

#### Database structure
After deciding on the project's features, I used Lucidchart to plan the database structure. The diagram below serves as an initial guide, illustrating the types of data and their relationships.

![](static/images/readme_images/er_diagram.png)

### Surface

#### Colours

The following colour palette was used from [Coolors](https://coolors.co/):

![](static/images/readme_images/colour_palette.png)

#### Typography

- Headings: The "Montserrat" font-family is used for all heading levels to ensure a modern and clean look.
- Body Text: The default Bootstrap font settings are utilized for all other text to maintain consistency and readability across the site.

[Back To Top](#table-of-contents)

## Existing Features

- Account Creation: New users can sign up, with email confirmation required to ensure security and prevent spam.
   <details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/sign-up.png"></details>
   <br>

- Login System: Existing users can log in to access their profiles and manage their bookings.
   <details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/sign-in.png"></details>
   <br>

- Password Recovery: If users forget their password, they can reset it through a secure process.
   <details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/reset-password.png"></details>

- Change Recovery: If users wants to change their password, they can change it on My Profile Page.
   <details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/change-password.png"></details>

### CRUD Functionality

As part of the Build Master Shop project, the application provides front-end and back-end CRUD (Create, Read, Update, Delete) functionality for various features, allowing both administrators and users to manage content easily.

#### Administrator Features

##### Product Management:

- Create: Admins can add new products to the catalog through the admin interface, including product descriptions, images, pricing, and stock.
- Read: Admins can view all products in the catalog, along with detailed information for each item.
- Update: Admins can update product details such as prices, descriptions, and stock, ensuring the catalog is always up-to-date.
- Delete: Admins can remove products from the catalog when necessary, for instance, when a product is discontinued or out of stock.

##### Blog Management:

- Create: Admins can write and publish blog posts directly from the admin interface, sharing industry news, product updates, or customer tips.
- Read: Admins can view all blog posts, including drafts and published content, for management purposes.
- Update: Admins can edit blog posts as needed, updating text, images, or categories to keep content fresh and relevant.
- Delete: Admins can delete blog posts that are outdated or irrelevant, ensuring that the site remains organized and informative.

#### User Features

##### Ratings:

- Create: Users can rate products they have purchased, providing feedback based on their experience.
- Read: Users can view ratings and reviews submitted by other customers to help inform their purchasing decisions.
- Update: Users can edit their ratings or reviews if they wish to change their feedback after further use of the product.
- Delete: Users can delete their own ratings or reviews, allowing them to remove content if needed.

##### Wishlist:

- Create: Users can add products they are interested in to their wishlist, saving items for future reference or purchase.
- Read: Users can view their wishlist to easily keep track of items they are considering purchasing.
- Update: Users can update their wishlist by adding new items or removing those they are no longer interested in.
- Delete: Users can remove individual items from their wishlist or clear the entire list if desired.

These CRUD functionalities empower both administrators and users to efficiently manage products, blog content, ratings, and wishlists, contributing to a seamless user experience on the Build Master Shop website.

### Responsive Navbar
The Build Master website features a sleek and user-friendly navigation bar designed for an optimal browsing experience across all devices.

- The BuildMaster logo is prominently displayed in the top navigation section of the website, ensuring brand consistency and recognition. This logo is clearly visible across all screen sizes and contributes to a professional and cohesive identity. However, for mobile users, the logo remains part of the top navigation, while the navbar toggler button is used to collapse the menu for a cleaner view on smaller screens. The toggler focuses on providing a functional way to access the menu rather than displaying the logo itself.

- Mobile-First Design: Optimized for mobile devices, the navbar includes a responsive toggler button that collapses the menu into a more compact layout on smaller screens. This ensures that users can easily access the menu without unnecessary clutter, even on mobile.

- Search Functionality: The navbar includes a dedicated search bar, allowing users to quickly search for cars, bookings, or other relevant information. On mobile devices, the search option is also available in a dropdown for easy access.

- Dynamic Navigation Links: The navbar includes key links such as My Account, My Wishlist, My Profile, and Cart, along with options like Add Product and Add Post for admins. These links are designed to be easily accessible and provide a smooth navigation experience.

    - User-Specific Options: For authenticated users, the My Account dropdown gives access to personalized features, including links to My Profile, My Reviews, My Wishlist, and a logout option.

    - Admin-Specific Options: Admins (superusers) have additional management options in the navbar, such as Add Product and Add Post, to manage site content directly from the navigation menu.

    - Cart: The Cart icon in the navbar shows the number of items in the cart and the total cost. If there are items in the cart, a badge will display the quantity, providing users with real-time updates.

    The links dynamically highlight based on the current page, providing users with a visual cue of where they are within the site. These navigation elements are intuitive, ensuring that users can easily find and access key areas of the site.

- Promotional Banner:
Beneath the top navigation, users are greeted with a promotional banner that highlights special offers, such as free delivery on orders over a specified amount. This banner is strategically placed to grab users' attention while they navigate the site. The message is displayed in a clear, concise format that encourages users to take advantage of the offer, and its design ensures it remains visible without cluttering the user interface.

Landing page on desktop
<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/navbar-desktop.png"></details>
<br>

Landing page on mobile
<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/navbar-mobile.png"></details>

### Footer
The footer of our website is carefully designed to offer users convenient access to important information, helpful resources, and essential policies. Here's a detailed breakdown of the footer features:

#### Contact Information:
- Users can easily find our contact details in this section. It includes:
    - Phone number: For immediate assistance, users can reach us at +353 1 2312 3123.
    - Email address: For inquiries and support, the contact email is provided as buildmaster@example.com.
- Additionally, users can stay connected with us via social media, including a link to our Facebook page for updates and community interaction.

#### Links:
- We link to our Blog Posts and Contact Us pages, ensuring users have direct access to helpful content and support options.
- Under the “Useful Links” section, we provide access to external resources, such as the Health and Safety Authority (HSA). This allows users to access important safety and regulatory information.

#### Policies:
- This section includes links to our Privacy Policy and Terms of Service. These links provide transparency and ensure users can easily review our terms and privacy practices.

#### Subscription Form:
- We also offer a subscription form to allow users to subscribe to updates from our site. The form is linked to a Mailchimp subscription service, and it requests users to enter their email address to receive notifications and news directly in their inbox.

Landing page on desktop
<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/footer-desktop.png"></details>

<br>
Landing page on mobile
<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/footer-mobile.png"></details>

### Home Page
This page provides a comprehensive and engaging user experience with a focus on showcasing products, services, and content related to Build Master Shop. Here’s a breakdown of the main sections and features:

#### Welcome Section
- A large hero section with a prominent heading that welcomes users to Build Master Shop.
- A brief description highlighting the store’s focus on high-quality power tools, workwear, and safety equipment.
- A call-to-action (CTA) button that directs users to browse the products available in the shop.

<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/welcome-section.png"></details>

#### Popular Categories
- This section presents the main product categories available at Build Master Shop. Each category is represented by an image and a brief description:
    - Power Tools for Construction: Showcasing high-performance tools designed for heavy-duty work.
    - Durable Workwear: Featuring tough and comfortable clothing for outdoor jobs.
    - Safety Equipment: Highlighting essential safety gear like gloves, helmets, and more.
- Each category includes a link to explore the respective product selection.

<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/popular-categories.png"></details>

#### Why Choose Us?

- A section dedicated to explaining the reasons why Build Master Shop stands out, with three key points:
    - Quality Guaranteed: Emphasizing product testing for durability and performance.
    - Expertise You Can Trust: Offering insights from a team with decades of experience.
    - Exceptional Customer Service: Highlighting customer service assistance before, during, and after the purchase.

<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/why-choose-us.png"></details>

#### Latest Blog Posts

- A dynamic display of the latest blog posts related to the products, tips, and industry news.
- The layout adjusts for different screen sizes (mobile, tablet, and desktop):
    - Mobile: Displays a single post.
    - Tablet: Displays two posts.
    - Desktop: Displays three posts.
- Each blog post includes the title, a brief description, and metadata such as the publication date and view count.
- A button at the bottom directs users to view all blog posts.

<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/latest-blogs.png"></details>

#### About Us

- A section providing detailed information about Build Master Shop, including the company’s history, mission, and values.
- It highlights the company’s dedication to providing high-quality products and supporting both professionals and DIY enthusiasts.

Each section is designed to engage users, provide valuable information, and encourage exploration of the website's offerings.

<details><summary>Click to view a screenshot of the feature</summary><img src="static/images/readme_images/features/about-us.png"></details>