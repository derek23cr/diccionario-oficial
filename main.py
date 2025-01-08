
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "FOMO": "Miedo a perderse algo, especialmente en redes sociales",
    "YOLO": "Aprovechar al máximo cada momento, ya que solo se vive una vez",
    "TROLL": "Persona que intenta provocar a otros en internet con comentarios provocativos",
    "MEME": "Imagen o video viral que se difunde rápidamente en internet",
    "SMH": "Sacudir la cabeza, usado para expresar incredulidad o desaprobación",
    "BTW": "Por cierto, abreviatura comúnmente usada en mensajes de texto",
    "BFF": "Mejor amigo/a para siempre"}

while True:
    unknown = input('Esquiba la palabra que no entiende:')
    if unknown in meme_dict.keys():
        print(meme_dict[unknown])
    elif unknown == '0':
        break
    else:
        print('La palabra no esta en el memecionario')
