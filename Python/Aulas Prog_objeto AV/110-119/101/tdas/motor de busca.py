# Motor de Busca da Web

def obter_pagina(url):  # procedimento para conecção com a web
    try:                # Este comando garante que este procedimento sege executado primeiro
        impot (urllib)
        return urllib.urlopen(url).read()
    except:
        return ""

def rastreador_da_web (semente):    # Procedimento de iniciação do web crawler
    tocrawl = [semente]            # comando gerador do indice
    rastreador = []
    grafico = {}
    indice = {}
    while tocrawl:
        if pagina not in rastreador:
            conteudo = obter_pagina (pagiana)
            adicionar_pagina_ao_indice (indice, pagina, conteudo)
            outros_links = obter_todos_os_link (conteudo)
            grafico [pagina] = outros_links
            uniao (tocrawl, outros_links)
            rastreador.append (pagina)
        return indice, grafico
cache = {
    'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>






""", 
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""", 
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>




""", 
}

def obter_pagina (url):
    if url in cache :
        return cache [url]
    else:
        return Nenhum
def obter_proximo_alvo(pagina) :
    iniciar_link = pagina.find('<a href=')  #<a href= o inicio de um link
    if iniciar_link == -1:
        return Nada, 0
        iniciar_quote = pagina.find('"', iniciar_link)
        fim_quote = pagina.find ('"', iniciar_quote +1)
        url = pagina[iniciar_quote + 1: fim_quote]
    return url, fim_quote

def obter_todos_links(pagina):
    links = []
    while True:
        url, endpos = obter_proximo_alvo(pagina)
        if url:
            links.append(url)
            pagina = pagina[endpos:]
        else:
            break
        return links

def adicionar_pagina_ao_indice(indice, url, conteudo):
    palavras = conteudo.split()
    for palavra in palavras:
        adicionar_ao_indice(indice, palavras, url)

def adicionar_ao_indice (indice, palavra_chave, url):
    if palavra_chave in indice:
        incide[palavra_chave].append(url)
    else:
        indice[palavra_chave] = [url]

def pesquisa(indice, palavra_chave):
    if palavra_chave in indice:
        return indice[palavra_chave]
    else:
        return Nada

indice, grafico = rastreador_da_web('http://udacity.com/cs101x/urank/index.html')
if 'http://udacity.com/cs101x/urank/index.html' in grafico:
    print (grafico['http://udacity.com/cs101x/urank/index.html'])