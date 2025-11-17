# Design Document

## Overview

Este documento descreve o design técnico para implementar responsividade completa focada em web e testes unitários abrangentes para a aplicação GMF-tech. A solução inclui melhorias no sistema de breakpoints, otimização de layouts para diferentes tamanhos de tela, e uma suite completa de testes usando pytest.

## Architecture

### Responsive Design System

A arquitetura de responsividade será baseada em três camadas:

1. **Breakpoint Detection Layer**: Sistema centralizado para detectar e gerenciar breakpoints
2. **Layout Adaptation Layer**: Componentes que se adaptam baseado no breakpoint ativo
3. **Theme System Enhancement**: Extensão do sistema de tema para incluir valores responsivos

### Testing Architecture

A arquitetura de testes seguirá o padrão AAA (Arrange, Act, Assert):

1. **Test Fixtures**: Objetos mock reutilizáveis (Page, Controls, etc.)
2. **Unit Tests**: Testes isolados para cada componente
3. **Integration Tests**: Testes de fluxo entre componentes
4. **Coverage Reports**: Relatórios de cobertura usando pytest-cov

## Components and Interfaces

### 1. Responsive Utilities Module (`utils/responsive.py`)

```python
class Breakpoint(Enum):
    MOBILE = "mobile"      # <= 600px
    TABLET = "tablet"      # 601-900px
    DESKTOP = "desktop"    # > 900px

class ResponsiveConfig:
    """Configurações responsivas centralizadas"""
    
    @staticmethod
    def get_breakpoint(width: int) -> Breakpoint
    
    @staticmethod
    def get_font_size(base_size: int, breakpoint: Breakpoint) -> int
    
    @staticmethod
    def get_spacing(base_spacing: int, breakpoint: Breakpoint) -> int
    
    @staticmethod
    def get_grid_columns(breakpoint: Breakpoint) -> int
    
    @staticmethod
    def get_container_padding(breakpoint: Breakpoint) -> dict
```

### 2. Enhanced Theme Module (`theme.py`)

Adicionar funções responsivas ao módulo de tema existente:

```python
def get_responsive_font_size(base_size: int, width: int) -> int:
    """Retorna tamanho de fonte baseado na largura da tela"""
    
def get_responsive_padding(base_padding: int, width: int) -> int:
    """Retorna padding baseado na largura da tela"""
    
def get_responsive_spacing(base_spacing: int, width: int) -> int:
    """Retorna spacing baseado na largura da tela"""
```

### 3. Page Components Enhancement

Cada página será refatorada para usar o sistema responsivo:

**home.py**:
- Botões com largura adaptativa
- Espaçamento dinâmico entre elementos
- Tamanhos de fonte responsivos

**services.py**:
- GridView com runs_count dinâmico baseado em breakpoint
- Cards com largura e padding adaptativos
- Ícones com tamanhos responsivos

**portfolio.py**:
- Imagens com dimensões responsivas
- Layout de grid adaptativo
- Espaçamento entre projetos dinâmico

**coins.py**:
- Gráfico com altura adaptativa
- Container com padding responsivo
- Loading state otimizado

**contact.py**:
- Campos de formulário com largura 100% em mobile
- Validação aprimorada
- Feedback visual melhorado

**about.py**:
- Container com largura máxima responsiva
- Espaçamento vertical adaptativo
- Texto com alinhamento otimizado

### 4. Test Suite Structure

```
tests/
├── __init__.py
├── conftest.py                 # Fixtures globais
├── test_theme.py              # Testes do módulo theme
├── test_responsive.py         # Testes do sistema responsivo
├── pages/
│   ├── __init__.py
│   ├── test_home.py          # Testes da página home
│   ├── test_services.py      # Testes da página services
│   ├── test_about.py         # Testes da página about
│   ├── test_contact.py       # Testes da página contact
│   ├── test_coins.py         # Testes da página coins
│   └── test_portfolio.py     # Testes da página portfolio
└── test_app.py               # Testes do app principal
```

## Data Models

### ResponsiveBreakpoint Model

```python
@dataclass
class ResponsiveBreakpoint:
    name: str
    min_width: int
    max_width: Optional[int]
    font_scale: float
    spacing_scale: float
    grid_columns: int
    container_padding: int
```

### TestPageMock Model

```python
@dataclass
class TestPageMock:
    width: int
    height: int
    route: str
    controls: List
    overlay: List
    
    def go(self, route: str) -> None
    def update(self) -> None
    def run_task(self, task) -> None
```

## Error Handling

### Responsive System

