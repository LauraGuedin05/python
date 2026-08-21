from flask import Flask

app = Flask(__name__)

@app.route('/')
def curriculo():
    nome = "Laura Guedin"
    email = "lauraguedin3@gmail.com"
    telefone = "(31) 99254-5926"
    instagram = "@laaguedin"
    escola = "Escola Técnica do COTEMIG"
    
    habilidades = [
        "MySQL", "C#", "N8N", "Kotlin", "Swift", "Flutter", 
        "React", "Python", "Git", "HTML", "CSS", "Tailwind CSS", 
        "JavaScript", "APIs", "Supabase", "Postgres"
    ]
    
    badges_habilidades = "".join([
        f'<div style="padding: 8px 14px; background: #f3f3f3; border-radius: 8px;">{habilidade}</div>' 
        for habilidade in habilidades
    ])

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Currículo - {nome}</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; }}
            a {{ color: #0366d6; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div align="center" style="padding: 20px;">
          <h1 style="margin-bottom: 5px;">👋 {nome}</h1>
          <p style="font-size: 16px; color: #555;">
            Programador • Estudante de Tecnologia • Focado em React e projetos próprios
          </p>
        </div>

        <hr/>

        <section style="max-width: 900px; margin: auto; padding: 20px;">
          <h2>🚀 Sobre mim</h2>
          <p>
            Tenho 17 anos e sou estudante da <strong>{escola}</strong>, atualmente atuando na área de tecnologia.
            Sou apaixonada por desenvolvimento de software e estou focada na criação de <strong>projetos próprios</strong> e no
            crescimento da minha <strong>empresa pessoal</strong>, utilizando principalmente <strong>Flutter e Python</strong>.
          </p>
          <p>
            Busco constantemente evoluir como desenvolvedora, aplicando boas práticas, aprendendo novas tecnologias
            e criando soluções eficientes e escaláveis.
          </p>

          <hr/>

          <h2>🧠 Tecnologias & Ferramentas</h2>
          <div style="display: flex; flex-wrap: wrap; gap: 10px;">
            {badges_habilidades}
          </div>

          <hr/>

          <h2>📚 O que estou estudando atualmente</h2>
          <ul>
            <li>Desenvolvimento avançado com <strong>React (puro), Flutter e Swift</strong></li>
            <li>Arquitetura de projetos Front-end</li>
            <li>Consumo e integração de APIs</li>
            <li>Boas práticas de código e versionamento</li>
            <li>Criação e escalabilidade de produtos digitais</li>
            <li>Automações em N8N</li>
          </ul>

          <hr/>

          <h2>💼 Projetos em destaque</h2>
          <ul>
            <li>🔹 Projetos pessoais em React e Python</li>
            <li>🔹 Aplicações web com foco em performance e UX</li>
            <li>🔹 Sistemas integrados com APIs</li>
          </ul>
          <p style="color: #666; font-size: 14px;">
            *(Em constante evolução — novos projetos em breve!)*
          </p>

          <hr/>

          <h2>🎯 Objetivos profissionais</h2>
          <ul>
            <li>Consolidar minha carreira como desenvolvedor</li>
            <li>Criar soluções tecnológicas de impacto</li>
            <li>Expandir minha empresa pessoal</li>
            <li>Aprimorar habilidades em Front-end e arquitetura de software</li>
          </ul>

          <hr/>

          <h2>📫 Contato</h2>
        </section>

        <div align="center" style="padding: 20px; color: #777;">
          <p>💡 Sempre aberto a novas oportunidades, desafios e conexões.</p>
        </div>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
