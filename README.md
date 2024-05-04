# OxPhysCopiliot
**NOTE: I KNOW I MISSPELT COPILOT IN THE REPO NAME. I'M SORRY. I CAN'T BE BOTHERED CHANGING IT NOW.**

### Description
This repository contains the code I will using to demonstrate some uses of Copilot through the example of
plotting an HR diagram at the Oxford Physics Department's coding lecture series. 
I have included all the material needed for individual learners to go through the material on their own, and for teachers
to use this material as a base for their own tutorial. 

#### Python Requirements
* Python 3+
* Pytest
* Matplotlib
* Pandas

#### Problem? Question? Suggestion?
Start a GitHub issue on this repo! If I don't respond, email hfstevance@gmail.com

## For Learners
If you are going through this repository on your own without a teacher present you can still use all the resources in 
this repository. 

* **Make sure you have Copilot running** in your Integrated Development Environment (IDE) of choice (see below if needed).
* Create a new file called `plot_HRDiagram.py`
* Open the file `plot_HRDiagram_teacherversionwithnotes.py` and start **writing the code** in your new file.
* When you get to STEP 8, I recommend starting a new_utils.py file where you can copy the code from the utils.py file to see how Copilot begins filling in based on the comments 

#### Why do I need to write the example code rather than copy paste the lines?
1) The point is for you to see how Copilot starts filling in for you. If you just copy paste full lines, although you will see 
Copilot's suggestions for the next lines you won't see where and how quickly it starts making suggestions.

2) Generally you learn very little from copy pasting code. Actually typing the code out and interacting with the syntax yourself is the fastest way to learn.


### How to get Copilot for free?
If you are students or an educator you can get the PRO version of GitHub for free which will give you access to Copilot.
You need to apply and get verified which you can do [here](https://education.github.com/discount_requests/application)

To get Copilot running in you IDE you'll likely need to isntall a pluggin. 
* [VSCode](https://code.visualstudio.com/docs/copilot/getting-started)
* PyCharm: `Settings` > `Plugins` > `search for copilot`
* [Vim/NeoVim](https://github.com/github/copilot.vim)


## Slide-free Cliffnotes

### What is Copilot?
Copilot is an AI pair programmer. It is not the same as Microsoft Copilot (it is Bing Chat with a different name, and Clippy's grandchild in Microsoft Lore).
It is also not the same as ChatGPT (although it is based on the same kind of Large Language Model technology).
Chat GPT is trained on a large corpus of text (mostly from the internet in the case of 3.5) that is not code specific (but includes a lot of code so GPT is pretty good at coding).
Copilot is trained on a large corpus of code (GitHub is choke-full of it) and is specifically designed for software development. 

### What is a Large Language Model? 
This is a big question. The main take-aways are:
* They are very large (billions of parameters) Transformer models. If you don't know what that means that's cool but it gives you a word to google if you need it. 
* Their task is to predict the next word in a sequence of words. This is done by training the model on a large corpus of text and then sometimes fine-tuning it on a specific task.
* **They are essentially word calculators**. They don't understand language in the way we do. They don't understand anything. They are just very good at predicting the next word in a sequence of words.
* They don't yet have the ability to "know when they don't know". So sometimes they will confidently give you the wrong answer. Some people call this "hallucinations", I think it's marketting bulsh*t to avoid saying the model is wrong, and to make it sound more like a human.

### What are some cool things Copilot can do?
* If you write a comment with what you want the next bit of code to do, Copilot will often fill in the code for you.
* If you have code already written and start typing in a comment, it is good at documenting the code for you.
* It can help you write tests because copilot knows about the code you wrote in the other files in your repository
* It can help you write code in other languages you are not familiar with and learn them faster as a result
* I find the **copilot chat a useful learning tool** because you can have a conversation with it about new concepts. 
For example ask copilot (or chat GPT) to summarise the basics of Django REST API. Then pick one bit of the summary that wasn't 
so clear for you and ask more detail. The rapid itteration from question to answer makes "reading manuals" much more engaging and intuitive. 

### How do I know if Copilot is wrong?
* Usually it's obvious when Copilot is makign things up or repeating itself. But it it's not...
* The code will crap out and give you an error. You can give this error to the copilot chat and it will help you debug. 

#### What about silent errors?
* That's why you need good testing practices. The same can happen with a human programmer. 



## For Teachers
I didn't add the slides to this repository because the key messages are in the cliffnotes below. If this is the first time you are demonstrating this code I recommend going through the `For Learners` section to familiarise yourself. 

#### How to structure the session
* **Introduce yourself** and your coding past and everyday experience. Telling 
your learners how your everyday coding experience has changed since using Copilot is a great way to get them engaged. 
* **Make Motivations**: If you are teaching scientists and more senior astronomers they may be reluctant/sceptical at the idea of using an A.I. tool. 
You can emphasise the **time saving** aspects, but also stress that these tools are now **commonplace** in industry.
**LLMs and the basics of [prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)** are now essential transferable skills. 
* **I DO NOT RECOMMEND TRYING TO GET YOUR CLASS TO INSTALL COPILOT**. Even if everyone has already got a Github pro account this could take you a whole hour of trouble shooting. 
* Instead, **go through the code as a learner** on a projected screen so that your class can see the suggestions Copilot makes. 
* Encourage your learners to **ask questions as you are coding**. It can be overwhelming to live code and answer questions but often these queries are better treater in situ
* **Leave 10-15 minutes at the end** to try prompt suggestions from the class.

#### TIP:
Including personal experiences or screenshots of where Copilot has failed is also a great way to show that although it is a powerful tool it is, at the end of the day,
just a really well-informed word generator. They can often be funny so it can add levety to your lesson.