1. **Invalid Width Values**: Se width for None ou inválido, usar valor padrão de 1024px (desktop)
2. **Breakpoint Detection Failure**: Fallback para breakpoint DESKTOP
3. **Missing Responsive Config**: Usar valores base sem escala

### Testing System

1. **Import Errors**: Testes devem falhar graciosamente se módulos não existirem
2. **Mock Failures**: Fixtures devem ter valores padrão seguros
3. **Assertion Errors**: Mensagens claras indicando o que falhou e valores esperados vs obtidos

## Testing Strategy

### Unit Tests Coverage

1. **Theme Module** (test_theme.py):
   - Teste de get_theme() retorna objeto Theme válido
   - Teste de get_button_style() retorna ButtonStyle com propriedades corretas
   - Teste de get_text_style() com diferentes parâmetros
   - Teste de get_shadow() retorna BoxShadow válido
   - Teste de funções responsivas com diferentes larguras

2. **Responsive Module** (test_responsive.py):
   - Teste de detecção de breakpoint para cada faixa de largura
   - Teste de cálculo de font_size responsivo
   - Teste de cálculo de spacing responsivo
   - Teste de grid_columns para cada breakpoint
   - Teste de container_padding para cada breakpoint

3. **Page Components**:
   - Teste de renderização de conteúdo
   - Teste de responsividade em diferentes larguras
   - Teste de handlers de eventos
   - Teste de validações (formulários)
   - Teste de estados de loading/error

4. **App Principal** (test_app.py):
   - Teste de criação de header em mobile/desktop
   - Teste de criação de footer
   - Teste de navegação entre rotas
   - Teste de modal de login
   - Teste de resize handler

### Test Fixtures (conftest.py)

```python
@pytest.fixture
def mock_page():
    """Mock de ft.Page para testes"""
    
@pytest.fixture
def mobile_page():
    """Mock de Page com largura mobile (400px)"""
    
@pytest.fixture
def tablet_page():
    """Mock de Page com largura tablet (768px)"""
    
@pytest.fixture
def desktop_page():
    """Mock de Page com largura desktop (1920px)"""
    
@pytest.fixture
def theme_colors():
    """Dicionário de cores do tema"""
```

### Test Execution

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=. --cov-report=html --cov-report=term

# Executar testes específicos
pytest tests/test_theme.py
pytest tests/pages/test_home.py

# Executar com verbose
pytest -v

# Executar com output detalhado
pytest -vv -s
```

## Implementation Notes

### Responsive Implementation Priority

1. **Phase 1**: Criar módulo de utilidades responsivas
2. **Phase 2**: Atualizar theme.py com funções responsivas
3. **Phase 3**: Refatorar páginas para usar sistema responsivo
4. **Phase 4**: Testar em diferentes resoluções

### Testing Implementation Priority

1. **Phase 1**: Configurar pytest e criar fixtures
2. **Phase 2**: Implementar testes de módulos base (theme, responsive)
3. **Phase 3**: Implementar testes de páginas
4. **Phase 4**: Implementar testes de integração (app.py)

### Performance Considerations

1. **Caching**: Manter cache de valores calculados para breakpoints
2. **Lazy Loading**: Carregar componentes pesados apenas quando necessário
3. **Debouncing**: Aplicar debounce em resize handlers para evitar re-renders excessivos
4. **Test Performance**: Manter tempo de execução de testes < 30s usando mocks eficientes

### Accessibility Considerations

1. **Touch Targets**: Mínimo 44x44px em todos os breakpoints
2. **Font Sizes**: Mínimo 14px para texto de corpo em mobile
3. **Contrast**: Manter ratios de contraste WCAG AA
4. **Focus States**: Garantir estados de foco visíveis em todos os elementos interativos

## Dependencies

### New Dependencies

```toml
[project.optional-dependencies]
test = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.0",
]
```

### Configuration Files

**pytest.ini**:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --cov=.
    --cov-report=term-missing
    --cov-report=html
```

**.coveragerc**:
```ini
[run]
omit = 
    tests/*
    */__pycache__/*
    */venv/*
    */dist/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:
```

## Validation Criteria

### Responsive Design Validation

1. Testar em Chrome DevTools com diferentes dispositivos
2. Validar em larguras: 375px (mobile), 768px (tablet), 1920px (desktop)
3. Verificar ausência de scroll horizontal
4. Confirmar que todos os elementos são clicáveis/tocáveis
5. Validar carregamento de imagens em diferentes resoluções

### Testing Validation

1. Cobertura de código >= 80%
2. Todos os testes passando (0 failures)
3. Tempo de execução < 30 segundos
4. Nenhum warning de deprecação
5. Relatório de cobertura HTML gerado com sucesso
