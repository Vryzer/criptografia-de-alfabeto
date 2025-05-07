from PIL import Image
import os
import string

def criar_mapa_criptografia():
    mapa_cripto = {}
    caracteres_especiais = {
        ' ':'ESPACO',
        'ç':'Ç',
        ',':'VIRGULA',
        '.':'PONTOFINAL'
    }
    for letra in string.ascii_uppercase:
        mapa_cripto[letra.lower()] = f"letras/{letra.upper()}criptografado.png"
    for char, prefixo in caracteres_especiais.items():
        mapa_cripto[char] = f"letras/{prefixo}criptografado.png"
    return mapa_cripto

mapa_criptografia = criar_mapa_criptografia()

def criar_png(texto):
    imagens = []
    
    # Carregar imagens correspondentes às letras
    for letra in texto.lower():
        caminho_imagem = mapa_criptografia.get(letra)
        if caminho_imagem and os.path.exists(caminho_imagem):
            imagens.append(Image.open(caminho_imagem))
        else:
            print(f"Imagem não encontrada para '{letra}', ignorando...")

    if not imagens:
        print("Nenhuma imagem válida encontrada.")
        return

    #Determinando largura e altura em pixels, como um quarto de uma folha a4. Isso vai servir para contar as linhas caso fique uma mensagem enorme, pois sem isso ficaria tudo na mesma linha.
    #Por curiosidade, um exemplo da folha a4, com 210mm x 297mm, convertendo para pixels, fica 2480 e 3508.
    largura_maxima = 620
    altura_maxima = 877
    
    #inicializa as dimensões da imagem formada, tudo no ponto 0,0.
    x_offset = 0
    y_offset = 0
    linha_atual_altura = 0
    
 # A definição do RGBA está baseada na cor de fundo das fotos da pasta "letras". Caso você mude as letras e tenha uma outra cor de fundo, mude os valores usados em (217, 196, 142, 255)
    nova_imagem = Image.new("RGBA", (largura_maxima, altura_maxima), (217, 196, 142, 255))

    for imagem in imagens:
        largura, altura = imagem.size

        # Quebra de linha se a largura ultrapassar a máxima permitida
        if x_offset + largura > largura_maxima:
            x_offset = 0
            y_offset += linha_atual_altura
            linha_atual_altura = 0

        # Verificar se a imagem ultrapassaria o limite da folha
        if y_offset + altura > altura_maxima:
            print("Conteúdo ultrapassou o limite da folha A4. Truncando...")
            break

        # Colar imagem na posição correta
        nova_imagem.paste(imagem, (x_offset, y_offset))
        x_offset += largura
        linha_atual_altura = max(linha_atual_altura, altura)

    # Salva a imagem final
    nova_imagem.save("texto_criptografado.png")
    print("Imagem gerada com sucesso! Nome: texto_criptografado.png")


# Exemplo: texto de entrada
entrada_usuario = input("Digite o texto para criptografar: ")
criar_png(entrada_usuario)

