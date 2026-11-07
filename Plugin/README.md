# JVPLEY ETS2 Telemetry Plugin (Windows x64)

## Implementado no código
- Plugin nativo compilado como biblioteca dinâmica Windows x64 (JVPLEY_ETS2.dll).
- Integração com o framework Rust para a API pública SCS Telemetry SDK.
- Assinatura de velocidade, RPM, marcha, distância de navegação, tempo de rota e limite de velocidade.
- Registro de inicialização, pausa, retomada e amostras de telemetria no log do jogo.
- Build automatizado em GitHub Actions.

## Estado de validação
O código-fonte do plugin foi adicionado e a compilação Windows x64 está sendo executada pelo GitHub Actions. Até a compilação terminar com sucesso, não há um binário confirmado para baixar. Mesmo após gerar a DLL, ainda será necessário testar o carregamento e os dados em uma instalação real do ETS2 1.61.

Não instale uma DLL de build antiga ou marcada como scaffold. Use somente o artefato chamado JVPLEY-ETS2-x64-DLL, depois de confirmar que a execução correspondente terminou com sucesso.

## Limites desta primeira etapa
A DLL registra os dados no log do ETS2. A comunicação direta com a interface JVPLEY.exe (named pipe ou memória compartilhada) ainda será implementada em uma etapa posterior. Portanto, a telemetria ainda não aparece automaticamente na tela JVPLEY.

## Compatibilidade
O plugin declara suporte ao jogo ETS2 a partir do schema de telemetria 1.14 e usa Telemetry API 1.01. Isso não substitui o teste no ETS2 1.61: a compatibilidade efetiva será confirmada em execução.

## Referências
- SCS Telemetry SDK: https://modding.scssoft.com/wiki/Documentation/Engine/SDK/Telemetry
- Implementação de referência do framework SCS SDK: https://github.com/AptS-1547/scs-sdk-crates

## Instalação futura
Quando a DLL for compilada e validada, o destino esperado será:
Euro Truck Simulator 2/bin/win_x64/plugins/JVPLEY_ETS2.dll

Não copie o arquivo para a pasta do jogo antes da validação. Nunca renomeie um arquivo de texto ou Python para .dll.
