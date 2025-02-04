from PIL import Image
import os

# Dicionário com o caminho correto das imagens na pasta 'letras'
mapa_criptografia = {
    "a": "letras/Acriptografado.png",
    "b": "letras/Bcriptografado.png",
    "c": "letras/Ccriptografado.png",
    "d": "letras/Dcriptografado.png",
    "e": "letras/Ecriptografado.png",
    "f": "letras/Fcriptografado.png",
    "g": "letras/Gcriptografado.png",
    "h": "letras/Hcriptografado.png",
    "i": "letras/Icriptografado.png",
    "j": "letras/Jcriptografado.png",
    "k": "letras/Kcriptografado.png",
    "l": "letras/Lcriptografado.png",
    "m": "letras/Mcriptografado.png",
    "n": "letras/Ncriptografado.png",
    "o": "letras/Ocriptografado.png",
    "p": "letras/Pcriptografado.png",
    "q": "letras/Qcriptografado.png",
    "r": "letras/Rcriptografado.png",
    "s": "letras/Scriptografado.png",
    "t": "letras/Tcriptografado.png",
    "u": "letras/Ucriptografado.png",
    "v": "letras/Vcriptografado.png",
    "w": "letras/Wcriptografado.png",
    "x": "letras/Xcriptografado.png",
    "y": "letras/Ycriptografado.png",
    "z": "letras/Zcriptografado.png",
    " ": "letras/ESPACOcriptografado.png"
}

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

    # Calcula dimensões da imagem final concatenada
    largura_total = sum(imagem.width for imagem in imagens)
    altura_maxima = max(imagem.height for imagem in imagens)
    
    # Cria uma nova imagem com o tamanho combinado
    nova_imagem = Image.new("RGBA", (largura_total, altura_maxima))
    
    # Adiciona cada imagem lado a lado
    x_offset = 0
    for imagem in imagens:
        nova_imagem.paste(imagem, (x_offset, 0))
        x_offset += imagem.width
    
    # Salva a imagem final
    nova_imagem.save("texto_criptografado.png")
    print("Imagem gerada com sucesso! Nome: texto_criptografado.png")


# Exemplo: texto de entrada
entrada_usuario = input("Digite o texto para criptografar: ")
criar_png(entrada_usuario)