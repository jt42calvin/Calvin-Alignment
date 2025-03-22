# Calvin-Alignment

## Inspiration

The inspiration for this app came from a class exercise in CORE 290: Minorities in STEM. During the class, we were tasked with coming up with a list of characteristics we identify with and determining how those align with the student population at Calvin University. However, we quickly realized that it was much harder to come up with an accurate percentage. Everyone had results that varied widely across the class, and we struggled to find a reliable way to compare our individual characteristics with the larger student body. This class exercise sparked the idea for my app, an easy to use tool that would provide students with a clear view of how their characteristics align with the entire Calvin student population. 

## What I Learned

This project was my first experience building and hosting an app on Azure, and it taught me a lot about deploying and managing a cloud-based application. I learned how to create resources for apps and web services on Azure, which was a pretty much new to me. Also, I faced challenges working with the user interface, especially since I hadn’t worked with HTML and CSS in quite some time, nearly 10 years! I had to re-familiarize myself with these technologies to build a clean, functional frontend. 

Through this project, I also learned new skills with Flask, Python, and other libraries like Pandas and Matplotlib. It was my first time using these tools, and they made handling data, generating graphs, and presenting it all in a responsive way much more easy than I thought it would be. This project also forced me to take a deep dive into JavaScript and learn how to make interactive elements like dynamic data graphs that react to the user’s input, although this was not as difficult because I had prior experience with this in other projects. 

## How I Built the Project

I originally drafted a prototype for the app using Tkinter and just running it in Python through my terminal. However, I wanted to go really big for this hackathon and create something on the web that anyone can use. I talked with my friend Kenny and he suggested I look into using Flask and HTMX, which helped me build the backend much faster than I was hoping, which was super helpful for this timed hackathon. I used Flask to handle the backend logic and communicate with the Azure hosted database. For the frontend, I built a simple HTML interface and utilized Matplotlib to generate the graphs based on the user’s survey input. 

My app allows users to see how their characteristics (such as gender, ethnicity, and church affiliation) align with the entire Calvin student population, based on an anonymized dataset I requested from Calvin Admissions. Then, by comparing the user’s input to the survey, the app generates pie charts and bar graphs that make the comparison visual.

## Challenges Faced

One of the biggest challenges I faced was working on this project solo. I didn’t have any teammates, which meant I was responsible for all aspects of development, from backend to frontend. While I wanted to push myself to deliver a quality project, I sometimes felt overwhelmed by the time constraints and the need to meet my own personal standards. The lack of a team also meant that I didn’t have anyone to bounce ideas off of, so there were many moments where I had to solve problems on my own, which was both challenging and rewarding. Maybe I'm destined to be a freelance full-stack dev hahaha.

The UI/UX was another hurdle. HTML and CSS are a bit rusty for me, and I spent a lot of time tweaking the layout and design to make sure it looked clean and functional. Honestly I think I spent most of my time getting something that looked half decent. There were also moments when I felt frustrated because it seemed like the project wasn’t coming together as smoothly as I wanted. However, by pushing through, I learned a lot about the process of designing, coding, and deploying an app.

## Final Thoughts

Despite my challenges, I’m really proud of how this project turned out. Given the time constraints and difficulties I faced working alone, it's very rewarding to see the app come to life. I am so proud of myself for attempting this hackathon and feeling like I have something worth showing off. I’ve learned so much about working with Azure, Flask, and creating a "dynamic, data-driven" web applications. In the end, I’m very happy with the final product and I’m excited to share it with others. For my presentation, I’ve created a QR code linking directly to the app so that anyone can try it for themselves, it's fun to see how people compare to the Calvin student population.

This project not only helped me improve my technical skills but also gave me the opportunity to build something meaningful that could help others gain a deeper understanding of their personal identity and how they fit within the broader community.