# Hangman-CoC (Country or City)

## Code Institute: Milestone Project 3

### Python Essentials: A command-line application

![Responsive]

[Click here to view the live project.]

[Click here to view the repository.]

## Table of Contents:
- [User Experience (UX)]  

- [Features]

- [Technologies Used]
  
- [Testing]

- [Deployment]

- [Credits]

- [Acknowledgements]
    

## User Experience (UX)

-   ### Introduction
     Hangman-CoC is a Python based game, which runs in the Code Institue mock terminal on Heroku.
     It is a challenging word search game involving user interaction to guess a word which would be a name of a country or a city. The game has two difficulty levels which users can select at the start of the game. Users have to guess the letters of the hidden word with limited number of lives which vary based on the difficulty level. Each wrong guess takes away one life. The game is over either when the user has correctly guessed the word or there are no lives remaining.
     
-   ### How to Play
     Users can play Hangman_CoC using mock terminal. 
     -  User will be prompted to enter name to start the game. 
     -  User will be promoted to select difficulty level. 
        - Easy and Hard are the two difficulty levels. 
        - Easy has 7 lives to guess the word while Hard has 5 lives.
     -  Upon selecting the difficulty level, the game starts with an aim to guess the hidden word. The hidden word is represented by _ _ _ _ which display users the number of letters in the word. 
     - User now have to guess the letters that would make the word.
        - With each correct guess, the _ is replaced with the correct letter. 
        - With each incorrect guess, one life is deducted. This is visualize graphically using hangman. 
     - The game is over either when the user has correctly guessed the word or they have run out of lives. 
     - Users can either choose to restart or quit the game.

     
-   ### Audience
     The application is aimed for enthusiasts who like to play guess the word game. People from all ages and different background can play this challenging and interactive game.

-   ### User stories

    -   #### First Time Visitor
        1. I want to be able to start the game easily.
        2. I should easily understand the instructions of the game. 
        3. I want the game to run easily which would keep me engrossed.

    -   #### Returning Visitor
        1. I should find the game challenging with different difficulty levels.
        2. I should enjoy the game.   

    -   #### Frequent User 
        1. 
        2. 

*   ### Design

    - [Code Logic Flowchart]

    
    
## Features

 ### Existing Features

   

 

- ### Future Enhancements 

    - 
    - 

## Technologies Used

- ### Languages Used

  -   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


- ### Frameworks, Libraries & Programs Used

  
  - [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
  - [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.   
  - [Lucidchart:](https://www.lucidchart.com/)
    - Lucidchart was used to create the flowchart during the inital phase.
    
## Testing

  



 - ### Further Testing

   -   
   

  - ### Known Bugs

    -   

## Deployment

 - ### GitHub Pages

  The project was deployed via [Heroku](https://heroku.com/) using the following steps...

  - Creating Application on Heroku.
    - Ensure all codes are correct and ready for deployment.
    - Log in to Heroku with your credentials.
    - Navigate to the Dashboard.
    - Click "New" and from the drop down menu select "create app". This is located on the upper right side of the window.
    - Provide a name for your application which has to be unique and select your region.
    - Click "Create App".

  - Setting up the Application
    - Navigate to "Settings". Scroll to "Config Vars" and select "Reveal Config Vars". Input the following. KEY: PORT, VALUE:8000. The project does not have any confidentail data hence no additional steps needed.
    - Then scroll and select "Buildpacks" and then click both "python" and "node.js"(node.js is needed for the mock terminal).
    - Ensure that the python buildpack is above the node.js buildpack, You can click and drag the packs to re-arrange them.
    
  - Application Deployment
    - Navigate to the "Deploy" section.
    - Scroll down to "Deployment Method" and select "GitHub".
    - Authorize the connection of Heroku and GitHub.
    - Search for your GitHub repository name, and select the correct repository.
    - For Deployment there are two options, Automatic Deployments or Manual.
      - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
      - Manual Deployment: This will only prompt Heroku to build your app when you manually opt to do so.
    - Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment.

   


 - ### Making a Local Clone

    1. Log in to GitHub and navigate to the [GitHub Repository]
    2. To clone the repository using HTTPS, click Code and copy the address. 
    ![Clone Repository]
    3. Navigate to Git Bash and clone the repository. 
    ![Clone-Command]
    4. Press Enter and your local clone will be created. 
    ![Clone-Output]

## Credits

  - ### Code
    

  - ### Content
    

## Acknowledgements

  -   My Mentor for continuous helpful feedback and advises.
  -   Slack community and my fellow slackers for being available at any given time of the day.


## [BACK TO TOP]