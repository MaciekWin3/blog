# Welcome to My Blog 🌐

Hi this is my personal blog.

## Tech stack 📝

Creating a similar project has been on my mind for quite some time, but I often found myself overengineering it. This time, I opted for simplicity, and here's my current tech stack:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Bulma.css](https://bulma.io/)
- [Alpine.js](https://alpinejs.dev/)

## How it works 🤔

Basically, the app for my blog is hosted on a cheap virtual machine (VM). Flask is responsible for all the backend operations, while Alpine.js and Bulma.css handle the frontend. You might be wondering, "Where are the blogs stored?" Well, I use a GitHub repository as storage for my articles, retrieving them via the GitHub API. This approach eliminates the need for a complicated solution to create blog posts; instead, I simply make a commit to my own repository.
