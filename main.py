from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  temperature=0.1,
  messages=[
    {"role": "system", "content": "Уяви, що ти професіонал у сфері компʼютерної лінгвістики та штучного інтелекту. Твоя головна спеціалізація - робити синтаксичну розмітку речення, використовуючи граматику залежностей. Використовуй теги з Universal Dependencies.  Твої відповіді лаконічні. Тобі в якості питання задають речення, яке ти повинен розмітити. Твоя відповідь - беспосередньо синтаксина розмітка речення з використанням граматики залежностей. Не пиши будь ласка нічого крім розмітки. Відповідь повинна мати таку структуру - cписок з елементів, які відображають слово, відповідний тег та його опис"} ,
    {"role": "user", "content": "Я ходжу до школи щодня, але мені це не дуже подобається"}
  ]
)

print(completion.choices[0].message.content)