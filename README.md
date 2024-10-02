<div align="center">
  <img width=600px height=430px src='https://github.com/user-attachments/assets/06d62597-ad80-48b0-ae21-106fddd1c4d5'>
  <br>
  <img src="http://img.shields.io/static/v1?label=language&message=python&color=rgb(246,120,40)&style=plastic">
</div>

<h2>O que é e como funciona?</h2>
<p>
  O 'Have ClickJacking?' é um scanner de ClickJacking para sites. Utilizando a função <code>hcj()</code>, tendo como parâmetro a URL do site no formato <code>domain.tld</code>, e também com as funções da biblioteca <code>requests</code>, o código analisa as diretivas X-Frame-Options e CSP do cabeçalho HTTP do site e a partir da análise conclui a vulnerabilidade dele. O valor retornado pela função é um dicionário com valor booleano para 'ClickJacking', e o valor das supracitadas diretivas com as chaves sendo seus respectivos nomes de protocolo e, caso a chave 'ClickJacking' tenha o valor <code>True</code> , um arquivo HTML de nome <code>hcj_domain.tld.html</code> é criado com <code><iframe></code> importando o referido site.
</p>

<h2>Exemplo de uso</h2>
<p>
  1. Neste exemplo, o site "example.com" é vulnerável ao ClickJacking, as diretivas de proteção à esta falha no cabeçalho HTTP são inexistentes e o algoritimo automaticamente criará um arquivo HTML chamado "hcj_example.com.html" que importa o site.
  
  ```python
    from hcj import hcj

    site = 'example.com'

    print(hcj(site))

    Output: {'ClickJacking': True, 'X-Frame-Options': '', 'Content-Security-Policy': ''}
  ```

  2. Neste exemplo, o site "google.com" não é vulnerável ao ClickJacking, pois sua diretiva "X-Frame-Options" está marcada como "SAMEORIGIN". Neste caso o arquivo HTML não é criado.

  ```python
    from hcj import hcj

    site = 'google.com'

    print(hcj(site))

    Output: {'ClickJacking': False, 'X-Frame-Options': 'SAMEORIGIN', 'Content-Security-Policy': ''}
  ```
</p>

<h2>Motivação</h2>
<p>Escrevi tal código como uma forma de me reaproximar da área de cibersegurança, e treinar minha capacidade de filtrar bugs. O público-alvo então, como já se imagina, são estudantes da segurança digital, pentesters, equipes de bug bounty e hackers éticos no geral.</p>

<h2>Considerações finais</h2>
<p> A falha de ClickJacking possui valor baixo na maioria dos serviços de bug bounty, e cabe ao hacker argumentar sobre sua capacidade de impacto com as empresas inscritas no serviço. Um exemplo disso é o ClickJacking pode ser feito em telas de login, o que é perigoso e rende certo bounty. Mas outra coisa é o phishing ser feito em uma tela onde não há entrada para informações pessoais.</p>
