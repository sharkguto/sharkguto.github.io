# Requirements Document

## Introduction

Este documento define os requisitos para tornar o site GMF-tech 100% responsivo focado para web e implementar testes unitários abrangentes para todos os componentes da aplicação. O objetivo é garantir uma experiência de usuário consistente em diferentes tamanhos de tela (desktop, tablet, mobile) e assegurar a qualidade do código através de testes automatizados.

## Glossary

- **Sistema**: A aplicação web GMF-tech desenvolvida em Flet
- **Componente**: Qualquer elemento visual ou funcional da aplicação (páginas, botões, formulários, etc.)
- **Breakpoint**: Ponto de quebra de layout baseado na largura da tela (mobile: ≤600px, tablet: 601-900px, desktop: >900px)
- **Teste Unitário**: Teste automatizado que verifica o comportamento de um componente isolado
- **Layout Responsivo**: Interface que se adapta automaticamente a diferentes tamanhos de tela

## Requirements

### Requirement 1

**User Story:** Como um usuário mobile, eu quero que o site se adapte perfeitamente à tela do meu dispositivo, para que eu possa navegar facilmente sem zoom ou scroll horizontal.

#### Acceptance Criteria

1. WHEN THE Sistema detecta uma largura de tela menor ou igual a 600px, THE Sistema SHALL renderizar o layout mobile com menu hambúrguer
2. WHEN THE Sistema detecta uma largura de tela entre 601px e 900px, THE Sistema SHALL renderizar o layout tablet com elementos redimensionados proporcionalmente
3. WHEN THE Sistema detecta uma largura de tela maior que 900px, THE Sistema SHALL renderizar o layout desktop com navegação horizontal completa
4. THE Sistema SHALL ajustar automaticamente tamanhos de fonte, espaçamentos e imagens baseado no breakpoint ativo
5. THE Sistema SHALL garantir que nenhum elemento cause scroll horizontal em qualquer breakpoint

### Requirement 2

**User Story:** Como um desenvolvedor, eu quero testes unitários para todos os componentes, para que eu possa garantir que mudanças futuras não quebrem funcionalidades existentes.

#### Acceptance Criteria

1. THE Sistema SHALL incluir testes unitários para todas as funções de criação de conteúdo das páginas (home_content, services_content, about_content, contact_content, currency_chart_content, portfolio_content)
2. THE Sistema SHALL incluir testes para as funções de tema (get_theme, get_button_style, get_text_style, get_shadow)
3. THE Sistema SHALL incluir testes para as funções de navegação e roteamento
4. THE Sistema SHALL incluir testes para validação de formulários (página de contato)
5. THE Sistema SHALL incluir testes para o sistema de cache da página de cotações

### Requirement 3

**User Story:** Como um usuário desktop, eu quero que todos os elementos visuais sejam proporcionais e bem distribuídos na tela, para que eu tenha uma experiência visual agradável.

#### Acceptance Criteria

1. WHEN THE Sistema renderiza cards de serviços em desktop, THE Sistema SHALL exibir 3 cards por linha com espaçamento uniforme
2. WHEN THE Sistema renderiza o portfólio em desktop, THE Sistema SHALL exibir 2 projetos por linha com imagens de 400px de largura
3. THE Sistema SHALL garantir que o header ocupe no máximo 8% da altura da viewport
4. THE Sistema SHALL garantir que o footer seja sempre visível no final do conteúdo sem sobrepor elementos
5. THE Sistema SHALL aplicar sombras e bordas arredondadas consistentes em todos os containers

### Requirement 4

**User Story:** Como um usuário tablet, eu quero que o conteúdo se ajuste adequadamente à minha tela, para que eu não perca informações importantes nem tenha elementos muito pequenos.

#### Acceptance Criteria

1. WHEN THE Sistema renderiza cards de serviços em tablet, THE Sistema SHALL exibir 2 cards por linha
2. WHEN THE Sistema renderiza o portfólio em tablet, THE Sistema SHALL exibir 2 projetos por linha com imagens redimensionadas
3. THE Sistema SHALL ajustar tamanhos de fonte para serem 10-20% menores que desktop mas maiores que mobile
4. THE Sistema SHALL manter todos os botões com área de toque mínima de 44x44 pixels
5. THE Sistema SHALL garantir espaçamento adequado entre elementos interativos (mínimo 8px)

### Requirement 5

**User Story:** Como um desenvolvedor, eu quero que os testes sejam executados automaticamente, para que eu possa validar rapidamente se o código está funcionando corretamente.

#### Acceptance Criteria

1. THE Sistema SHALL incluir um arquivo de configuração pytest para execução de testes
2. THE Sistema SHALL organizar testes em uma estrutura de diretórios espelhando a estrutura do código fonte
3. THE Sistema SHALL gerar relatórios de cobertura de código mostrando percentual de linhas testadas
4. THE Sistema SHALL executar todos os testes em menos de 30 segundos
5. THE Sistema SHALL incluir fixtures reutilizáveis para objetos comuns (page mock, theme colors, etc.)

### Requirement 6

**User Story:** Como um usuário mobile, eu quero que imagens e gráficos sejam otimizados para minha tela, para que o carregamento seja rápido e a visualização seja clara.

#### Acceptance Criteria

1. WHEN THE Sistema renderiza imagens do portfólio em mobile, THE Sistema SHALL redimensionar imagens para largura máxima de (viewport_width - 80px)
2. WHEN THE Sistema renderiza o gráfico de cotações em mobile, THE Sistema SHALL ajustar altura do gráfico para 300px
3. THE Sistema SHALL garantir que todas as imagens usem fit=COVER para evitar distorções
4. THE Sistema SHALL aplicar border_radius consistente em todas as imagens (8px)
5. THE Sistema SHALL carregar o gráfico de cotações de forma assíncrona com indicador de loading

### Requirement 7

**User Story:** Como um usuário, eu quero que formulários sejam fáceis de preencher em qualquer dispositivo, para que eu possa entrar em contato sem dificuldades.

#### Acceptance Criteria

1. THE Sistema SHALL validar que todos os campos obrigatórios do formulário de contato estejam preenchidos antes do envio
2. WHEN THE Sistema detecta campos vazios no envio, THE Sistema SHALL exibir mensagem de erro em SnackBar vermelho
3. WHEN THE Sistema envia formulário com sucesso, THE Sistema SHALL exibir mensagem de sucesso em SnackBar verde
4. THE Sistema SHALL limpar todos os campos do formulário após envio bem-sucedido
5. THE Sistema SHALL garantir que campos de texto tenham largura de 400px em desktop e 100% em mobile

### Requirement 8

**User Story:** Como um desenvolvedor, eu quero testes para o sistema de login, para que eu possa garantir que os modais e autenticação funcionem corretamente.

#### Acceptance Criteria

1. THE Sistema SHALL incluir testes para abertura do modal de login
2. THE Sistema SHALL incluir testes para cada método de login (Google, Apple, X)
3. THE Sistema SHALL incluir testes para fechamento do modal de login
4. THE Sistema SHALL incluir testes para exibição de SnackBar após tentativa de login
5. THE Sistema SHALL incluir testes para comportamento do WebView durante exibição do modal na página de cotações
