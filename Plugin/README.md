# JVPLEY ETS2 Plugin (Windows x64)

## Estado verificado
Esta pasta contém apenas a documentação inicial. Não foi confirmado neste repositório um binário DLL funcional do JVPLEY. Portanto, ainda não instale nada na pasta do jogo.

## Como a integração será feita
O plugin precisa ser uma DLL x64 que implemente as funções de exportação e callbacks definidos pelo SCS Telemetry SDK. Depois, ele enviará os dados de telemetria ao aplicativo JVPLEY por uma interface local documentada.

## Referência oficial
- SCS Telemetry SDK: https://modding.scssoft.com/wiki/Documentation/Engine/SDK/Telemetry
- A página oficial informa que o SDK inclui documentação e exemplos. A versão do SDK não é a mesma numeração da versão do jogo; a compatibilidade específica com ETS2 1.61 precisa ser conferida no SDK e validada em teste.

## Destino esperado após compilação e validação
`Euro Truck Simulator 2/bin/win_x64/plugins/JVPLEY_ETS2.dll`

## Critérios antes de distribuir
1. Implementar a API usando os headers oficiais do SDK.
2. Compilar em Windows x64.
3. Confirmar que o ETS2 carrega a DLL sem erro.
4. Verificar telemetria real e a comunicação com o JVPLEY.exe.
5. Publicar o binário somente depois dos testes.

**Importante:** não renomeie um arquivo de texto ou Python para `.dll`. Isso não cria um plugin válido.
