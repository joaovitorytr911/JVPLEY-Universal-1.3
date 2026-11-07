# JVPLEY Universal 1.3

Projeto em desenvolvimento para uma central multimídia com visual futurista azul, inicialmente direcionado ao Windows 11 e à experimentação com Euro Truck Simulator 2.

## Conteúdo atual
- `app.py`: protótipo visual desktop feito com Tkinter (biblioteca padrão do Python).
- Interface demonstrativa com relógio e cartões de navegação, áudio, telemetria e conexão.

## Executar o protótipo no Windows 11
1. Instale Python 3.10 ou superior.
2. Baixe o repositório pelo botão **Code > Download ZIP**.
3. Extraia o ZIP.
4. Abra o PowerShell na pasta extraída.
5. Execute: `python app.py`

## Estado real do projeto
Esta é uma primeira estrutura/protótipo. GPS, Spotify, chamadas, leitura real de telemetria do ETS2, suporte universal a caminhões, instalador MSI e plugin do jogo **ainda não estão implementados nem testados**. Os cartões exibem apenas informações de demonstração; não representam dados do veículo.

## Próximas etapas
1. Validar o protótipo no Windows 11.
2. Definir e implementar a integração de telemetria do ETS2 1.61.
3. Projetar a comunicação com a central multimídia Android.
4. Criar instalador MSI somente depois de o aplicativo estar funcional e testado.

## Segurança
Não opere a interface enquanto conduz. Faça todos os testes com o veículo parado.


## Gerar o executável Windows
O GitHub Actions possui um fluxo em `.github/workflows/build-exe.yml` que compila `app.py` em `JVPLEY.exe` usando Windows.

- O fluxo é iniciado ao enviar alterações em `app.py` ou manualmente pela aba **Actions**.
- Quando terminar com sucesso, abra a execução e baixe o artefato **JVPLEY-Windows-EXE**.
- O artefato fica disponível por 14 dias.

O EXE é apenas o protótipo visual atual; integrações com GPS, Spotify, chamadas e telemetria ainda não existem.
