# Sanity

A mood viewer.

I keep a detailed journal on various KPIs every day and now I'm drowning in data, not having an intuitive place to pour it all in and look at the big picture. So I poured it in an xml file (each of my KPIs is a tag) and wrote a little javascript to conjure the big picture that I wanted to see. It looks like this:

![alt tag](https://raw.githubusercontent.com/MariaStoica/Sanity/master/img1.png)

Here, a Timepiece is a period of time, generally triggered by an epiphany. I want to monitor those because they lead to changes in habits and opportunities. I also want to see mood patterns. (I wrote a data generator to help me with development)

Mood Color Codes

Trigger    - Red
Happy      - Green
Default    - DarkSeaGreen
Frustrated - DarkKhaki
Chaos      - Maroon
Worried    - Gray
Sad        - SteelBlue
Pit        - Black

These are the names of CSS colors: https://en.wikipedia.org/wiki/Web_colors

Each column in the table is a day and the table is 365 columns long. For each column I display the significant activities for that day and I can see them by zooming in.

![alt tag](https://raw.githubusercontent.com/MariaStoica/Sanity/master/img2.png)