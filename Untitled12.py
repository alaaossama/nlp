#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[2]:


import nltk
from nltk.chat.util import Chat, reflections


# In[3]:


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you",
  "yo soy"     : "tu eres",
  "Yo era"     : "tú eras",
  "Yo"         : "tú",
  "soy"        : "tú eres",
  "yo"         : "tú lo harías",
  "yo tengo"   : "tú tienes",
  "yo haré"    : "tú lo harás",
  "tú eres"    : "yo soy",
  "tú eras"    : "yo era",
  "tienes"     : "tengo",
  "tú"         : "lo haré",
  "tu"         : "mi"
}


# In[4]:


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
         r"what is your name ?",
        ["I am a bot created by nlp . you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
         r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
        ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
         r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
     [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ], 
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo estás hoy?",]
    ],
    [
        r"hola|hola|hola",
        ["Hola", "Hola",]
    ],
    [
         r"¿Cuál es tu nombre?",
        ["Soy un bot creado por nlp . ¡Puedes llamarme loco!",]
    ],
    [
        r"¿cómo estás?",
        ["Estoy bien. ¿Qué hay de ti?",]
    ],
    [
        r"lo siento (.*)",
        ["Está bien","Está bien, no importa",]
    ],
    [
         r"Estoy bien",
        ["Es genial escuchar eso, ¿cómo puedo ayudarte?",]
    ],
    [
        r"estoy (.*) bien",
        ["Es bueno escuchar eso","¿Cómo puedo ayudarte? :)",]
        ],
    [
        r"¿Qué (.*) quieres?",
        ["Hazme una oferta que no pueda rechazar",]
    ],
    [
        r"(.*) creado?",
        ["Raghav me creó usando la biblioteca NLTK de Python", "top secret;)",]
    ],
    [
        r"(.*) (ubicación|ciudad) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"¿Cómo está el tiempo en (.*)?",
        ["El clima en %1 es increíble como siempre","Muy caluroso aquí en %1","Muy frío aquí en %1","Ni siquiera he oíd de %1"]
    ],
    [
         r"trabajo en (.*)?",
        ["%1 es una empresa increíble, he oído hablar de ella. Pero tienen grandes pérdidas en estos días",]
    ],
    [
        r"(.*)lluvia en (.*)",
        ["No ha llovido desde la semana pasada aquí en %2","Maldita sea, está lloviendo demasiado aquí en %2"]
    ],
    [
        r"cómo (.*) salud (.*)",
        ["Soy un programa de computadora, así que siempre estoy saludable",]
    ],
     [
        r"(.*) (deportes|juego) ?",
        ["Soy un gran fanático del fútbol",]
    ],
    [
        r"¿quién (.*) deportista?",
        ["Desordenado","Ronaldo","Roony"]
    ], [
        r"¿quién (.*) (estrella de cine|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"Estoy buscando guías y cursos en línea para aprender ciencia de datos, ¿puede sugerirme?",
        ["Crazy_Tech tiene muchos artículos excelentes con la explicación de cada paso junto con el código que puede explorar"]
    ],
    [
        r"salir",
        ["BBye, cuídate. Nos vemos pronto :) "," Fue un placer hablar contigo. Hasta pronto :)"]
    ],
    
]


# In[ ]:


def chat():
    print("Hi! I am a chatbot created by nlp for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()


# In[ ]:




